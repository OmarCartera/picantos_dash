# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(330, 274)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("egg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcd_speed = QtGui.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lcd_speed.setFont(font)
        self.lcd_speed.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_speed.setFrameShadow(QtGui.QFrame.Plain)
        self.lcd_speed.setSmallDecimalPoint(True)
        self.lcd_speed.setDigitCount(3)
        self.lcd_speed.setMode(QtGui.QLCDNumber.Dec)
        self.lcd_speed.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_speed.setProperty("value", 200.0)
        self.lcd_speed.setProperty("intValue", 200)
        self.lcd_speed.setObjectName(_fromUtf8("lcd_speed"))
        self.gridLayout.addWidget(self.lcd_speed, 0, 0, 1, 1)
        self.bar_rpm = QtGui.QProgressBar(self.centralwidget)
        self.bar_rpm.setMaximum(5000)
        self.bar_rpm.setProperty("value", 750)
        self.bar_rpm.setObjectName(_fromUtf8("bar_rpm"))
        self.gridLayout.addWidget(self.bar_rpm, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSetup = QtGui.QMenu(self.menubar)
        self.menuSetup.setObjectName(_fromUtf8("menuSetup"))
        self.menuBaud = QtGui.QMenu(self.menuSetup)
        self.menuBaud.setObjectName(_fromUtf8("menuBaud"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action9600 = QtGui.QAction(MainWindow)
        self.action9600.setObjectName(_fromUtf8("action9600"))
        self.action115200 = QtGui.QAction(MainWindow)
        self.action115200.setObjectName(_fromUtf8("action115200"))
        self.action11 = QtGui.QAction(MainWindow)
        self.action11.setObjectName(_fromUtf8("action11"))
        self.actionPort_2 = QtGui.QAction(MainWindow)
        self.actionPort_2.setObjectName(_fromUtf8("actionPort_2"))
        self.menuBaud.addAction(self.action9600)
        self.menuBaud.addAction(self.action115200)
        self.menuSetup.addSeparator()
        self.menuSetup.addAction(self.actionPort_2)
        self.menuSetup.addAction(self.menuBaud.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OBD Dash", None))
        self.bar_rpm.setFormat(_translate("MainWindow", "%v", None))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup", None))
        self.menuBaud.setTitle(_translate("MainWindow", "Baud", None))
        self.action9600.setText(_translate("MainWindow", "9600", None))
        self.action115200.setText(_translate("MainWindow", "115200", None))
        self.action11.setText(_translate("MainWindow", "11", None))
        self.actionPort_2.setText(_translate("MainWindow", "Port", None))

