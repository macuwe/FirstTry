#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn3 = QtGui.QPushButton("Button 3", self)
        btn3.move(90, 90)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))        
        self.statusBar().showMessage('Ready')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        if sender.text() == 'Button 1':
            self.move(10, 10)
        elif sender.text() == 'Button 2':
            self.move(90, 90)
        else:
            self.move(170, 170)
        self.statusBar().showMessage(sender.text() + ' was pressed')


def getLink():
    print 'dada#'

        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    getLink()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()