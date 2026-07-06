from math import gcd

def findCoprime(phi):
  flag = True

  count = 2
  while flag:
    coprime = gcd(count, phi)
    
    if coprime == 1:
      return count

    count += 1
