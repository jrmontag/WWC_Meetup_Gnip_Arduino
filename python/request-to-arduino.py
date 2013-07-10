#!/usr/bin/env python
#  WWC Meetup
#     Gnip and Arduino Fun!
#     2013-07-10
###########################################
# Make sure you have pyserial and requests 
# packages install and working for your python 
# installation:
#    Pyserial http://pyserial.sourceforge.net/
#    Requests http://docs.python-requests.org/en/latest/
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
try:
    serial_dev = '/dev/tty.usbmodemfd121'
    ser = serial.Serial(serial_dev, 9600)
except serial.serialutil.SerialException, e:
    print >>sys.stderr, "Check your serial port definition: (%s)"%(str(e))
    ser = None
###########################################
# Terms you want to track -- discussion in meetup
# up to 9 terms here:
terms_to_watch = ["orange", "blue"]
# simple protocol for communication with arduino
terms = { terms_to_watch[i]:1+i for i in range(len(terms_to_watch))}

# for testing, writes and reads any string from serial device
def echo(x):
    print "writing to arduino: ", x
    if ser:
        ser.write("%s\n"%x)
    print "reading from arduino: ", ser.readline()

# This function writes to the arduino through serial port
def write_term(x):
    res = "None"
    if ser:
        ser.write(str(x))
        res = ser.read()
    else:
        print >>sys.stderr, "No serial connection detected."
    return res    

TIME_DELAY = 3 # seconds
THRESHOLD = 20 # minimum count change needed in order to signal arduino

if __name__=="__main__":
    # initial the counters for the last terms read from the server
    last = {x:0 for x in terms}
    # build a format string of the right length
    tmpfmt = "%s:"*len(terms)
    # repeat this forever (?)
    while True:
        tmp = tmpfmt%tuple(terms.keys())
        response = requests.get(CNT_URL%tmp)
        try:
            res_dict = json.loads(response.text)
        except ValueError:
            print >>sys.stderr, "Invalid json:", response.text
        # let's see some output
        #print >>sys.stderr,response.text
        # step through the terms and do something
        for c in terms:
            if c in res_dict["keys"]:
                # calculate count diffs from last time through the loop
                diff = int(res_dict["keys"][c]["count"]) - last[c]
                if diff > THRESHOLD:
                    # write to the arduino over the serial port
                    print "term: %10s  count change: %5d  blinks: %d  reponse: %s"%(c, diff, terms[c], write_term(terms[c]))
                    # keep track of counts for next diff
                    last[c] = int(res_dict["keys"][c]["count"])
                else:
                    print "term: %10s  skipping: %d <= %d"%(c, diff, THRESHOLD)
                time.sleep(TIME_DELAY)
