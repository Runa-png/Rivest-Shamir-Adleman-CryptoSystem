def splitString(message, count):
  resultingList = []

  # This is the amount of characters allocated to showing digit count
  digitCount = len(str(count))

  ### Then get the full byte of data
  
  while message:
    ## Numbers after this in a block
    digits = message[0:digitCount]

    ## Then the full block
    characterWithCount = message[0:int(digits)+digitCount]

    # Remove the counter so its jsut ascii of the character
    character = characterWithCount[digitCount:]

    resultingList.append(character)

    message = message[int(digits)+digitCount:]
  
  return (resultingList)