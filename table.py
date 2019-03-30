import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from load import predict
from tex import cs
import pandas as pd
 
class App(QWidget):
 
    def __init__(self, x, y):
        super().__init__()
        self.title = x
        self.left = 0
        self.top = 0
        self.width = 1980
        self.height = 1080
        self.initUI(y)
 
    def initUI(self, y):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable(y)
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self, y):

        cs(y)
        df = pd.read_csv("tweets.csv")
        a=[]
        for i in range(len(df)):
            a.append(str(df.iloc[i]))

       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(2)

        for i in range(df.shape[0]):
            self.tableWidget.setItem(i,0, QTableWidgetItem(a[i]))
        for i in range(df.shape[0]):
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(predict(a[i]))))
        self.tableWidget.move(0,0)
        self.tableWidget.resizeColumnsToContents()
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = input("Enter the keywords: ")
    ex = App(x, x)
    sys.exit(app.exec_())