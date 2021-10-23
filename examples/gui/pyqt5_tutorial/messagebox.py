#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program shows a confirmation 
message box when we click on the close
button of the application window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QCalendarWidget
from PyQt5.QtCore import QDate


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        cal=QCalendarWidget(self)
        cal.clicked[QDate].connect(self.showDate)

        self.msg = QMessageBox(self)
        width=450
        height=350
        self.setGeometry(500, 500, width, height)    
        cal.setGeometry(0, 0, width, height)       
        self.setWindowTitle('Calendar')    
        self.show()

    def showDate(self, date):
        
        datestr="{} {}".format("Your Appointment is on:", date.toString())
        self.msg.about(self,"Appointment",datestr)
 
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
