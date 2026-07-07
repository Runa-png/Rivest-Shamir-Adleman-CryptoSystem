from functions.generateUser import connect

def getUserPublicKey(username):
  connection, cursor = connect()

  data = cursor.execute("SELECT public,common FROM keys WHERE username=?", (username.lower(),)).fetchall()

  if not data:
    print("User does not exist")
    exit()
  else:
    data = data[0]
    data = list(map(int, data))

  return data

def getUserPrivateKey(username):
  connection, cursor = connect()

  data = cursor.execute("SELECT private,common FROM keys WHERE username=?", (username.lower(),)).fetchall()

  if not data:
    print("User does not exist")
    exit()
  else:
    data = data[0]
    data = list(map(int, data))

  return data
