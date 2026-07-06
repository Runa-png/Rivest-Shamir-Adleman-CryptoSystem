from functions.genPrime import uniquePrime
from functions.findCoprime import findCoprime
from functions.convertString import convertString

class Config:
  message = 73878237
  digitCount = int(len(str(message)) / 2) + 1

  def convert(self):
    self.message = convertString(self.message)

def main():
  config = Config()

  config.convert()

  # Prime one and prime two
  p,q = uniquePrime(config.digitCount)

  n = p * q

  # Regenerate bytes
  count = 0
  while n < config.message:
    exit()

  
  #print("generating phi")
  phi = (p - 1) * (q - 1)

  #print("finding coprime")
  e = findCoprime(phi)

  ## d is multiplicative inverse of e
  #print("Getting inverse")
  d = pow(e, -1, phi)

  ## Testing
  #print("Testing")
  if (e*(e**-1)) % phi != 1:
    print("Multiplicative inverse DIDN'T work correctly")

  private = (n,d)
  public = (n,e)

  #print("Encrypting")
  ## Encrypt
  m = config.message

  c = pow(m,e,n)
  # c = (m**e) % n

  ## Decrypt
  #print("Decrypting")
  
  decrypted = pow(c,d,n)
  #decrypted = (c**d) % n

  if decrypted != m:
    print(f"Message: {m} Encrypted: {c} Decrypted: {decrypted}")
    print(f"prime one: {p}, prime two: {q}")
    print(f"Phi: {phi}")
    print(f"Inverse E: {d}, E: {e}")
    print(f"")
  else:
    print(f"Message {m} Decrypted {decrypted}")


if __name__ == '__main__':
  flag = True
  while flag:
    main()
    # flag = False
