# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Ui_Dialogstat2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 250)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        Dialog.setFont(font)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 200, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 32, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox2 = QtGui.QComboBox(Dialog)
        self.comboBox2.setGeometry(QtCore.QRect(150, 90, 141, 22))
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(30, 92, 121, 20))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.comboBox3 = QtGui.QComboBox(Dialog)
        self.comboBox3.setGeometry(QtCore.QRect(130, 150, 161, 22))
        self.comboBox3.setFont(font)
        self.comboBox3.setObjectName("comboBox3")
        self.label3 = QtGui.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(30, 152, 91, 20))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Field 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "Field 2 (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Dialog", "Statistic tool", None, QtGui.QApplication.UnicodeUTF8))

