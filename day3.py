#!/usr/bin/env python

import sys

slopes = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
totaltrees = 1
grid = []

for line in sys.stdin.readlines():
  grid.append(list(x for x in line if x != '\n'))

for s in slopes:
  x, y, trees = 0, 0, 0
  
  while y < len(grid)-1:
    x = (x + s[0]) % len(grid[0])
    y += s[1]
    if grid[y][x] == '#':
      trees += 1
  print("Slope:",s,"Trees:",trees)
  totaltrees *= trees

print("Total trees:", totaltrees)
