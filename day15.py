#!/usr/bin/env python

import sys

data = list(map(int, sys.stdin.read().split(',')))

# { nr: [ lastspoken, prevspoken ] }
numbers = {}
turn = 1

while turn <= 30000000: 
#while turn <= 2020: 
  #if turn % 10000 == 0:
    #print('Turn:',turn)

  if turn <= len(data): # Starting numbers
    numbers[data[turn-1]] = [ turn, 0 ]
    last = data[turn-1]
    notseen = True
  else:
    if notseen:
      last = 0
    else:
      last = numbers[last][0] - numbers[last][1]

    if last not in numbers:
      notseen = True
      numbers[last] = [ turn, 0 ]
    else:
      notseen = False
      numbers[last][1] = numbers[last][0]
      numbers[last][0] = turn
  turn += 1

print('Turn:',turn-1,'Last:',last)
