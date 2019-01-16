import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self,x,y):
        QMainWindow.__init__(self)

        #self.setMinimumSize(QSize(440, 240))    
        self.setWindowTitle(x) 

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.setPlainText(y)
        self.b.setReadOnly(True)
        #self.b.move(10,10)
        #self.b.resize(400,200)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow('add','sdsd')
    sys.exit( app.exec_() )