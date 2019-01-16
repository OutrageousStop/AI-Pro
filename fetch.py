import sys
from PyQt5.QtWidgets import *
from twitter import search
import tex

class App2(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 800, 600)

        self.btn = QPushButton("Enter",self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter the keywords seperated by space") 
        self.btn.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()

    def on_click(self):
        self.m = str(search(self.textbox.text()))
    #    self.temp = tex.ExampleWindow("Tweets related to {}".format(self.textbox.text()),self.m)
        self.temp = tex.ExampleWindow("tweets related to %s" % self.textbox.text(), self.m)

# def fetch():
#     app2 = QApplication(sys.argv)
#     ex2 = App2()
#     sys.exit(app2.exec_())
