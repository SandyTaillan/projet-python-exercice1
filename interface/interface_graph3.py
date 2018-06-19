# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandy/Documents/informatique/mes-scripts/projet-python-exercice1/interface/interface_graph3.ui'
#
# Created: Tue Jun 19 07:31:51 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 555)
        Dialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.la_nomfich2 = QtGui.QLabel(Dialog)
        self.la_nomfich2.setAlignment(QtCore.Qt.AlignCenter)
        self.la_nomfich2.setObjectName("la_nomfich2")
        self.verticalLayout.addWidget(self.la_nomfich2)
        self.le_nomfich2 = QtGui.QLineEdit(Dialog)
        self.le_nomfich2.setObjectName("le_nomfich2")
        self.verticalLayout.addWidget(self.le_nomfich2)
        self.la_enonce2 = QtGui.QLabel(Dialog)
        self.la_enonce2.setAlignment(QtCore.Qt.AlignCenter)

        self.la_enonce2.setObjectName("la_enonce2")
        self.verticalLayout.addWidget(self.la_enonce2)
        self.le_enonce2 = QtGui.QTextEdit(Dialog)
        self.le_enonce2.setObjectName("le_enonce2")
        self.verticalLayout.addWidget(self.le_enonce2)

        self.la_soluce2 = QtGui.QLabel(Dialog)
        self.la_soluce2.setAlignment(QtCore.Qt.AlignCenter)
        self.la_soluce2.setObjectName("la_soluce2")
        self.verticalLayout.addWidget(self.la_soluce2)
        self.le_soluce2 = QtGui.QTextEdit(Dialog)

        self.le_soluce2.setObjectName("le_soluce2")
        self.verticalLayout.addWidget(self.le_soluce2)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(gDialo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Création d\'une fiche", None, QtGui.QApplication.UnicodeUTF8))
        self.la_nomfich2.setText(QtGui.QApplication.translate("Dialog", "Entrez le nom de la fiche :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce2.setText(QtGui.QApplication.translate("Dialog", "Entrez l\'énoncé de la fiche : ", None, QtGui.QApplication.UnicodeUTF8))
        self.la_soluce2.setText(QtGui.QApplication.translate("Dialog", "Entrez la solution de la fiche :", None, QtGui.QApplication.UnicodeUTF8))

