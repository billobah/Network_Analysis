from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_testDialogtoollc(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(545, 240)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog2)
        self.buttonBox.setGeometry(QtCore.QRect(180, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog2)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 101, 24))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(20, 16, 81, 20))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(20, 28, 81, 20))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(300, 16, 101, 20))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 20, 101, 24))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(300, 28, 101, 20))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog2)
        self.label_5.setGeometry(QtCore.QRect(20, 83, 131, 20))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 80, 61, 24))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 140, 61, 24))
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_6 = QtWidgets.QLabel(Dialog2)
        self.label_6.setGeometry(QtCore.QRect(20, 143, 131, 20))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_5.setGeometry(QtCore.QRect(420, 140, 101, 24))
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_7 = QtWidgets.QLabel(Dialog2)
        self.label_7.setGeometry(QtCore.QRect(260, 143, 151, 20))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog2)
        self.buttonBox.rejected.connect(Dialog2.reject)
        self.buttonBox.accepted.connect(Dialog2.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QtWidgets.QApplication.translate("Dialog2", "Dialog", None))
        self.label.setText(QtWidgets.QApplication.translate("Dialog2", "Start nodes", None))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog2", "field", None))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog2", "End nodes", None))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog2", "field", None))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog2", "Directed network ?", None))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog2", "Weighted network ?", None))
        self.label_7.setText(QtWidgets.QApplication.translate("Dialog2", "Weight field (optional)", None))
