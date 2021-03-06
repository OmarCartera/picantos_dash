#/******************************
# *     Author: Omar Gamal     *
# *   c.omargamal@gmail.com    *
# *                            *
# *   Language: Python 2.7     *
# *                            *
# *         15/1/2018          *
# *                            *
# *      TCP Multi-Client      *
# *      Chat Application      *
# ******************************/

#!/usr/bin/env python
###########################################
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import loadUiType

# import design.py for GUI things
import design
import second

import sys

# to open files and sleep()
import os
import time

import serial
import io

# used in USB Ports detection
import glob


# progress bar GUI thread
class progress_bar_thread(QtCore.QThread):
	def __init__(self):
		super(progress_bar_thread, self).__init__()

	# call the function that updates the bar from the secondary thread
	def run(self):
		while 1:
			self.emit(SIGNAL('update_progress_bar()'))
			time.sleep(0.2)


class Second(QtGui.QMainWindow, second.Ui_MainWindow):
	def __init__(self):
		super(Second, self).__init__()
		self.setupUi(self)

		self.btn_connect.clicked.connect(self.btn_connect_fn)
		self.btn_refresh.clicked.connect(self.serial_ports_fn)

		self.serial_ports_fn()

	def btn_connect_fn(self):
		self.hide()
		self.dialog = mainApp(int(self.combo_baud.currentText()), str(self.combo_ports.currentText()))
		self.dialog.show()


	# check the available serial ports. Cross platform
	def serial_ports_fn(self):
		# initialize variable
		result = []

		# works only if serial is disconnected. because it shuts off ports
		# while testing their availability
		# if we running on windows
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]

		# if we are running linux
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = glob.glob('/dev/tty[A-Za-z]*')

		# if we are running darwin
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')

		# if any other OS
		else:
			raise EnvironmentError('Unsupported platform')

		# test every port in the system
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)

			except (OSError, serial.SerialException):
				pass


		# put the ports names in the ports drop list
		self.combo_ports.clear()
		self.combo_ports.addItems(result)

		if result == []:
			self.btn_connect.setEnabled(False)

		else:
			self.btn_connect.setEnabled(True)



# main GUI class
class mainApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self,  baud, port):
		super(mainApp, self).__init__()
		self.setupUi(self)

		# GUI thread things
		self.progress_bar_thread = progress_bar_thread()
		self.connect(self.progress_bar_thread, SIGNAL('update_progress_bar()'), self.update_progress_bar)

		self.action9600.triggered.connect(self.baud_9600)
		self.action115200.triggered.connect(self.baud_115200)

		self.connect_serial(port, baud)

		
		# ser.close()             # close port


	def update_progress_bar(self):
		if self.ser.inWaiting() > 0:
			self.ser.flushInput()

		x = int(self.ser.readline())
		self.bar_rpm.setValue(x)
		self.lcd_speed.display(x)


	def baud_9600(self):
		self.connect_serial(9600)


	def baud_115200(self):
		self.connect_serial(115200)



	def connect_serial(self, port, baud):
		self.ser = serial.Serial(port, baud)
		print(self.ser.name)

		self.progress_bar_thread.start()



def main():
	App = QtGui.QApplication(sys.argv)
	form = Second()
	form.show()
	App.exec_()


if __name__ == '__main__':
	main()
