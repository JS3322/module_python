# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.seebutton = QtWidgets.QPushButton(Form)
        self.seebutton.setGeometry(QtCore.QRect(260, 30, 113, 32))
        self.seebutton.setObjectName("seebutton")
        self.deletebutton = QtWidgets.QPushButton(Form)
        self.deletebutton.setGeometry(QtCore.QRect(260, 80, 113, 32))
        self.deletebutton.setObjectName("deletebutton")
        self.cancelbutton = QtWidgets.QPushButton(Form)
        self.cancelbutton.setGeometry(QtCore.QRect(260, 130, 113, 32))
        self.cancelbutton.setObjectName("cancelbutton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 231, 271))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.seebutton.setText(_translate("Form", "see datamap"))
        self.deletebutton.setText(_translate("Form", "delete file"))
        self.cancelbutton.setText(_translate("Form", "cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
