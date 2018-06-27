# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandy/Documents/informatique/mes-scripts/projet-python-exercice1/interface/interface_graph3.ui'
#
# Created: Sun Jun 24 14:52:23 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 555)
        Dialog.setModal(True)




        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Création d\'une fiche", None, QtGui.QApplication.UnicodeUTF8))
        self.la_soluce2.setText(QtGui.QApplication.translate("Dialog", "Entrez la solution de la fiche :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce2.setText(QtGui.QApplication.translate("Dialog", "Entrez l\'énoncé de la fiche : ", None, QtGui.QApplication.UnicodeUTF8))
        self.la_nomfich2.setText(QtGui.QApplication.translate("Dialog", "Entrez le nom de la fiche :", None, QtGui.QApplication.UnicodeUTF8))
