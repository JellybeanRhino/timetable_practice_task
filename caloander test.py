#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows a QCalendarWidget widget.

Author: Jan Bodnar
Website: zetcode.com
"""
# imports and intialising shit
from PySide6.QtWidgets import (QWidget, QCalendarWidget,
        QLabel, QApplication, QVBoxLayout)
from PySide6.QtCore import QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    # This the gui shit, dont worry about it being weird in a task it can be outside a class
    def initUI(self):
        #Layout
        vbox = QVBoxLayout(self)
        #Calender
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        # Calender in the layout
        vbox.addWidget(cal)
        #Label
        self.lbl = QLabel(self)
        # GET THE DATE BY CALLING .selectedDate()!!!!!!
        date = cal.selectedDate()
        # just setting label to the date by converting it into a string
        self.lbl.setText(date.toString())
        # Add label to the layout
        vbox.addWidget(self.lbl)
        # set window to layout
        self.setLayout(vbox)
        # basic shit i shouldve done at beginning
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    #!! THIS THE SHIT !!
    def showDate(self, date):
        # date.toString() converts the shit to str value
        # IF "" IN "" THEN DO "" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # GET ME?? 
        if "Mon" in date.toString():
            # THIS IS WHERE YOU MAKE IT DO THE THING
            # FOR EXAMPLE SAY THAT DAYS TIMETABLE
            # ITS EASY YOU GOT IT
            self.lbl.setText(date.toString())
        else:
            # TEST IF IT WORKED
            print("Not monday")


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
# RUN BECAUSE I GENIUS<3 HOPE THIS IS EAYS AND HELPFUL
# LOVE RHIANNON