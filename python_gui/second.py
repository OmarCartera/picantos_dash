# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
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
        MainWindow.resize(300, 312)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("egg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.combo_ports = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_ports.sizePolicy().hasHeightForWidth())
        self.combo_ports.setSizePolicy(sizePolicy)
        self.combo_ports.setObjectName(_fromUtf8("combo_ports"))
        self.gridLayout_2.addWidget(self.combo_ports, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.btn_refresh = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.gridLayout_2.addWidget(self.btn_refresh, 3, 3, 1, 1, QtCore.Qt.AlignRight)
        self.btn_connect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.gridLayout_2.addWidget(self.btn_connect, 7, 1, 1, 3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 6, 1, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 2, 1, 1)
        self.combo_baud = QtGui.QComboBox(self.centralwidget)
        self.combo_baud.setObjectName(_fromUtf8("combo_baud"))
        self.combo_baud.addItem(_fromUtf8(""))
        self.combo_baud.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_baud, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
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

        self.retranslateUi(MainWindow)
        self.combo_baud.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OBD Dash | Settings", None))
        self.label.setText(_translate("MainWindow", "Baud Rate:", None))
        self.label_2.setText(_translate("MainWindow", "Comm Port:", None))
        self.btn_refresh.setText(_translate("MainWindow", "⟳", None))
        self.btn_connect.setText(_translate("MainWindow", "Connect", None))
        self.combo_baud.setItemText(0, _translate("MainWindow", "9600", None))
        self.combo_baud.setItemText(1, _translate("MainWindow", "115200", None))
        self.action9600.setText(_translate("MainWindow", "9600", None))
        self.action115200.setText(_translate("MainWindow", "115200", None))
        self.action11.setText(_translate("MainWindow", "11", None))
        self.actionPort_2.setText(_translate("MainWindow", "Port", None))

