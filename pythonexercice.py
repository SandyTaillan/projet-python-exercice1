#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui
from interfacegraph.interface_graph import Ui_ExercicePython


class Relationinterface(QtGui.QMainWindow, Ui_ExercicePython):

    def __init__(self):
        super(Relationinterface, self).__init__()

        # Lancement des script
        self.setupUi(ExercicePython)
        self.Connectioninterface()

    def Connectioninterface(self):

        self.btn_5lignes.clicked.connect(self.lirefich)

    def lirefich(self):
        print('premier test')

app = QtGui.QApplication([])

ExercicePython = QtGui.QMainWindow()

Relationinterface()
ExercicePython.show()
app.exec_()