from .generateUser import connect

def getUserPublicKey(username):
  connection, cursor = connect()

  data = cursor.execute("SELECT public,common FROM keys WHERE username=?", (username.lower(),)).fetchall()

  if not data:
    print("User does not exist")
    return False
  else:
    data = data[0]

  return data
