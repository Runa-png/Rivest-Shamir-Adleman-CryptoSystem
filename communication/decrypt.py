def decrypt(encrypted, private):
  d, n = private
  return pow(encrypted,d,n)