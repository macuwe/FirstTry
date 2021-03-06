#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import pycurl
import StringIO

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

    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color) #für übergang
        qp.setBrush(QtGui.QColor(200, 200, 0))
        qp.drawRect(10, 10, 20, 20)
        qp.setBrush(QtGui.QColor(20, 200, 130))
        qp.drawRect(20,20, 30, 30)
        qp.end()


    def buttonClicked(self):

        sender = self.sender()
        if sender.text() == 'Button 1':
            getContent()
            #self.move(10, 10) #move Window

        elif sender.text() == 'Button 2':
            getURL()
            self.move(90, 90)
        else:
            self.move(170, 170)
        self.statusBar().showMessage(sender.text() + ' was pressed')


def getURL():
    c = pycurl.Curl()
    URL = 'https://api.hitbox.tv'
    URL += '/chat/servers'
    c.setopt(c.URL, URL)
    info = c.getinfo(pycurl.EFFECTIVE_URL)
    print info

def getContent():
    c = pycurl.Curl()
    URL = 'https://api.hitbox.tv'
    URL += '/chat/servers'
    storage = StringIO.StringIO()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()
    print content



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()