#!/usr/bin/env python

import sys

slopes = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
totaltrees = 1
grid = []

for line in sys.stdin.readlines():
  grid.append(list(x for x in line if x != '\n'))

width = len(grid[0])
height = len(grid)

for s in slopes:
  x = s[0]
  y = s[1]

  xpos, ypos, trees = 0, 0, 0
  
  while ypos < height-1:
    xpos = (xpos + x) % width
    ypos += y
    if grid[ypos][xpos] == '#':
      trees += 1
  print("Slope:",s,"Trees:",trees)
  
  totaltrees *= trees

print("Total trees:", totaltrees)
