#!/usr/bin/env python
# -*- coding: utf-8 -

# todo : d'abord le faire en python 2.7 puis en 3
# todo : Faire en PySide puis en PySide 2
# todo : Je devrais donc avoir au moins 2 ou 3 versions de mon script
# todo : rajouter une barre de progression avec la posssibilité d'indiquer qu'un exercice est réussi.
# todo : faire en sorte que des fenêtres pop pup s'ouvent pour indiquer l'énoncé et le contenu à la création de la fiche.
# todo : Faire en sorte que le texte dans les fiches soit en utf8.
#
# En python 2.7 PySide 1

# importation des modules nécessaire à la création de mon application
import os
from PySide import QtGui, QtCore
from pythonexercice_calcul import Fiche


class FenetrePrincipale(QtGui.QMainWindow, Fiche):
    """Cette classe représente la fenêtre principale de mon application."""

    def __init__(self):
        super(FenetrePrincipale, self).__init__()       # permet d'hériter de QMainWindow

        # On initialise la fenêtre en lui donnant un titre
        self.setWindowTitle('Mon Logiciel')

        # déclaration des variables
        chbase = os.path.dirname(__file__)
        self.nomfich = "ficheinitiale"
        self.dosdata = os.path.join(chbase, 'data')
        self.chfich = os.path.join(self.dosdata, '/' + self.nomfich + '.txt')
        self.niveaudeb = '# Niveau : débutant'
        self.textenonce = '# Enonce'
        self.textsoluce = '# Solution'

        # Appel de la fonction pour dessiner l'interface

        self.dossierdata()
        self.creationinterface()
        self.connectionInterface()
        self.affichlistfich()

    def creationinterface(self):
        """Création de l'interface graphique."""

        self.resize(760, 720)

        # Déclaration du centralwidget (obligatoire) et de la barre de menu
        self.centralwidget = QtGui.QWidget(self)
        self.menubar = QtGui.QMenuBar(self)
        self.statusbar = QtGui.QStatusBar(self)

        # Pour relier le centralwidget et la barre de menu à la fenêtre
        self.setCentralWidget(self.centralwidget)
        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

        # création du gridlayout (le self permet de le parenter à la fenêtre)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)

        # Création des boutons des niveaux
        self.radbout_debut = QtGui.QRadioButton(self.centralwidget)
        self.radbout_interme = QtGui.QRadioButton(self.centralwidget)
        self.radbout_expert = QtGui.QRadioButton(self.centralwidget)

        # Création du listWidget pour la liste de nom de fichier
        self.listwid_fichier = QtGui.QListWidget(self.centralwidget)

        # Création de la ligne de séparation
        self.line = QtGui.QFrame(self.centralwidget)

        # Création du label énoncé
        self.la_enonce = QtGui.QLabel(self.centralwidget)

        # Création du QtextEdit pour l'énoncé
        self.te_enonce = QtGui.QTextEdit(self.centralwidget)

        # Création du Qlabel pour le contenu
        self.la_contenu = QtGui.QLabel(self.centralwidget)

        # Création du QTextEdit pour le contenu
        self.te_contenu = QtGui.QTextEdit(self.centralwidget)

        # Création des boutons d'affichage du contenu
        self.btn_5lignes = QtGui.QPushButton(self.centralwidget)   # je crée un nouvel objet QPushButton
        self.btn_10lignes = QtGui.QPushButton(self.centralwidget)
        self.btn_toutvoir = QtGui.QPushButton(self.centralwidget)

        # création de la barre de menu
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuCreer_exer = QtGui.QMenu(self.menubar)
        self.menuChang_theme = QtGui.QMenu(self.menubar)
        self.menuAide = QtGui.QMenu(self.menubar)

        # création des sous-menus
        self.actionOuv_fich = QtGui.QAction(self)
        self.actionSauv_fich = QtGui.QAction(self)
        self.actionFerm_fich = QtGui.QAction(self)
        self.actionTheme_clair = QtGui.QAction(self)
        self.actionTheme_sombre = QtGui.QAction(self)
        self.actionAide_log = QtGui.QAction(self)
        self.action_Apropos = QtGui.QAction(self)
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

        # pour relier les widgets au gridlayout et leur donner une dimension
        self.gridLayout.addWidget(self.radbout_debut, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.radbout_interme, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.radbout_expert, 0, 2, 1, 1)

        self.listwid_fichier.setMinimumSize(QtCore.QSize(0, 490))
        self.gridLayout.addWidget(self.listwid_fichier, 2, 0, 5, 3)

        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.gridLayout.addWidget(self.line, 0, 3, 7, 1)

        self.gridLayout.addWidget(self.la_enonce, 0, 4, 1, 1)

        self.te_enonce.setMinimumSize(QtCore.QSize(300, 0))
        self.gridLayout.addWidget(self.te_enonce, 2, 4, 2, 3)

        self.gridLayout.addWidget(self.la_contenu, 4, 4, 1, 1)

        self.gridLayout.addWidget(self.te_contenu, 5, 4, 1, 3)

        self.gridLayout.addWidget(self.btn_5lignes, 6, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_10lignes, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_toutvoir, 6, 6, 1, 1)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 22))

        self.retranslate()

    def connectionInterface(self):
        """ Pour connecter l'interface au code véritable."""
        self.btn_5lignes.clicked.connect(self.direbonjour)
        self.btn_10lignes.clicked.connect(self.direaurevoir)
        self.btn_toutvoir.clicked.connect(self.diresalut)
        self.radbout_debut.clicked.connect(self.affichselectionfich)
        self.radbout_interme.clicked.connect(self.affichselectionfich)
        self.radbout_expert.clicked.connect(self.affichselectionfich)
        self.listwid_fichier.itemClicked.connect(self.affichenoncefich)

    def retranslate(self):
        self.radbout_debut.setText(QtGui.QApplication.translate("self", "Niv. Débutant", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_interme.setText(QtGui.QApplication.translate("self", "Niv. intermédiaire", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_expert.setText(QtGui.QApplication.translate("self", "Niv. expert", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce.setText(QtGui.QApplication.translate("self.", "Énoncé :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_contenu.setText(QtGui.QApplication.translate("self", "Solution :", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_5lignes.setText(QtGui.QApplication.translate("self", "Voir 5 lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_10lignes.setText(QtGui.QApplication.translate("self", "Voir 10 Lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_toutvoir.setText(QtGui.QApplication.translate("self", "Tout voir", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("self", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreer_exer.setTitle(QtGui.QApplication.translate("self", "Créer un exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.menuChang_theme.setTitle(QtGui.QApplication.translate("self", "Changer le thème", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAide.setTitle(QtGui.QApplication.translate("self", "Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuv_fich.setText(QtGui.QApplication.translate("self", "Ouvrir un fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSauv_fich.setText(QtGui.QApplication.translate("self", "Sauvegarder un fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFerm_fich.setText(QtGui.QApplication.translate("self", "Fermer le fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_clair.setText(QtGui.QApplication.translate("self", "Thème clair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_sombre.setText(QtGui.QApplication.translate("self", "Thème sombre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAide_log.setText(QtGui.QApplication.translate("self", "Aide sur le logiciel", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Apropos.setText(QtGui.QApplication.translate("self", "À Propos", None, QtGui.QApplication.UnicodeUTF8))

    # Création du slot
    def direbonjour(self):
        print('bonjour')

    def direaurevoir(self):
        print('Au revoir')

    def diresalut(self):
        print('salut')

    def affichlistfich(self):
        """Fonction permettant d'afficher les notes récupérées par la fonction liredosfich du fichiercalcul."""
        self.listwid_fichier.clear()                       # nettoie la liste de note
        self.listfiches = self.liredosfich()
        self.listwid_fichier.addItems(self.listfiches)

    def affichselectionfich(self):
        """Fonction pour afficher les notes selon leur niveau"""
        if self.radbout_debut.isChecked():
            self.niveaudeb = '# Niveau : débutant'
        if self.radbout_interme.isChecked():
            self.niveaudeb = '# Niveau : intermédiaire'
        if self.radbout_expert.isChecked():
            self.niveaudeb = '# Niveau : expert'

        self.listwid_fichier.clear()     # nettoie la liste de note
        self.listfichselect = []
        self.listfichselect= self.liredosfichselection()
        self.listwid_fichier.addItems(self.listfichselect)

    def selectfich(self):
        """Sélection de la note."""
        fichselect = self.listwid_fichier.selectedItems()  # type list
        if not fichselect:
            return
        self.nomfich = fichselect[-1].text()                # permet de récupérer juste le nom sélectionné
        self.chfich = os.path.join(self.dosdata, '/', self.nomfich + '.txt')
        return self.nomfich, self.chfich

    def affichenoncefich(self):
        """Affichage de l'énoncé de la note."""
        self.nomfich, self.chfich = self.selectfich()
        self.enoncefich = self.lirenoncefich()
        self.te_enonce.setText(self.enoncefich)





app = QtGui.QApplication([])        # création de l'application

fenetre = FenetrePrincipale()       # instanciation de la fenêtre principale J'ai maintenant un objet fenetre

fenetre.show()                      # affichage de la fenêtre
app.exec_()                         # exécution de l'application
