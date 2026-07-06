def encrypt(message, public):
  e, n = public
  return pow(message,e,n)