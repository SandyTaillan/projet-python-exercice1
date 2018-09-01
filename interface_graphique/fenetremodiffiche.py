#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore
from PySide import QtGui

class Ui_fenetretroisieme(object):
    def setupUItroisieme(self):

        self.fenetremodif = QtGui.QDialog(self.fenetreprincipale_2)
        self.fenetremodif.setWindowModality(QtCore.Qt.ApplicationModal)
        self.fenetremodif.show()

        self.fenetremodif.resize(605, 555)

        self.gridLayout = QtGui.QGridLayout(self.fenetremodif)
        self.la_nomfich3 = QtGui.QLabel(self.fenetremodif)

        self.radbout_debut2 = QtGui.QRadioButton(self.fenetremodif)
        self.radbout_interme2 = QtGui.QRadioButton(self.fenetremodif)
        self.radbout_expert2 = QtGui.QRadioButton(self.fenetremodif)
        self.la_enonce3 = QtGui.QLabel(self.fenetremodif)
        self.le_enonce3 = QtGui.QTextEdit(self.fenetremodif)
        self.la_soluce3 = QtGui.QLabel(self.fenetremodif)
        self.le_soluce3 = QtGui.QTextEdit(self.fenetremodif)
        self.buttonBox = QtGui.QDialogButtonBox(self.fenetremodif)

        self.la_nomfich3.setAlignment(QtCore.Qt.AlignCenter)
        self.la_enonce3.setAlignment(QtCore.Qt.AlignCenter)
        self.la_soluce3.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.la_nomfich3, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.radbout_debut2, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.radbout_interme2, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.radbout_expert2, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.la_enonce3, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.le_enonce3, 7, 0, 1, 4)
        self.gridLayout.addWidget(self.la_soluce3, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.le_soluce3, 10, 0, 1, 4)
        self.gridLayout.addWidget(self.buttonBox, 11, 2, 1, 1)

        self.radbout_debut2.setMinimumSize(190, 20)
        self.radbout_interme2.setMinimumSize(190,20)
        self.radbout_expert2.setMinimumSize(150, 20)

        self.retranslateUitroisieme()

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.fenetremodif.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.fenetremodif.reject)

        self.buttonBox.clicked.connect(self.modifierfich)


        QtCore.QMetaObject.connectSlotsByName(self.fenetremodif)

    def retranslateUitroisieme(self):
        self.setWindowTitle(QtGui.QApplication.translate("self.fenetremodif", "Création d'une fiche", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.la_nomfich3.setText(
            QtGui.QApplication.translate("self.fenetremodif", self.nomfich, None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.la_enonce3.setText(
            QtGui.QApplication.translate("self.fenetremodif", "Entrez l'énoncé de la fiche : ", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.la_soluce3.setText(
            QtGui.QApplication.translate("self.fenetremodif", "Entrez la solution de la fiche :", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.radbout_debut2.setText(QtGui.QApplication.translate("self.fenetremodif", "Niv. débutant", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.radbout_interme2.setText(
            QtGui.QApplication.translate("self.fenetremodif", "Niv. intermédiaire", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.radbout_expert2.setText(QtGui.QApplication.translate("self.fenetremodif", "Niv. expert", None,
                                                                  QtGui.QApplication.UnicodeUTF8))



