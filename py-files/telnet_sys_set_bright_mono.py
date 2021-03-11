#!/usr/bin/env python
import sys
import telnetlib
import time
from sys import argv

host = argv[1]
tn = telnetlib.Telnet(host, 1000)
digit = int(argv[3])
digit = int(digit*2.5)
ch = argv[2]
tn.write("bright " + ch + " " + str(digit) + "\n")
#time.sleep(1)
#s = tn.read_until("\n")
#print s
tn.close();
