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

def decryptData(username, message):
  config = Config
  messageDataVar = messageData

  key = getUserPrivateKey(username)

  messageDataVar.message = encrypted

  splitMessageList = splitString(messageDataVar.message, config.maxCount)

  splitMessageListInt = map(int, splitMessageList)
  
  decryptedAsciiList = list(map(lambda x: decrypt(x, key), splitMessageListInt))

  decryptedCharacterList = list(map(chr, decryptedAsciiList))

  decryptedString = "".join(decryptedCharacterList)
  
  return (decryptedString)

class Config:
  # Choose how many digits the prime numbers should have
  digitCount = 4
  # Choose the maximum digits the character count can have (in 9s)
  maxCount = 99

class messageData:
  message = ""
  length = 0

if __name__ == '__main__':
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
      username = input("What is your username: ")
      encrypted = input("Encrypted message: ")

      decrypted = decryptData(username, encrypted)

      print("Message: ", str(decrypted))

    case _:
      print("Invalid Option")



