import sys
from PyQt5.QtWidgets import *
from twitter import search
import tex
import speech
import table

class App2(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 800, 600)

        self.btn = QPushButton("Enter",self)
        self.vbtn = QPushButton("Voice", self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter the keywords seperated by space") 
        self.btn.clicked.connect(self.on_click)
        self.vbtn.clicked.connect(self.voice)

        hl = QHBoxLayout()
        hl.addWidget(self.textbox)
        hl.addWidget(self.vbtn)

        layout = QVBoxLayout()
        layout.addLayout(hl)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()

    def on_click(self):
        #self.m = str(search(self.textbox.text()))
        #self.temp = tex.ExampleWindow("Tweets related to %s" % self.textbox.text(), self.m)
        self.temp = table.App("Tweets related to %s" % self.textbox.text(), self.textbox.text())

    def voice(self):
        self.textbox.setText(speech.lis())

def fetch():
    app2 = QApplication(sys.argv)
    ex2 = App2()
    sys.exit(app2.exec_())

fetch()