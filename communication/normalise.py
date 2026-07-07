def normaliseList(asciiList: list, messageClass, config):
  # Convert items in list to string
  asciiListString = list(map(str, asciiList))
  
  # Length of the longest value in list
  requiredLength = (len(max(asciiListString, key=len)))

  messageClass.length = requiredLength

  # Make each number the required size
  normalisedList = list(map(lambda x: normaliseItem(x, messageClass.length, config), asciiListString))

  return normalisedList

def normaliseItem(item, digits, config):
  text = ("0" * (len(item) - digits) + item)
  textCount = len(text)

  maxCount = config.maxCount

  if textCount > maxCount:
    print("Encryption length is too long for allocated digitCount in config class")
    exit()
  else:
    return ("0" * (len(str(maxCount)) - len(str(textCount))) + str(textCount) + text)