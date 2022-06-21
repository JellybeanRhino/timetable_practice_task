# Timetable
# Rhiannon MacCreadie
# 22/06/2022
# 22/06/2022

# Sys Setup
from PySide6.QtWidgets import *
from dataclasses import dataclass
from datetime import time
import sys

# OOP
# Class()
@dataclass
class Class():
    _course_name: str
    _teacher_code: str
    _teacher_name: str
    _class_start: time
    _class_finish: time

    @property
    def course_name(self) -> str:
        return self._course_name

    @property
    def teacher_code(self) -> str:
        return self._teacher_code

    @property
    def teacher_name(self) -> str:
        return self._teacher_name

    @property
    def class_start(self) -> str:
        return self._class_start

    @property
    def class_finish(self) -> str:
        return self._class_finish


# Day()
@dataclass
class Day():
    _day_name: str
    _class_one: dict
    _class_two: dict
    _class_three: dict
    _class_four: dict
    _class_five: dict


# Week()
@dataclass
class Week():
    _monday: str
    _tuesday: str
    _wednesday: str
    _thursday: str
    _friday: str


# Gui

# Calander 
# Insert calander widget
# if in 
# print day

# Timetable print 
# Button
# Week pretty print
