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


