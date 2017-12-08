from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(472, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog2)
        self.buttonBox.setGeometry(QtCore.QRect(110, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog2)
        self.comboBox.setGeometry(QtCore.QRect(110, 20, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(20, 18, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(20, 28, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(260, 18, 81, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 20, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(260, 28, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog2)
        self.label_5.setGeometry(QtCore.QRect(20, 83, 101, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 80, 51, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 140, 51, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_6 = QtWidgets.QLabel(Dialog2)
        self.label_6.setGeometry(QtCore.QRect(20, 143, 101, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_5.setGeometry(QtCore.QRect(350, 140, 101, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_7 = QtWidgets.QLabel(Dialog2)
        self.label_7.setGeometry(QtCore.QRect(220, 143, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog2)
        self.label_8.setGeometry(QtCore.QRect(20, 203, 121, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_6.setGeometry(QtCore.QRect(90, 200, 171, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(Dialog2)
        self.comboBox_7.setGeometry(QtCore.QRect(400, 200, 51, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_9 = QtWidgets.QLabel(Dialog2)
        self.label_9.setGeometry(QtCore.QRect(305, 203, 91, 16))
        self.label_9.setObjectName("label_9")

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
        self.label_8.setText(QtWidgets.QApplication.translate("Dialog2", "Indices", None))
        self.label_9.setText(QtWidgets.QApplication.translate("Dialog2", "Normalization ?", None))

