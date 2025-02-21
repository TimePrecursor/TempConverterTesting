from time import sleep
from typing import Any
from typing import Any

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime as dt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 100, 100)

        # calling methods
        self.UiComponents()
        self.mainWindowSetup()

        # showing all the widgets
        self.show()

    def mainWindowSetup(self):
        self.setFixedSize(500, 300)
        self.setWindowTitle("Temperature Converter (TESTING)")

    def loginstuff2(self):
        usern = self.userin.text()
        with open("Logins2.txt") as file:
            lines = file.readlines()
            print(usern)
            for pos, line in enumerate(lines):
                x = line.split("|")
                print(x)
                print(x[2])
                print(pos)
                passinput = self.passin.text()
                print(passinput)
                if x[2] == usern:
                    import PasswordCheck as ft
                    bool1 = ft.functionclass.passwordstep(self,pos,passinput)
                    if bool1 == True:
                        print("TRUE")
                    else:
                        print("FALSE")
                    break
                else:
                    print("No match found!")

    # OLD
    # def loginstuff(self):
    #     usern = self.userin.text()
    #     with open("Logins2.txt") as file:
    #         lines = file.readlines()
    #         print(usern)
    #         for line in lines:
    #             if line.find(usern) != -1:
    #                 print("Lmao")
    #                 break
    #             else:
    #                 print("nope")

    # method for widgets
    def UiComponents(self):
        self.userlabel = QLabel(self)
        self.passlabel = QLabel(self)
        self.userin = QLineEdit(self)
        self.passin = QLineEdit(self)
        self.pushb1 = QPushButton(self)

        self.userlabel.setText("Enter Username:")
        self.userlabel.setGeometry(10,10,100,20)
        self.passlabel.setText("Enter Password:")
        self.passlabel.setGeometry(10, 50, 100, 20)
        self.userin.setGeometry(100,10,100,20)
        self.pushb1.setText("Login as")
        self.pushb1.setGeometry(50, 100, 150, 50)
        self.pushb1.clicked.connect(self.loginstuff2)
        self.passin.setGeometry(100,50,100,20)
        self.passin.setEchoMode(QLineEdit.Password)





        # connect the button click to a function

        # # creating a push button
        # button = QPushButton("CLICK", self)
        # # setting geometry of button
        # button.setGeometry(200, 150, 100, 30)
        # # adding action to a button
        # button.clicked.connect(self.clickme)


    # def btnstate(self):
    #     print("button released")
    # # action method (OLD)
    # def clickme(self):
    #     # printing pressed
    #     print("pressed")

class Logininfo:
  def __init__(self, f_name1, l_name1, user1, pass1):
    self.f_name1 = f_name1
    self.l_name1 = l_name1
    self.user1 = user1
    self.pass1 = pass1

  def __str__(self):
    return f"({self.f_name1}|{self.l_name1}|{self.user1}|{self.pass1})"

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


# just incase:
# www.geeksforgeeks.org/pyqt5-how-to-add-action-to-a-button/