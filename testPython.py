import os
from subprocess import * 

#run child script 1
p = Popen('MyPython1.py', shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print output[0]

#run child script 2
p = Popen('MyPython2.py', shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print output[0]

