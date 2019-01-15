import sys
from PyQt5.QtWidgets import *

class App1(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 800, 600)

        self.btn = QPushButton("Enter",self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter a tweet") 
        self.btn.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()

    def on_click(self):
        QMessageBox.about(self, "AI", "This tweet is ...")
        
def check():
    app1 = QApplication(sys.argv)
    ex1 = App1()
    sys.exit(app1.exec_())