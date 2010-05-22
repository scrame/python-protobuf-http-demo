#!/usr/bin/python
import httplib
httplib.HTTPConnection.debuglevel = 1    

import urllib
data = urllib.urlopen('http://www.cnn.com').read()    
print data
