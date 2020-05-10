# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 494)
        self.ipAddress = QtWidgets.QLineEdit(Form)
        self.ipAddress.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.ipAddress.setObjectName("ipAddress")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.port.setObjectName("port")
        self.textFromClient = QtWidgets.QTextBrowser(Form)
        self.textFromClient.setGeometry(QtCore.QRect(380, 20, 256, 421))
        self.textFromClient.setObjectName("textFromClient")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 331, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 54, 12))
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(50, 100, 113, 20))
        self.name.setObjectName("name")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 54, 12))
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 54, 12))
        self.label_5.setObjectName("label_5")
        self.plainText = QtWidgets.QLineEdit(Form)
        self.plainText.setGeometry(QtCore.QRect(50, 150, 301, 20))
        self.plainText.setObjectName("plainText")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 54, 12))
        self.label_6.setObjectName("label_6")
        self.cipherText = QtWidgets.QLineEdit(Form)
        self.cipherText.setGeometry(QtCore.QRect(50, 200, 301, 20))
        self.cipherText.setObjectName("cipherText")
        self.buttonEncode = QtWidgets.QPushButton(Form)
        self.buttonEncode.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.buttonEncode.setObjectName("buttonEncode")
        self.buttonDecode = QtWidgets.QPushButton(Form)
        self.buttonDecode.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.buttonDecode.setObjectName("buttonDecode")
        self.buttonClear = QtWidgets.QPushButton(Form)
        self.buttonClear.setGeometry(QtCore.QRect(250, 240, 75, 23))
        self.buttonClear.setObjectName("buttonClear")
        self.textCodec = QtWidgets.QTextEdit(Form)
        self.textCodec.setGeometry(QtCore.QRect(20, 280, 331, 151))
        self.textCodec.setObjectName("textCodec")
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.sendButton.setObjectName("sendButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "服务器"))
        self.label.setText(_translate("Form", "ip地址"))
        self.label_2.setText(_translate("Form", "端口"))
        self.pushButton.setText(_translate("Form", "建立服务器"))
        self.label_3.setText(_translate("Form", "昵称"))
        self.label_4.setText(_translate("Form", "秘钥"))
        self.label_5.setText(_translate("Form", "明文"))
        self.label_6.setText(_translate("Form", "密文"))
        self.buttonEncode.setText(_translate("Form", "加密"))
        self.buttonDecode.setText(_translate("Form", "解密"))
        self.buttonClear.setText(_translate("Form", "清除"))
        self.sendButton.setText(_translate("Form", "发送"))
