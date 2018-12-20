# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fortune.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Fortunes(object):
    def setupUi(self, Fortunes):
        Fortunes.setObjectName("Fortunes")
        Fortunes.resize(532, 336)
        Fortunes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(12)
        Fortunes.setFont(font)
        Fortunes.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fortunes.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Fortunes)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 491, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 471, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(19, 240, 491, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(20, 5, 451, 31))
        self.toolButton.setObjectName("toolButton")
        Fortunes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fortunes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 24))
        self.menubar.setObjectName("menubar")
        Fortunes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fortunes)
        self.statusbar.setObjectName("statusbar")
        Fortunes.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Fortunes)
        self.actionAbout.setObjectName("actionAbout")
        self.actionWhat_is_the_point = QtWidgets.QAction(Fortunes)
        self.actionWhat_is_the_point.setObjectName("actionWhat_is_the_point")

        self.toolButton.clicked.connect(self.get_fortune)

        self.retranslateUi(Fortunes)
        QtCore.QMetaObject.connectSlotsByName(Fortunes)

    def get_fortune(self):

        fortunezz = os.system("fortune")

        fortunez = str(fortunezz)

        self.plainTextEdit.insertPlainText(fortunez)

    def retranslateUi(self, Fortunes):
        _translate = QtCore.QCoreApplication.translate
        Fortunes.setWindowTitle(_translate("Fortunes", "Know your fortune today!"))
        Fortunes.setStatusTip(_translate("Fortunes", "Whatever fortune(s) you get... It\'s probably real!"))
        self.label.setText(_translate("Fortunes", "Fortune"))
        self.toolButton.setToolTip(_translate("Fortunes", "Push if you dare!"))
        self.toolButton.setStatusTip(_translate("Fortunes", "Get your fortune!"))
        self.toolButton.setText(_translate("Fortunes", "...forTune..."))
        self.actionAbout.setText(_translate("Fortunes", "About"))
        self.actionWhat_is_the_point.setText(_translate("Fortunes", "FAQ"))

