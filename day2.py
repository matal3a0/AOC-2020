#!/usr/bin/env python

valida = 0
validb = 0

with open("day2.txt") as f:
  for line in f:
    a, b, pw = line.split()
    m, n = map(int, a.split('-'))
    c = b.strip(':')

    if pw.count(c) >= m and pw.count(c) <= n:
      valida += 1
    if pw[m-1] == c and not pw[n-1] == c or pw[n-1] == c and not pw[m-1] == c:
      validb += 1

print("Valid passwords Part 1:",valida)
print("Valid passwords Part 2:",validb)

    
