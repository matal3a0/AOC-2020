#!/usr/bin/env python

import sys,math

def decode(code,low,high):
  for c in code:
    if c in 'FL':
      high -= math.floor((high-low)/2)+1
    elif c in 'BR':
      low += math.ceil((high-low)/2)
  return low 


def main():
  seats = []

  for line in sys.stdin.readlines():
    row = decode(line[:-4],0,127)
    col = decode(line[-4:],0,7)
    seats.append(row*8+col)

  seats.sort()
  print('Highest:',seats[-1])

  for i in range(seats[0], seats[-1]):
    if not i in seats:
      print("My seat:",i)


if __name__ == "__main__":
  main()
