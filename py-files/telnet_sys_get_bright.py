#!/usr/bin/env python
import sys
import telnetlib
import time
from sys import argv

host = argv[1]
tn = telnetlib.Telnet(host, 1000)
tn.write("get realstate\n")
#time.sleep(1)
s = tn.read_until("#")
#print s
tn.close();
arr_tmp = s.split(' *')
digit = int(arr_tmp[1])
digit = int(digit / 2.5)
print(str(digit)).replace("\n","")
