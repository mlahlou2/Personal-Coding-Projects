#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:48:48 2018

@author: soundpipe
"""

import sys
from PyQt4 import QtGui

Class Window(QtGui.QMainWindow)

class Button(QtGui.QPushButton):
  
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        self.setText(e.mimeData().text()) 


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)
        
        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)


def main():
  
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    window.setGeometry(50,50, 500,300)
    window.setWindowTitle("Google Scheduler Pusher")
    
    window.show()
    app.exec_()  
  

if __name__ == '__main__':
    main() 