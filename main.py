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
  primeKeyOne = generatePrime(500)
  primeKeyTwo = generatePrime(500)

  n = primeKeyOne * primeKeyTwo
  phi = (primeKeyOne - 1) * (primeKeyTwo - 1)

  for i in range(100,5000):
    status = coprime(phi,i)

    if status == True:
      e = i
      break

  print(e)

def coprime(a, b):
  status = math.gcd(a, b) == 1
  return status


if __name__ == '__main__':
  main()

https://www.cryptool.org/en/cto/rsa-step-by-step/