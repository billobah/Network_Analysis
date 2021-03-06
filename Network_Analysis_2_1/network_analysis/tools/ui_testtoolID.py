from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogtesttoolID(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 250)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 195, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 25, 141, 22))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 27, 121, 20))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox2 = QtWidgets.QComboBox(Dialog)
        self.comboBox2.setGeometry(QtCore.QRect(150, 85, 141, 22))
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(30, 87, 121, 20))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.comboBox3 = QtWidgets.QComboBox(Dialog)
        self.comboBox3.setGeometry(QtCore.QRect(150, 145, 141, 22))
        self.comboBox3.setFont(font)
        self.comboBox3.setObjectName("comboBox3")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(30, 147, 121, 20))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Nodes ID", None))
        self.label2.setText(QtWidgets.QApplication.translate("Dialog", "Edges Start ID", None))
        self.label3.setText(QtWidgets.QApplication.translate("Dialog", "Edges End ID", None))
