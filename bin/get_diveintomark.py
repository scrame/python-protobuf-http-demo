#!/usr/bin/python
import httplib
httplib.HTTPConnection.debuglevel = 1    

import urllib
data = urllib.urlopen('http://www.diveintomark.org/xml/atom.xml').read()    
print data
