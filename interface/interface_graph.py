# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandy/Documents/informatique/mes-scripts/fenetre_avec_menu/interface/interface_graph.ui'
#
# Created: Fri Jun 15 07:02:54 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

















        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce.setText(QtGui.QApplication.translate("MainWindow", "Énoncé :", None, QtGui.QApplication.UnicodeUTF8))
        self.radbut_interme.setText(QtGui.QApplication.translate("MainWindow", "Niv. Intermédiaire", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_10lignes.setText(QtGui.QApplication.translate("MainWindow", "Voir 5 Lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_5lignes.setText(QtGui.QApplication.translate("MainWindow", "Voir 10 lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_toutvoir.setText(QtGui.QApplication.translate("MainWindow", "Tout voir", None, QtGui.QApplication.UnicodeUTF8))
        self.radbut_expert.setText(QtGui.QApplication.translate("MainWindow", "Niv. Expert", None, QtGui.QApplication.UnicodeUTF8))
        self.la_contenu.setText(QtGui.QApplication.translate("MainWindow", "Solution :", None, QtGui.QApplication.UnicodeUTF8))
        self.radbut_debutant.setText(QtGui.QApplication.translate("MainWindow", "Niv. Débutant", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreer_exer.setTitle(QtGui.QApplication.translate("MainWindow", "Créer un exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.menuChang_theme.setTitle(QtGui.QApplication.translate("MainWindow", "Changer le thème", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAide.setTitle(QtGui.QApplication.translate("MainWindow", "Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuv_fich.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir un fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSauv_fich.setText(QtGui.QApplication.translate("MainWindow", "Sauvegarder un fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFerm_fich.setText(QtGui.QApplication.translate("MainWindow", "Fermer le fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_clair.setText(QtGui.QApplication.translate("MainWindow", "Thème clair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_sombre.setText(QtGui.QApplication.translate("MainWindow", "Thème sombre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAide_log.setText(QtGui.QApplication.translate("MainWindow", "Aide sur le logiciel", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Apropos.setText(QtGui.QApplication.translate("MainWindow", "À Propos", None, QtGui.QApplication.UnicodeUTF8))

