def convertToAscii(string: str):
  listString = list(string)
  listAscii = list(map(ord, listString))

  return listAscii