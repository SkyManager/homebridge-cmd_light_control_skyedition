#!/usr/bin/env python
import sys
import telnetlib
import time
from sys import argv

host = argv[1]
tn = telnetlib.Telnet(host, 1000)
digit = int(argv[2])
digit = int(digit*2.5)
tn.write("bright 60 " + str(digit) + "\n")
#time.sleep(1)
#s = tn.read_until("\n")
#print s
tn.close();
