import sys
from PyQt5.QtWidgets import *
import check
import fetch

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "AI"
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(150, 150, 800, 600)

        b = QPushButton("Check",self)
        c = QPushButton("Fetch",self)
        b.resize(b.sizeHint())
        c.resize(c.sizeHint())
        b.clicked.connect(self.on_click1)
        c.clicked.connect(self.on_click2)

        layout = QVBoxLayout()
        layout.addWidget(b)
        layout.addWidget(c)

        self.setLayout(layout)
        self.show()

    def on_click1(self):
        self.temp = check.App1()

    def on_click2(self):
        self.temp2 = fetch.App2()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
