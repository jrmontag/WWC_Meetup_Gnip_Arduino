#WWC Meetup

Data science-y goodness with Gnip. 


##Install notes

###OS X
install official 2.7.5 Python binary: 

`http://www.python.org/ftp/python/2.7.5/python-2.7.5-macosx10.6.dmg`

install distribute & pip:

	$ curl -O http://python-distribute.org/distribute_setup.py
	$ python distribute_setup.py
	$ easy_install pip


### Windows 
install official 2.7.5 Python binary: 
`http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi` 

install setuptools: 
`http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools` 

[Download ==> setuptools-0.7.8.win-amd64-py2.5.exe] 

install pip:
`http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip`

[Download ==> pip-1.3.1.win-amd64-py2.7.exe]


((setuptools & pip ref: http://stackoverflow.com/a/12476379/1851811))


### After above, on either operating system, install the necessary packages: 
install req'd packages (possibly `sudo`):

	$ pip install requests
	$ pip install pyserial


##Party on, Wayne!

###Warm-up
1. Plug in your Arduino. 
2. Start Arduino app
3. Select appropriate Arduino Board (probably Uno) [Tools > Board]
4. Select correct serial port (probably `tty.usbmodem` on Linux/OS X, 0 or 1 on Windows) [Tools > Serial Port] 
5. Burn echo.ino onto your board. Follow instructions in the code & play with it.  

###Game Time
1. Find your serial port. Run this from your command line:

`ls /dev/ | grep tty.usbmodem`

2. Copy / paste the result as the `usbmodem` string near the top of `python/request-to-arduino.py`
3. Burn basic.ino onto your board. 
4. Run request-to-arduino.py script ( `./request-to-arduino.py` )
5. Experiment with search terms in the Python script 



