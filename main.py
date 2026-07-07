from functions.genPrime import uniquePrime
from functions.findCoprime import findCoprime
from functions.convertString import convertString, convertInt
from functions.encrypt import encrypt
from functions.decrypt import decrypt

from functions.generateKeys import genKeys
from functions.generateUser import addUser, generateTable
from functions.fetchKeys import getUserPublicKey

class Config:
  message = "123"
  digitCount = (int(len(str(message)) / 2) + 1) * 3

  def convert(self):
    self.message = convertString(self.message)

def main():
  config = Config()

  unencryptedMessage = (config.message)

  isString = False
  try:
    config.message = int(config.message)
  except ValueError:
    print("Converting to string")
    config.convert()
    isString = True

  private, public = genKeys(config)
  print(f"Public Key: {public}")

  message = int(config.message)

  ## Encrypt
  encrypted = encrypt(message, public)

  ## Decrypt
  decrypted = decrypt(encrypted, private)

  ## Reverse convert to integers if it started as a string
  if isString:
    decryptedString = convertInt(decrypted)
  else:
    decryptedString = decrypted

  print(f" Message:  {unencryptedMessage} \n Encrypted: {encrypted} \n Decrypted: {decryptedString}")


if __name__ == '__main__':
  flag = True
  while flag:
    main()
    flag = False

  generateTable()

  print("___ASYMETRIC___CIPHER___")
  print("1. Create User")
  print("2. Encrypt")
  print("3. Decrypt")
  print("________________________ \n")
  choice = input("Choice: ")

  match choice:
    case "1":
      username = input("Username: ")
      
      config = Config
      private, public = genKeys(config)
      addUser(username, (private), (public))
    
    case "2":
      username = input("Who is this message for? ")

      key = getUserPublicKey(username)

      print(key)
    
    case _:
      print("Invalid Option")

