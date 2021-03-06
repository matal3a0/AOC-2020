#!/usr/bin/env python

import sys

valida = 0
validb = 0

for line in sys.stdin.readlines():
  a, b, pw = line.split()
  m, n = map(int, a.split('-'))
  c = b.strip(':')

  if m <= pw.count(c) <= n:
    valida += 1
  #if pw[m-1] == c and not pw[n-1] == c or pw[n-1] == c and not pw[m-1] == c:
  if (pw[m-1] == c) ^ (pw[n-1] == c):
    validb += 1

print("Valid passwords Part 1:",valida)
print("Valid passwords Part 2:",validb)

    
