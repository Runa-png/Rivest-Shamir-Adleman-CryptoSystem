def convertToAscii(string: str):
  listString = list(string)
  
  # ord just converts letters to their ascii codes
  listAscii = list(map(ord, listString))

  return listAscii