import sys
import time
import os
from PyQt5.QtWidgets import QLabel,QLineEdit, QApplication,QPushButton, QWidget, QMainWindow, QTextEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5 import QtGui

# Function to help access files and folders both within and outside the exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Window coordinates and dimensions
X = 300
Y = 100
WIDTH = 327
HEIGHT = 580

class FirstWindow(QWidget):
	switch_to_second = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.createUI()


	# Called when proceed is clicked
	def on_proceed_click(self):
		self.switch_to_second.emit()
		self.close()


	# Function to create widgets
	def createUI(self):
		self.setGeometry(X,Y,WIDTH,HEIGHT)
		self.setWindowTitle("Welcome")

		self.setStyleSheet("background-color:white")

		self.background_label = QLabel(self)
		self.background_label.setPixmap(QtGui.QPixmap(resource_path("background.jpeg")).scaledToWidth(327))
		self.background_label.resize(327,580)
		#self.background_label.move(260,10)

		self.proceed_button = QPushButton(self)
		self.proceed_button.setText("Proceed")
		self.proceed_button.resize(120,40)
		self.proceed_button.move(100,450)
		self.proceed_button.clicked.connect(self.on_proceed_click)
		self.proceed_button.setStyleSheet("background-color:darkgreen; color:white; border-radius:15px; font-size:10pt")

		self.name_label = QLabel(self)
		self.name_label.setText("By Jahan")
		self.name_label.move(240,545)
		self.name_label.setStyleSheet("background-color:None;color: white; font-family: Bahnschrift SemiBold; font-size:12pt")


class SecondWindow(QWidget):
	switch_to_third = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.createUI()

	# Functions that displays output
	def display_text(self,text):
		text = ">> " + text
		self.output_text.append(text)

	# Function called when run is clicked
	def on_run_click(self):
		decks = self.deck_entry.text()
		if not decks:
			messagebox = QMessageBox(self)
			messagebox.setIcon(QMessageBox.Information)
			messagebox.setText("Please enter the number of decks      ")
			messagebox.setWindowTitle("Empty value")
			messagebox.show()
			return

		try:

			n = float(self.deck_entry.text())
			truecount = n/controller.ct
			print("truecount =",truecount)
			self.display_text("Truecount = "+ str(truecount))
			if truecount > 0.6:
				print("good count")
				self.display_text("Good count")
			else: 
				print("bad count")
				self.display_text("Bad count")

			self.deck_entry.clear()
			controller.ct = 0

		except Exception as e:
			messagebox = QMessageBox(self)
			messagebox.setIcon(QMessageBox.Information)
			messagebox.setText(str(e))
			messagebox.setWindowTitle("Exception occured")
			messagebox.show()
			self.deck_entry.clear()
			return

	# Function called when next is clicked
	def on_next_click(self):
		card = self.card_entry.text()
		if not card:
			messagebox = QMessageBox(self)
			messagebox.setIcon(QMessageBox.Information)
			messagebox.setText("Please enter a card      ")
			messagebox.setWindowTitle("Empty value")
			messagebox.show()
			return

		try:

			c = int(card)


			if  c > 0 and c < 7:
				controller.ct = controller.ct + 1
				print (controller.ct)
				print ("Low card")

				self.display_text(str(controller.ct))
				self.display_text("Low Card")

			elif c >= 7 and c < 10:
				controller.ct = controller.ct + 0
				print(controller.ct)
				print("Neutral card")

				self.display_text(str(controller.ct))
				self.display_text("Neutral Card")

			elif c >= 10 and c < 12:
				controller.ct = controller.ct - 1
				print (controller.ct)
				print("High card")

				self.display_text(str(controller.ct))
				self.display_text("High Card")

			self.card_entry.clear()

		except Exception as e:
			messagebox = QMessageBox(self)
			messagebox.setIcon(QMessageBox.Information)
			messagebox.setText(str(e))
			messagebox.setWindowTitle("Exception occured")
			messagebox.show()
			self.card_entry.clear()
			return


	# Function to create widgets
	def createUI(self):
		self.setGeometry(X,Y,WIDTH,HEIGHT)
		self.setWindowTitle("Cards")
		self.setFocus(Qt.NoFocusReason)
		self.setStyleSheet("background-color:#2E4C6D")

		self.card_label = QLabel(self)
		self.card_label.setText("Enter a card :")
		self.card_label.move(52,50)
		self.card_label.setStyleSheet("color: rgb(220,220,220); font-family: Bahnschrift SemiBold; font-size:11.5pt")

		self.card_entry = QLineEdit(self)
		self.card_entry.resize(250,40)
		self.card_entry.move(38,75)
		self.card_entry.setStyleSheet("background-color: white; font-size:11pt; padding-left: 15px;border-radius:15px")
		self.card_entry.setPlaceholderText("Enter a card")
		self.card_entry.returnPressed.connect(self.on_next_click)

		self.next_button = QPushButton(self)
		self.next_button.setText("Next")
		self.next_button.resize(110,30)
		self.next_button.move(105,135)
		self.next_button.clicked.connect(self.on_next_click)
		self.next_button.setStyleSheet("background-color:darkgreen; color:white; border-radius:12px; font-size:10pt")

		self.deck_label = QLabel(self)
		self.deck_label.setText("Enter number of decks :")
		self.deck_label.move(52,180)
		self.deck_label.setStyleSheet("color: rgb(220,220,220); font-family: Bahnschrift SemiBold; font-size:11.5pt")

		self.deck_entry = QLineEdit(self)
		self.deck_entry.resize(250,40)
		self.deck_entry.move(38,205)
		self.deck_entry.setStyleSheet("background-color: white; font-size:11pt; padding-left: 15px;border-radius:15px")
		self.deck_entry.setPlaceholderText("Enter number of decks")
		self.deck_entry.returnPressed.connect(self.on_run_click)

		self.run_button = QPushButton(self)
		self.run_button.setText("Run")
		self.run_button.resize(110,30)
		self.run_button.move(105,270)
		self.run_button.clicked.connect(self.on_run_click)
		self.run_button.setStyleSheet("background-color:darkgreen; color:white; border-radius:12px; font-size:10pt")

		self.output_text = QTextEdit(self)
		self.output_text.resize(250,200)
		self.output_text.move(38,325)
		self.output_text.setStyleSheet("background-color: black; font-size:10pt; padding-left: 4px;border-radius:12px; color:rgb(20,200,20); font-family:consolas")

		self.name_label = QLabel(self)
		self.name_label.setText("By Jahan")
		self.name_label.move(240,545)
		self.name_label.setStyleSheet("background-color:None;color: rgb(200,200,200); font-family: Bahnschrift SemiBold; font-size:12pt")


# Class to handle switching between windows 
class Controller():

	ct = 0

	def show_first(self):
		self.first_screen = FirstWindow()
		self.first_screen.switch_to_second.connect(self.show_second)
		self.first_screen.show()

	def show_second(self):
		self.second_screen = SecondWindow()
		self.second_screen.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	controller = Controller()
	controller.show_first()
	sys.exit(app.exec_())