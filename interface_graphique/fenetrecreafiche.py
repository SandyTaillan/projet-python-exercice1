#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore
from PySide import QtGui

class Ui_fenetresecondaire(object):
    def setupUIsecond(self):

        self.fenetrecreation = QtGui.QDialog(self.fenetreprincipale_2)
        self.fenetrecreation.setWindowModality(QtCore.Qt.ApplicationModal)
        self.fenetrecreation.show()

        self.fenetrecreation.resize(605, 555)

        self.gridLayout = QtGui.QGridLayout(self.fenetrecreation)
        self.la_nomfich2 = QtGui.QLabel(self.fenetrecreation)
        self.le_nomfich2 = QtGui.QLineEdit(self.fenetrecreation)
        self.radbout_debut1 = QtGui.QRadioButton(self.fenetrecreation)
        self.radbout_interme1 = QtGui.QRadioButton(self.fenetrecreation)
        self.radbout_expert1 = QtGui.QRadioButton(self.fenetrecreation)
        self.la_enonce2 = QtGui.QLabel(self.fenetrecreation)
        self.le_enonce2 = QtGui.QTextEdit(self.fenetrecreation)
        self.la_soluce2 = QtGui.QLabel(self.fenetrecreation)
        self.le_soluce2 = QtGui.QTextEdit(self.fenetrecreation)
        self.buttonBox = QtGui.QDialogButtonBox(self.fenetrecreation)

        self.la_nomfich2.setAlignment(QtCore.Qt.AlignCenter)
        self.la_enonce2.setAlignment(QtCore.Qt.AlignCenter)
        self.la_soluce2.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)


        self.gridLayout.addWidget(self.la_nomfich2, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.le_nomfich2, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.radbout_debut1, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.radbout_interme1, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.radbout_expert1, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.la_enonce2, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.le_enonce2, 7, 0, 1, 4)
        self.gridLayout.addWidget(self.la_soluce2, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.le_soluce2, 10, 0, 1, 4)
        self.gridLayout.addWidget(self.buttonBox, 11, 2, 1, 1)

        self.radbout_debut1.setMinimumSize(190, 20)
        self.radbout_interme1.setMinimumSize(190,20)
        self.radbout_expert1.setMinimumSize(150, 20)

        self.retranslateUisecond()

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.fenetrecreation.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.fenetrecreation.reject)


        self.buttonBox.clicked.connect(self.affichcreafich)


        QtCore.QMetaObject.connectSlotsByName(self.fenetrecreation)

    def retranslateUisecond(self):
        self.setWindowTitle(QtGui.QApplication.translate("self.fenetrecreation", "Création d'une fiche", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.la_nomfich2.setText(
            QtGui.QApplication.translate("self.fenetrecreation", "Entrez le nom de la fiche :", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.la_enonce2.setText(
            QtGui.QApplication.translate("self.fenetrecreation", "Entrez l'énoncé de la fiche : ", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.la_soluce2.setText(
            QtGui.QApplication.translate("self.fenetrecreation", "Entrez la solution de la fiche :", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.radbout_debut1.setText(QtGui.QApplication.translate("self.fenetrecreation", "Niv. débutant", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.radbout_interme1.setText(
            QtGui.QApplication.translate("self.fenetrecreation", "Niv. intermédiaire", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.radbout_expert1.setText(QtGui.QApplication.translate("self.fenetrecreation", "Niv. expert", None,
                                                                  QtGui.QApplication.UnicodeUTF8))


