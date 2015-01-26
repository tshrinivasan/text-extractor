#!/usr/bin/python
import subprocess
import os

for (dirname, subshere, fileshere) in os.walk('.'):
#     print('[' + dirname + ']')
     for fname in fileshere:
	if fname.endswith('.html'): 
        	htmlfile = os.path.join(dirname, fname)
		print htmlfile
		command = "python /bin/html2text.py  " + htmlfile + " >> out.txt"
		print command
		os.system(command)

