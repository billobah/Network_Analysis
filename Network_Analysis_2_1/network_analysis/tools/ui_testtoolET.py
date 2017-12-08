from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogtesttoolET(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 310)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 260, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 141, 22))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 32, 121, 20))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox2 = QtWidgets.QComboBox(Dialog)
        self.comboBox2.setGeometry(QtCore.QRect(150, 90, 141, 22))
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(30, 92, 121, 20))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.comboBox3 = QtWidgets.QComboBox(Dialog)
        self.comboBox3.setGeometry(QtCore.QRect(150, 150, 141, 22))
        self.comboBox3.setFont(font)
        self.comboBox3.setObjectName("comboBox3")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(30, 152, 121, 20))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.comboBox4 = QtWidgets.QComboBox(Dialog)
        self.comboBox4.setGeometry(QtCore.QRect(150, 210, 141, 22))
        self.comboBox4.setFont(font)
        self.comboBox4.setObjectName("comboBox4")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(30, 212, 121, 20))
        self.label4.setFont(font)
        self.label4.setObjectName("label4")

        self.comboBoxb = QtWidgets.QComboBox(Dialog)
        self.comboBoxb.setGeometry(QtCore.QRect(450, 30, 141, 22))
        self.comboBoxb.setFont(font)
        self.comboBoxb.setObjectName("comboBoxb")
        self.labelb = QtWidgets.QLabel(Dialog)
        self.labelb.setGeometry(QtCore.QRect(330, 32, 121, 20))
        self.labelb.setFont(font)
        self.labelb.setObjectName("labelb")
        self.comboBox2b = QtWidgets.QComboBox(Dialog)
        self.comboBox2b.setGeometry(QtCore.QRect(450, 90, 141, 22))
        self.comboBox2b.setFont(font)
        self.comboBox2b.setObjectName("comboBox2b")
        self.label2b = QtWidgets.QLabel(Dialog)
        self.label2b.setGeometry(QtCore.QRect(330, 92, 121, 20))
        self.label2b.setFont(font)
        self.label2b.setObjectName("label2b")
        self.comboBox3b = QtWidgets.QComboBox(Dialog)
        self.comboBox3b.setGeometry(QtCore.QRect(450, 150, 141, 22))
        self.comboBox3b.setFont(font)
        self.comboBox3b.setObjectName("comboBox3b")
        self.label3b = QtWidgets.QLabel(Dialog)
        self.label3b.setGeometry(QtCore.QRect(330, 152, 121, 20))
        self.label3b.setFont(font)
        self.label3b.setObjectName("label3b")
        self.comboBox4b = QtWidgets.QComboBox(Dialog)
        self.comboBox4b.setGeometry(QtCore.QRect(450, 210, 141, 22))
        self.comboBox4b.setFont(font)
        self.comboBox4b.setObjectName("comboBox4b")
        self.label4b = QtWidgets.QLabel(Dialog)
        self.label4b.setGeometry(QtCore.QRect(330, 212, 121, 20))
        self.label4b.setFont(font)
        self.label4b.setObjectName("label4b")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Street 1 (option)", None))
        self.label2.setText(QtWidgets.QApplication.translate("Dialog", "Postal Code 1 (option)", None))
        self.label3.setText(QtWidgets.QApplication.translate("Dialog", "Name 1 ", None))
        self.label4.setText(QtWidgets.QApplication.translate("Dialog", "Country 1 (option)", None))
        self.labelb.setText(QtWidgets.QApplication.translate("Dialog", "Street 2 (option)", None))
        self.label2b.setText(QtWidgets.QApplication.translate("Dialog", "Postal Code 2 (option)", None))
        self.label3b.setText(QtWidgets.QApplication.translate("Dialog", "Name 2 ", None))
        self.label4b.setText(QtWidgets.QApplication.translate("Dialog", "Country 2 (option)", None))
