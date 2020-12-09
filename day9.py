#!/usr/bin/env python

import sys

preamble = 25
pos = preamble

data = list(map(int,sys.stdin.readlines())) 

for d in data[preamble:]:
  found = False
  for x in range(pos-preamble,pos):
    for y in range(pos-preamble,pos):
      if data[x]+data[y] == d and data[x] != data[y]:
        found = True
        break
    if found:
      break
  pos += 1

  if not found:
    print('Part 1:',d)
    break
    
for x in range(0,len(data)-2):
  found = False
  for y in range(x+1,len(data)-1):
    if sum(data[x:y]) == d:
      print('Part 2:',min(data[x:y])+max(data[x:y]))
      found = True
      break
  if found:
    break
