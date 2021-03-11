#!/usr/bin/env python
import sys
import telnetlib
import time
from sys import argv

host = argv[1]
tn = telnetlib.Telnet(host, 1000)
tn.write("sys off\n")
#time.sleep(1)
s = tn.read_until("\n")
print s
tn.close();
