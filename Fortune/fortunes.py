from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(ApplicationWindow, self).__init__()

        from design import Ui_Fortunes

        self.ui = Ui_Fortunes()
        self.ui.setupUi(self)


def main():

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.setWindowTitle('Know your fortune!')
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()