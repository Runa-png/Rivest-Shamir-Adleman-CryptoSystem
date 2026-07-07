import sqlite3


def connect():
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()

  return connection, cursor

def generateTable():
  connection, cursor = connect()

  cursor.execute("CREATE TABLE IF NOT EXISTS keys (username PRIMARY KEY, public, private, common)")

def addUser(username, private, public):
  connection, cursor = connect()

  username = username.lower()

  try:
    cursor.execute("INSERT INTO keys (username, public, private, common) VALUES (?,?,?,?)", (username, public[0], private[0], public[1]))
    return True
  except sqlite3.IntegrityError:
    print("Username already in use")
    return False

  connection.commit()
  connection.close()