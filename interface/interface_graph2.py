# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandy/Documents/informatique/mes-scripts/projet-python-exercice1/interface/interface_graph2.ui'
#
# Created: Tue Jun 19 07:31:51 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 719)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.te_enonce = QtGui.QTextEdit(self.centralwidget)
        self.te_enonce.setMinimumSize(QtCore.QSize(300, 0))
        self.te_enonce.setObjectName("te_enonce")
        self.gridLayout.addWidget(self.te_enonce, 2, 4, 2, 3)
        self.la_enonce = QtGui.QLabel(self.centralwidget)
        self.la_enonce.setObjectName("la_enonce")
        self.gridLayout.addWidget(self.la_enonce, 0, 4, 1, 1)
        self.radbut_interme = QtGui.QRadioButton(self.centralwidget)
        self.radbut_interme.setObjectName("radbut_interme")
        self.gridLayout.addWidget(self.radbut_interme, 0, 1, 1, 1)
        self.te_contenu = QtGui.QTextEdit(self.centralwidget)
        self.te_contenu.setObjectName("te_contenu")
        self.gridLayout.addWidget(self.te_contenu, 5, 4, 1, 3)
        self.btn_10lignes = QtGui.QPushButton(self.centralwidget)
        self.btn_10lignes.setObjectName("btn_10lignes")
        self.gridLayout.addWidget(self.btn_10lignes, 6, 4, 1, 1)
        self.btn_5lignes = QtGui.QPushButton(self.centralwidget)
        self.btn_5lignes.setObjectName("btn_5lignes")
        self.gridLayout.addWidget(self.btn_5lignes, 6, 5, 1, 1)
        self.btn_toutvoir = QtGui.QPushButton(self.centralwidget)
        self.btn_toutvoir.setObjectName("btn_toutvoir")
        self.gridLayout.addWidget(self.btn_toutvoir, 6, 6, 1, 1)
        self.radbut_expert = QtGui.QRadioButton(self.centralwidget)
        self.radbut_expert.setObjectName("radbut_expert")
        self.gridLayout.addWidget(self.radbut_expert, 0, 2, 1, 1)
        self.la_contenu = QtGui.QLabel(self.centralwidget)
        self.la_contenu.setObjectName("la_contenu")
        self.gridLayout.addWidget(self.la_contenu, 4, 4, 1, 1)
        self.radbut_debutant = QtGui.QRadioButton(self.centralwidget)
        self.radbut_debutant.setEnabled(True)
        self.radbut_debutant.setMinimumSize(QtCore.QSize(0, 0))
        self.radbut_debutant.setObjectName("radbut_debutant")
        self.gridLayout.addWidget(self.radbut_debutant, 0, 0, 1, 1)
        self.listwid_fichier = QtGui.QListWidget(self.centralwidget)
        self.listwid_fichier.setMinimumSize(QtCore.QSize(0, 490))
        self.listwid_fichier.setObjectName("listwid_fichier")
        self.gridLayout.addWidget(self.listwid_fichier, 2, 0, 5, 3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 3, 7, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 22))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuCreer_exer = QtGui.QMenu(self.menubar)
        self.menuCreer_exer.setObjectName("menuCreer_exer")
        self.menuChang_theme = QtGui.QMenu(self.menubar)
        self.menuChang_theme.setObjectName("menuChang_theme")
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuv_fich = QtGui.QAction(MainWindow)
        self.actionOuv_fich.setObjectName("actionOuv_fich")
        self.actionSauv_fich = QtGui.QAction(MainWindow)
        self.actionSauv_fich.setObjectName("actionSauv_fich")
        self.actionFerm_fich = QtGui.QAction(MainWindow)
        self.actionFerm_fich.setObjectName("actionFerm_fich")
        self.actionTheme_clair = QtGui.QAction(MainWindow)
        self.actionTheme_clair.setObjectName("actionTheme_clair")
        self.actionTheme_sombre = QtGui.QAction(MainWindow)
        self.actionTheme_sombre.setObjectName("actionTheme_sombre")
        self.actionAide_log = QtGui.QAction(MainWindow)
        self.actionAide_log.setObjectName("actionAide_log")
        self.action_Apropos = QtGui.QAction(MainWindow)
        self.action_Apropos.setObjectName("action_Apropos")
        self.menuFichier.addAction(self.actionOuv_fich)
        self.menuFichier.addAction(self.actionSauv_fich)
        self.menuFichier.addAction(self.actionFerm_fich)
        self.menuChang_theme.addAction(self.actionTheme_clair)
        self.menuChang_theme.addAction(self.actionTheme_sombre)
        self.menuAide.addAction(self.actionAide_log)
        self.menuAide.addAction(self.action_Apropos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuCreer_exer.menuAction())
        self.menubar.addAction(self.menuChang_theme.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

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

