#!/usr/bin/env python3

def print_fibonacci(length):
 fibonacci = []
 if length > 0:
  fibonacci.append(0)
 if length >= 2:
  fibonacci.append(1)
 for i in range(2, length):
  fibonacci.append(fibonacci[-1] + fibonacci[-2])

 print(fibonacci)
