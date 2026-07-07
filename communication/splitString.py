def splitString(message, count):
  print(message, count)

  resultingList = []

  # This is the amount of characters allocated to showing digit count
  digitCount = len(str(count))

  ### Then get the full byte of data
  
  while message:
    ## Numbers after this in a block
    digits = message[0:digitCount]

    ## Then the full block
    characterWithCount = message[0:int(digits)+digitCount]

    # Remove the counter
    character = characterWithCount[digitCount:]

    print(character) # and thats the encrypted character

    resultingList.append(character)

    message = message[int(digits)+digitCount:]
  
  return (resultingList)