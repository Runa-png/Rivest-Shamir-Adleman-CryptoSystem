import sqlite3


def connect():
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()

  return connection, cursor

def generateTable():
  connection, cursor = connect()

  cursor.execute("CREATE TABLE IF NOT EXISTS keys (username TEXT PRIMARY KEY, public TEXT, private TEXT, common TEXT)")

def addUser(username, private, public):
  connection, cursor = connect()

  username = username.lower()

  try:
    cursor.execute("INSERT INTO keys (username, public, private, common) VALUES (?,?,?,?)", (str(username), str(public[0]), str(private[0]), str(public[1])))
    connection.commit()
    connection.close()
    return True
  except sqlite3.IntegrityError:
    print("Username already in use")
    return False

  connection.commit()
  connection.close()