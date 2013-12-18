#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from ipoperate import ip2long, long2ip
 
if len(sys.argv) == 1:
    f = sys.stdin
else:
    f = open(sys.argv[1]) 
start = []
v = 0

for i in f:
    n = int(ip2long(i.strip('\n'))) # current value
    if abs(n - v) > 5:
        start.append(v)
        start.append(n)
    v = n # former value
else:
    start.append(n)

result = [long2ip(i) for i in start]
numb = 1
while numb<len(result):
    print result[numb] + '-' + result[numb+1].split('.')[-1]
    numb = numb + 2
