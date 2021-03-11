#!/usr/bin/env python
import sys
import telnetlib
import time
from sys import argv
import re

host = argv[1]
ch = argv[2]
tn = telnetlib.Telnet(host, 1000)
tn.write("get realstate\n")
#time.sleep(1)
s = tn.read_until("\0", 0.1)
#print s
tn.close();
#arr_tmp = s.split(' *')
arr_tmp = re.compile('\#\d{3}\s\*|\#\d{3}|\w{6}\s\=\w\s\*\d{3}\s\*').split(s)

def f(ch):
    return {
        '11': int(arr_tmp[1])/2.5,
        '12': int(arr_tmp[2])/2.5,
        '13': int(arr_tmp[3])/2.5,
        '21': int(arr_tmp[4])/2.5,
        '22': int(arr_tmp[5])/2.5,
        '23': int(arr_tmp[6])/2.5,
        '31': int(arr_tmp[7])/2.5,
        '32': int(arr_tmp[8])/2.5,
        '33': int(arr_tmp[9])/2.5,
        '41': int(arr_tmp[10])/2.5,
        '42': int(arr_tmp[11])/2.5,
        '43': int(arr_tmp[12])/2.5,
        '51': int(arr_tmp[13])/2.5,
        '52': int(arr_tmp[14])/2.5,
        '53': int(arr_tmp[15])/2.5,
    }.get(ch, "an out of range number")    # 9 is default if x not found
print f(ch)
