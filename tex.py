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
        self.resize(1980,1080)
        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.setPlainText("".join([i + str('\n') for i in y.split('(end)')]))
        self.b.setReadOnly(True)
        #self.b.move(10,10)
        self.b.resize(1980, 1080)
        self.show()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow('add','sdsd')
    sys.exit( app.exec_() )'''