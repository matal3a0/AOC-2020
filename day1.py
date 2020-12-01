#!/usr/bin/env python

data = ([int(i) for i in open('day1.txt').readlines()])

for x in data:
  for y in data:
    if y+x == 2020:
      print('a:',x*y)
    for z in data:
      if y+x+z == 2020:
        print('b:',x*y*z)
        
