from functions.genPrime import uniquePrime
from functions.findCoprime import findCoprime

from functions.generateKeys import genKeys
from functions.generateUser import addUser, generateTable

from communication.convertAscii import convertToAscii
from communication.encrypt import encrypt
from communication.decrypt import decrypt
from communication.fetchKeys import getUserPrivateKey, getUserPublicKey
from communication.normalise import normaliseList
from communication.splitString import splitString

class Config:
  # Choose how many digits the prime numbers should have
  digitCount = 4
  # Choose the maximum digits the character count can have (in 9s)
  maxCount = 99

class messageData:
  message = ""
  length = 0

def main():
  config = Config()

  unencryptedMessage = (config.message)

  isString = False
  config.digitCount = 7

  private, public = genKeys(config)
  print(f"Public Key: {public}")

  config.convert()

  message = int(config.message)

  ## Encrypt
  encrypted = encrypt(message, public)

  ## Decrypt
  decrypted = decrypt(encrypted, private)

  ## Reverse convert to integers
  decryptedString = convertInt(decrypted, 8)


  print(f" Message:  {unencryptedMessage} \n Encrypted: {encrypted} \n Decrypted: {decryptedString}")


if __name__ == '__main__':
  # flag = True
  # while flag:
  #   main()
  #   flag = False

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
      config = Config
      
      messageDataVar = messageData
      
      username = input("What is the user you're sending to: ")
      
      message = input("\nWhat is the message: ")
      messageDataVar.message = message

      asciiList = convertToAscii(messageDataVar.message)

      key = getUserPublicKey(username)

      encryptedAscii = list(map(lambda x: encrypt(x, key), asciiList))

      normalisedEncryptedAscii = normaliseList(encryptedAscii, messageDataVar, config)

      normalisedEncryptedString = "".join(normalisedEncryptedAscii)

      print("")
      print(normalisedEncryptedString)
    
    case "3":
      config = Config
      messageDataVar = messageData

      username = input("What is your username: ")
      key = getUserPrivateKey(username)

      encrypted = input("Encrypted message: ")
      messageDataVar.message = encrypted

      print(messageDataVar.message)

      splitMessageList = splitString(messageDataVar.message, config.maxCount)
      print(splitMessageList)

      splitMessageListInt = map(int, splitMessageList)
      
      decryptedAsciiList = list(map(lambda x: decrypt(x, key), splitMessageListInt))
      print(decryptedAsciiList)

      decryptedCharacterList = list(map(chr, decryptedAsciiList))
      print(decryptedCharacterList)

      decryptedString = "".join(decryptedCharacterList)
      print(decryptedString)

    case _:
      print("Invalid Option")

