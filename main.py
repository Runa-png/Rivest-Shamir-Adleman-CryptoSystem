from functions.genPrime import uniquePrime
from functions.findCoprime import findCoprime
from functions.convertString import convertString, convertInt
from functions.encrypt import encrypt
from functions.decrypt import decrypt

from functions.generateKeys import genKeys

class Config:
  message = "INSERT YOU MESSAGE HERE"
  digitCount = (int(len(str(message)) / 2) + 1) * 3

  def convert(self):
    self.message = convertString(self.message)

def main():
  config = Config()

  unencryptedMessage = (config.message)

  config.convert()

  private, public = genKeys(config)
  print(f"Public Key: {public}")

  message = int(config.message)

  ## Encrypt
  encrypted = encrypt(message, public)

  ## Decrypt
  decrypted = decrypt(encrypted, private)

  ## Reverse convert to integers
  decryptedString = convertInt(decrypted)

  print(f" Message:  {unencryptedMessage} \n Encrypted: {encrypted} \n Decrypted: {decryptedString}")


if __name__ == '__main__':
  flag = True
  while flag:
    main()
    flag = False
