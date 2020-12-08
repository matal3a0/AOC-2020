#!/usr/bin/env python

import sys,copy

def run(code):
  ptr = 0
  acc = 0
  history = []

  while(ptr not in history):
    history.append(ptr)    
    instr = code[ptr][0]
    val = int(code[ptr][1])

    if instr == 'acc':
        acc += val
    if instr == 'jmp':
        ptr += val
    else:
      ptr += 1

    if ptr == len(code):
      print('Part 2:',acc)
      sys.exit(0)

  return acc

def main():
  code = [ x.strip().split() for x in sys.stdin.readlines() ]

  print('Part 1:',run(code))

  for i in range(len(code)):
    code_copy = copy.deepcopy(code)

    if code_copy[i][0] == 'jmp':
      code_copy[i][0] = 'nop'
    elif code_copy[i][0] == 'nop':
      code_copy[i][0] = 'jmp'

    run(code_copy)
      
    
if __name__ == "__main__":
  main()
