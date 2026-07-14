import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QHBoxLayout, QBoxLayout

class Login(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    # Create Login Page
    self.loginLayout = QtWidgets.QVBoxLayout(self)

    self.loginLayoutUsername = QtWidgets.QVBoxLayout()
    self.loginLayoutUsername.setDirection(QBoxLayout.Direction.LeftToRight)

    self.loginLayoutPassword = QtWidgets.QVBoxLayout()
    self.loginLayoutPassword.setDirection(QBoxLayout.Direction.LeftToRight)

    # Username Details

    self.loginLayoutUsernameTitle = QtWidgets.QLabel("Username", alignment=QtCore.Qt.AlignCenter)
    self.loginLayoutUsernameTitle.setFixedWidth(200)
    
    self.loginLayoutUsernameInput = QtWidgets.QTextEdit()
    self.loginLayoutUsernameInput.setFixedHeight(30)
    self.loginLayoutUsernameInput.setFixedWidth(400)

    # Password details

    self.loginLayoutPasswordTitle = QtWidgets.QLabel("Password", alignment=QtCore.Qt.AlignCenter)
    self.loginLayoutPasswordTitle.setFixedWidth(200)
    
    self.loginLayoutPasswordInput = QtWidgets.QTextEdit()
    self.loginLayoutPasswordInput.setFixedHeight(30)
    self.loginLayoutPasswordInput.setFixedWidth(400)

    # Add widgets

    self.loginLayoutUsername.addWidget(self.loginLayoutUsernameTitle)
    self.loginLayoutUsername.addWidget(self.loginLayoutUsernameInput)

    self.loginLayoutPassword.addWidget(self.loginLayoutPasswordTitle)
    self.loginLayoutPassword.addWidget(self.loginLayoutPasswordInput)
    
    # Add to the rendered page

    self.loginLayout.addLayout(self.loginLayoutUsername)
    self.loginLayout.addLayout(self.loginLayoutPassword)

class Encrypt(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    # Main Box
    self.encryptLayout = QtWidgets.QVBoxLayout(self)

    # Main Box Children
    
    # User chooses recipient
    self.recipientLayout = QtWidgets.QVBoxLayout()
    self.recipientLayout.setDirection(QBoxLayout.Direction.LeftToRight) 

    # Recipient title
    self.recipientLayoutTitle = QtWidgets.QLabel("Recipient Name")
    self.recipientLayoutTitle.setMaximumWidth(400)
    
    # Recipient Input
    self.recipientLayoutInput = QtWidgets.QTextEdit()
    self.recipientLayoutInput.setMaximumWidth(400)
    self.recipientLayoutInput.setMaximumHeight(30)

    # Add widgets for recipient layout
    self.recipientLayout.addWidget(self.recipientLayoutTitle)
    self.recipientLayout.addWidget(self.recipientLayoutInput)

    # Message Input
    self.messageLayout = QtWidgets.QVBoxLayout()
    self.messageLayout.setDirection(QBoxLayout.Direction.LeftToRight)

    # Message Title
    self.messageLayoutTitle = QtWidgets.QLabel("Message")
    self.messageLayoutTitle.setMaximumWidth(400)

    # Message Input
    self.messageLayoutInput = QtWidgets.QTextEdit()
    self.messageLayoutInput.setMaximumWidth(400)
    self.messageLayoutInput.setMaximumHeight(300)

    # Add widgets to the message layout
    self.messageLayout.addWidget(self.messageLayoutTitle)
    self.messageLayout.addWidget(self.messageLayoutInput)

    # Encrypt Button
    
    # Button Layout
    self.buttonLayout = QtWidgets.QVBoxLayout()
    self.buttonLayout.setDirection(QBoxLayout.Direction.LeftToRight)

    # Encrypt Button
    self.buttonLayoutButton = QtWidgets.QPushButton("Encrypt!")

    # Add to button layout
    self.buttonLayout.addWidget(self.buttonLayoutButton)

    # Add all layouts to main window
    self.encryptLayout.addLayout(self.recipientLayout)
    self.encryptLayout.addLayout(self.messageLayout)
    self.encryptLayout.addLayout(self.buttonLayout)

class Decrypt(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    # Main Box
    self.decryptLayout = QtWidgets.QVBoxLayout(self)

    # Main Box Children
    
    # User chooses recipient
    self.recipientLayout = QtWidgets.QVBoxLayout()
    self.recipientLayout.setDirection(QBoxLayout.Direction.LeftToRight) 

    # Recipient title
    self.recipientLayoutTitle = QtWidgets.QLabel("Private key")
    self.recipientLayoutTitle.setMaximumWidth(400)
    
    # Recipient Input
    self.recipientLayoutInput = QtWidgets.QTextEdit()
    self.recipientLayoutInput.setMaximumWidth(400)
    self.recipientLayoutInput.setMaximumHeight(30)

    # Add widgets for recipient layout
    self.recipientLayout.addWidget(self.recipientLayoutTitle)
    self.recipientLayout.addWidget(self.recipientLayoutInput)

    # Message Input
    self.messageLayout = QtWidgets.QVBoxLayout()
    self.messageLayout.setDirection(QBoxLayout.Direction.LeftToRight)

    # Message Title
    self.messageLayoutTitle = QtWidgets.QLabel("Message")
    self.messageLayoutTitle.setMaximumWidth(400)

    # Message Input
    self.messageLayoutInput = QtWidgets.QTextEdit()
    self.messageLayoutInput.setMaximumWidth(400)
    self.messageLayoutInput.setMaximumHeight(300)

    # Add widgets to the message layout
    self.messageLayout.addWidget(self.messageLayoutTitle)
    self.messageLayout.addWidget(self.messageLayoutInput)

    # Decrypt Button
    
    # Button Layout
    self.buttonLayout = QtWidgets.QVBoxLayout()
    self.buttonLayout.setDirection(QBoxLayout.Direction.LeftToRight)

    # Decrypt Button
    self.buttonLayoutButton = QtWidgets.QPushButton("Decrypt!")

    # Add to button layout
    self.buttonLayout.addWidget(self.buttonLayoutButton)

    # Add all layouts to main window
    self.decryptLayout.addLayout(self.recipientLayout)
    self.decryptLayout.addLayout(self.messageLayout)
    self.decryptLayout.addLayout(self.buttonLayout)

if __name__ == '__main__':
  print("Generating GUI")

  app = QtWidgets.QApplication([])

  widgets = QtWidgets.QStackedWidget()

  # Add each page
  login = widgets.addWidget(Login())
  encrypt = widgets.addWidget(Encrypt())
  decrypt = widgets.addWidget(Decrypt())

  widgets.resize(800,600)
  widgets.show()

  (widgets.setCurrentIndex(decrypt))

  sys.exit(app.exec())