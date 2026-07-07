from .genPrime import uniquePrime
from .findCoprime import findCoprime


def genKeys(config):
  # Prime one and prime two
  print(config.digitCount)

  p,q = uniquePrime((int(len(str(config.message)) / 2) + 1) * config.digitCount)

  n = p * q

  # phi is the golden ratio
  phi = (p - 1) * (q - 1)

  # e is the coprime of phi, 2 prime numbers with no other factors than 1
  e = findCoprime(phi)

  ## d is multiplicative inverse of e
  d = pow(e, -1, phi)

  private = (d, n)
  public = (e, n)

  return private, public