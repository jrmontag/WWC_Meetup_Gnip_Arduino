#!/usr/bin/env python
import serial
import requests
import json
import sys
import time

TOP_URL = "http://shendrickson3.gnip.com:8090/redr8r/v1/top.json"
# colon delimited list of items to look for in the redis store
CNT_URL = "http://shendrickson3.gnip.com:8090/redr8r/v1/%s/count.json"

ser = serial.Serial('/dev/tty.usbmodemfd121', 9600)
#ser = serial.Serial('/dev/tty.usbmodemfa131', 9600)

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
