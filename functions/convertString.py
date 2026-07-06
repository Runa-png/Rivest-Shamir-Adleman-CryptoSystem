def convertString(string: str):
  def NormaliseResults(intList):
    stringList = list(map(str, intList))

    normalisedStrList = list(map(threeChars, stringList))

    return normalisedStrList

  def threeChars(char):
    new = ("0" * (3 - len(char)) + char)
    return new
  
  stringList = list(string)

  ascii = list(map(ord, stringList))
  
  strAscii = NormaliseResults(ascii)

  normalisedAsciiString = "".join(strAscii)
  
  return normalisedAsciiString

def convertInt(integer: int):
  badString = str(integer)

  # Should the string not divide by 3 evenly we know there were 0s during conversion from str to int
  goodString = "0" * (3 - (len(badString) % 3)) + badString

  # Splitting string into 3 seperate blocks
  count = 0
  splitList = []
  
  while count != len(goodString):
    splitList.append(goodString[count:count+3])
    count += 3
  
  integerList = list(map(int, splitList))
  characterList = list(map(chr, integerList))
  
  decryptedString = "".join(characterList)

  return decryptedString
