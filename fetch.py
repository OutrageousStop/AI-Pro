import sys
from PyQt5.QtWidgets import *

class App2(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 200, 100)

        self.btn = QPushButton("Enter",self)
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter a keyword") 
        self.btn.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()

    def on_click(self):
        msg = QMessageBox.about(self, "AI", "This tweet has: <br> 20% positive feedback <br> 50% neutral feedback <br> 30% negative feedback")
        msg.show()
        
def fetch():
    app2 = QApplication(sys.argv)
    ex2 = App2()
    sys.exit(app2.exec_())