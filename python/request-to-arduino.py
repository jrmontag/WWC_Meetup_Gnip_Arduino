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

colors = ["red", "blue", "yellow", "orange"]

def echo(x):
    print "writing input: ", x
    ser.write("%s\n"%x)
    print "reading arduino: ", ser.readline()

def color(x):
    x = x.lower()
    if x in colors:
        ser.write(x[0])
    else:
        print >>sys.stderr, "Invalid color (%s)"%x

if __name__=="__main__":
    last = {x:0 for x in colors}
    while True:
        tmp = "%s:%s:%s:%s"%tuple(colors)
        response = requests.get(CNT_URL%tmp)
        try:
            res_dict = json.loads(response.text)
        except ValueError:
            print >>sys.stderr, "Invalid json", response.text
        #echo(response.text)
        print response.text
        for c in colors:
            if c in res_dict["keys"]:
                diff = int(res_dict["keys"][c]["count"]) - last[c]
                if diff > 20:
                    color(c)
                    print diff, ser.read()
                    last[c] = int(res_dict["keys"][c]["count"])
                else:
                    print diff, "skipping"
                time.sleep(1.5)
