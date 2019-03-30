import sys
from PyQt5.QtWidgets import *
import speech
from load import predict

class App1(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 800, 600)

        self.btn = QPushButton("Enter",self)
        self.vbtn = QPushButton("Voice",self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter a tweet") 
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
        QMessageBox.about(self, "AI", str(predict(self.textbox.text())))

    def voice(self):
        self.textbox.setText(speech.lis())
        
def check():
    app1 = QApplication(sys.argv)
    ex1 = App1()
    sys.exit(app1.exec_())

check()