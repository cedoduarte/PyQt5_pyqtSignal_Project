from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class Dialog(QDialog):
	listWidgetTieneMultiploDe5 = pyqtSignal(int, int)

	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("dialog.ui", self)

		self.agregarButton.clicked.connect(self.onAgregarButtonClicked)
		self.listWidgetTieneMultiploDe5.connect(self.onListWidgetTieneMultiploDe5)

	def onAgregarButtonClicked(self):
		self.listWidget.addItem("Hola, mundo")
		if self.listWidget.count() % 5 == 0:
			self.listWidgetTieneMultiploDe5.emit(5, self.listWidget.count())

	def onListWidgetTieneMultiploDe5(self, a, b):
		QMessageBox.information(self, "OK", str(a) + " " + str(b))