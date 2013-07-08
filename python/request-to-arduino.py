#!/usr/bin/env python
#  WWC Meetup
#     Gnip and Arduino Fun!
#     2013-07-10
#
###########################################
#
# Make sure you have pyserial and requests packages install and working for your python installation
# Pyserial http://pyserial.sourceforge.net/
# Requests http://docs.python-requests.org/en/latest/
#
###########################################

import serial
import requests
import json
import sys
import time

###########################################
# Temporary Gnip interface to real tim social data
TOP_URL = "http://shendrickson3.gnip.com:8090/redr8r/v1/top.json"

# Example output
#  {
#          timestamp: 1373322884,
#          version: "v1",
#          topkeys: {
#              blue: 862,
#              justin: 1270,
#              egypt: 716,
#              sun: 1118,
#              one: 383,
#              black: 2428,
#              bieber: 1323,
#              amp: 407,
#              red: 1623,
#              obama: 690
#              }
#          }

CNT_URL = "http://shendrickson3.gnip.com:8090/redr8r/v1/%s/count.json"

# Example output
# {
#         keys: {
#             black: {
#                 count: 17628
#                 }
#             },
#         timestamp: 1373324445,
#         version: "v1"
#         }
###########################################
# ls the contents of your /dev folder.  Look for something
# like below. Change the string to match yours.

ser = serial.Serial('/dev/tty.usbmodemfd121', 9600)
#ser = serial.Serial('/dev/tty.usbmodemfa131', 9600)

###########################################

terms = ["red", "blue", "yellow", "orange", "black"]

def echo(x):
    print "writing input: ", x
    ser.write("%s\n"%x)
    print "reading arduino: ", ser.readline()

def write_term(x):
    x = x.lower()
    if x in terms:
        ser.write(x[0])
    else:
        print >>sys.stderr, "Invalid color (%s)"%x

TIME_DELAY = 1.5 # seconds

if __name__=="__main__":
    # initial the counters for the last terms read from the server
    last = {x:0 for x in terms}
    # build a format string of the right length
    tmpfmt = "%s:"*len(terms)
    # repeat this forever (?)
    while True:
        tmp = tmpfmt%tuple(terms)
        response = requests.get(CNT_URL%tmp)
        try:
            res_dict = json.loads(response.text)
        except ValueError:
            print >>sys.stderr, "Invalid json", response.text
        # let's see some output
        print response.text
        # step through the terms and do something
        for c in terms:
            if c in res_dict["keys"]:
                # calculate count diffs from last time through the loop
                diff = int(res_dict["keys"][c]["count"]) - last[c]
                if diff > 20:
                    # write to the arduino over the serial port
                    write_term(c)
                    # see what the arduino returns...
                    print diff, ser.read()
                    # log counts for next diff
                    last[c] = int(res_dict["keys"][c]["count"])
                else:
                    print >>sys.stderr,diff, "skipping"
                time.sleep(TIME_DELAY)
