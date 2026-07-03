import random
from sympy import isprime
import math

def generatePrime(n):
  primeFound = False
  
  while not primeFound:
    randomNumber = random.randint(int("1"+"0"*(n-1)), int("9"*n))
    primeFound = isprime(randomNumber)

  return randomNumber

def main():
  primeKeyOne = generatePrime(5)
  primeKeyTwo = generatePrime(5)

  n = primeKeyOne * primeKeyTwo
  phi = (primeKeyOne - 1) * (primeKeyTwo - 1)
  e = math.gcd()

  print(n)

def coprime(a, b):
  return math.gcd(a, b) == 1

if __name__ == '__main__':
  main()
