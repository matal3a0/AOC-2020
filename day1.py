#!/usr/bin/env python

with open("day1.txt") as f:
  data = list(map(int, f.read().splitlines()))

for x in data:
  for y in data:
    if y+x == 2020:
      print('a:',x*y)
    for z in data:
      if y+x+z == 2020:
        print('b:',x*y*z)
        
