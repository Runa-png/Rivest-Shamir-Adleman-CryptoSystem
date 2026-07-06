from sympy import isprime
import random

def genPrime(digits):
  flag = True

  while flag:
    prime = random.randint(int("1" + "0" * (digits-1)), int("9" * (digits)))

    primeStatus = isprime(prime)

    if primeStatus:
      print("Found prime")
      return prime

def uniquePrime(digits):  
  p = genPrime(digits)
  q = genPrime(digits)

  while p == q:
    p = genPrime(digits)
    q = genPrime(digits)
  
  return p,q