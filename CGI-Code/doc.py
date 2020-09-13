#!/usr/bin/python3

import cgi

import subprocess


print("content-type: text/html")
print()

imginput = cgi.FieldStorage()
nameinput = cgi.FieldStorage()
imgcmd = imginput.getvalue("im")
namecmd = nameinput.getvalue("y")
imgload = subprocess.getoutput("sudo docker pull " + imgcmd)
output = subprocess.getoutput("sudo docker run -dit --name " + namecmd + " " + imgcmd)
result = subprocess.getstatusoutput("sudo docker ps -a"  )
print(result)
