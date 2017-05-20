# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auto_Test.ui'
#
# Created: Tue Jan 17 13:52:15 2017
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt4 import QtCore, QtGui

import Main

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):  #####
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(902, 821)
        Form.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 841, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_reboot = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_reboot.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_reboot.setFont(font)
        self.checkBox_reboot.setObjectName(_fromUtf8("checkBox_reboot"))
        self.horizontalLayout.addWidget(self.checkBox_reboot)
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit_reboot = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_reboot.setMaximumSize(QtCore.QSize(50, 30))
        self.textEdit_reboot.setObjectName(_fromUtf8("textEdit_reboot"))
        self.horizontalLayout.addWidget(self.textEdit_reboot)
        spacerItem1 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 911, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 911, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 881, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wide Latin"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMargin(2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(560, 770, 321, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_run = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.horizontalLayout_3.addWidget(self.pushButton_run)
        self.pushButton_cancel = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Auto Test 1-1-2017", None))
        self.checkBox_reboot.setText(_translate("Form", "Reboot Test", None))
        self.label.setText(_translate("Form", "Cycles Number", None))
        self.label_2.setText(_translate("Form", "Auto Test 2017", None))
        self.pushButton_run.setText(_translate("Form", "Run", None))
        self.pushButton_cancel.setText(_translate("Form", "Cancel", None))

        ##### coding for buttons

        self.pushButton_run.clicked.connect(self.run_chosen)
        self.pushButton_cancel.clicked.connect(self.cancel_chosen)
        ##### functions for buttons

    def run_chosen(self):
        Device = Main.device_info(ex)
        print Device

    def cancel_chosen(self):
        sys.exit(app.exec_())


### coding
if __name__ == '__main__':  ######
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()

    ex.show()
    sys.exit(app.exec_())
