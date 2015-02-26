#!/usr/bin/env python

# timertest - A Python command line util for examining optimal download times
# when using urllib2.urlopen and reading data in chunks using .read(bytes)
#
# Version: 1 - 24/02/2015
# Stephen Angell
# stephen@x50.com


import time
import os
import urllib2


testdl = "http://traffic.libsyn.com/timferriss/Arnold_5_min_-_final.mp3"
chunkmulti = 4
numpass = 5

while (chunkmulti < 17):
	passtime = 0
	passattempt = 1
	while (passattempt <= numpass):
	    start = time.time()
	    req = urllib2.urlopen(testdl)
	    CHUNK = chunkmulti * 1024
	    with open("test.mp3", 'wb') as fp:
		    while True:
			    chunk = req.read(CHUNK)
			    if not chunk: break
			    fp.write(chunk)
	    end = time.time()
	    passtime += end - start
	    os.remove("test.mp3")
	    passattempt += 1
	print "Chunk size multiplier ", chunkmulti , " took ", passtime / passattempt, " seconds"
	chunkmulti += 1


