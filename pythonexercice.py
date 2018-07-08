# -*- coding: utf-8 -*-


# todo : d'abord le faire en python 2.7 puis en 3
# todo : Faire en PySide puis en PySide 2
# todo : Je devrais donc avoir au moins 2 ou 3 versions de mon script
# todo : rajouter une barre de progression avec la posssibilité d'indiquer qu'un exercice est réussi.
# todo : Je n'arrive pas à modifier plusieurs fois une fiche. Message d'erreur :
#                           QLayout: Attempting to add QLayout "" to QDialog "", which already has a layout
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
        self.nomfich = ""
        self.dosdata = os.path.join(chbase, 'data')
        self.chfich = os.path.join(self.dosdata, '/' + self.nomfich + '.txt')
        self.niveaudeb = '# Niveau : débutant'
        self.textenonce = '# Enoncé :'
        self.textsoluce = '# Solution : '
        self.contenu = ""

        # Appel des fonctions pour dessiner l'interface
        self.creationinterface()
        self.connectioninterface()
        self.themesombre()
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
        self.menuGestion_fiche = QtGui.QMenu(self.menubar)
        self.menuChang_theme = QtGui.QMenu(self.menubar)
        self.menuAide = QtGui.QMenu(self.menubar)

        # création des sous-menus
        self.actionOuv_fich = QtGui.QAction(self)
        #self.actionSauv_fich = QtGui.QAction(self)
        self.actionFerm_fich = QtGui.QAction(self)
        self.actionCreer_exercice = QtGui.QAction(self)
        self.acionModifier_exercices = QtGui.QAction(self)
        self.actionSupprimer_exercices = QtGui.QAction(self)
        self.actionTheme_clair = QtGui.QAction(self)
        self.actionTheme_sombre = QtGui.QAction(self)
        self.actionAide_log = QtGui.QAction(self)
        self.action_Apropos = QtGui.QAction(self)


        self.menuFichier.addAction(self.actionOuv_fich)
        #self.menuFichier.addAction(self.actionSauv_fich)
        self.menuFichier.addAction(self.actionFerm_fich)
        self.menuGestion_fiche.addAction(self.actionCreer_exercice)
        self.menuGestion_fiche.addAction(self.acionModifier_exercices)
        self.menuGestion_fiche.addAction(self.actionSupprimer_exercices)
        self.menuChang_theme.addAction(self.actionTheme_clair)
        self.menuChang_theme.addAction(self.actionTheme_sombre)
        self.menuAide.addAction(self.actionAide_log)
        self.menuAide.addAction(self.action_Apropos)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuGestion_fiche.menuAction())
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

    def connectioninterface(self):
        """ Pour connecter l'interface au code véritable."""
        self.btn_5lignes.clicked.connect(self.affich5lignes)
        self.btn_10lignes.clicked.connect(self.affich10lignes)
        self.btn_toutvoir.clicked.connect(self.affichConttotal)
        self.radbout_debut.clicked.connect(self.affichselectionfich)
        self.radbout_interme.clicked.connect(self.affichselectionfich)
        self.radbout_expert.clicked.connect(self.affichselectionfich)
        self.listwid_fichier.itemClicked.connect(self.affichenoncefich)
        self.actionFerm_fich.triggered.connect(self.fermerfichier)
        self.actionTheme_clair.triggered.connect(self.themeclair)
        self.actionTheme_sombre.triggered.connect(self.themesombre)
        self.actionCreer_exercice.triggered.connect(self.affichcreafich)
        self.acionModifier_exercices.triggered.connect(self.modifierfiche)
        self.actionSupprimer_exercices.triggered.connect(self.supprimerfich)

    def retranslate(self):
        """Pour que le texte s'affiche en utf8."""

        self.radbout_debut.setText(QtGui.QApplication.translate("self", "Niv. Débutant", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_interme.setText(QtGui.QApplication.translate("self", "Niv. intermédiaire", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_expert.setText(QtGui.QApplication.translate("self", "Niv. expert", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce.setText(QtGui.QApplication.translate("self.", "Énoncé :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_contenu.setText(QtGui.QApplication.translate("self", "Solution :", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_5lignes.setText(QtGui.QApplication.translate("self", "Voir 5 lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_10lignes.setText(QtGui.QApplication.translate("self", "Voir 10 Lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_toutvoir.setText(QtGui.QApplication.translate("self", "Tout voir", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("self", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGestion_fiche.setTitle(QtGui.QApplication.translate("self", "Fiche", None, QtGui.QApplication.UnicodeUTF8))
        self.menuChang_theme.setTitle(QtGui.QApplication.translate("self", "Changer le thème", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAide.setTitle(QtGui.QApplication.translate("self", "Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuv_fich.setText(QtGui.QApplication.translate("self", "Ouvrir un fichier", None, QtGui.QApplication.UnicodeUTF8))
        #self.actionSauv_fich.setText(QtGui.QApplication.translate("self", "Sauvegarder un fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFerm_fich.setText(QtGui.QApplication.translate("self", "Fermer le fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreer_exercice.setText(QtGui.QApplication.translate("self", "Créer un exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.acionModifier_exercices.setText(QtGui.QApplication.translate("self", "Modifier l'exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSupprimer_exercices.setText(QtGui.QApplication.translate("self", "Supprimer l'exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_clair.setText(QtGui.QApplication.translate("self", "Thème clair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTheme_sombre.setText(QtGui.QApplication.translate("self", "Thème sombre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAide_log.setText(QtGui.QApplication.translate("self", "Aide sur le logiciel", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Apropos.setText(QtGui.QApplication.translate("self", "À Propos", None, QtGui.QApplication.UnicodeUTF8))

    # Création des slots
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
        self.nomfich = fichselect[-1].text()               # permet de récupérer juste le nom sélectionné
        self.chfich = os.path.join(self.dosdata, '/', self.nomfich + '.txt')
        return self.nomfich, self.chfich

    def affichenoncefich(self):
        """Affichage de l'énoncé de la note."""
        self.nomfich, self.chfich = self.selectfich()
        self.enoncefich = self.lirenoncefich().decode('UTF-8')
        self.te_enonce.setText(self.enoncefich)

    def affich5lignes(self):
        """Affichage de 5 lignes du contenu de la note"""

        self.nomfich, self.chfich = self.selectfich()
        contenu5 = self.lirecont5lignes().decode('UTF-8')
        self.te_contenu.setText(contenu5)                 # le texte est placé dans l'interface

    def affich10lignes(self):
        """Affichage de 10 lignes du contenu de la note"""

        self.nomfich, self.chfich = self.selectfich()
        contenu10 = self.lirecont10lignes().decode('UTF-8')
        self.te_contenu.setText(contenu10)

    def affichConttotal(self):
        """Affichage du contenu complet de la note"""

        self.nomfich, self.chfich = self.selectfich()
        contenufich = self.lireconttout().decode('UTF-8')
        self.te_contenu.setText(contenufich)  # le texte est placé dans l'interface

    def affichcreafich(self):

        self.fenetrecreation = QtGui.QDialog()
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

        self.retranslateUi()

        f = QtCore.QFile("./interface/theme/interface_sombre.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        self.fenetrecreation.setStyleSheet(stylesheet)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.fenetrecreation.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.fenetrecreation.reject)


        self.buttonBox.clicked.connect(self.donneescreatfich)


        QtCore.QMetaObject.connectSlotsByName(self.fenetrecreation)

    def fermerfichier(self):
        fenetre.close()

    def donneescreatfich(self):
        """Fonction permettant de récupérer les données de création d'une fiche d'exercice."""

        self.nomfich = self.le_nomfich2.text()
        self.enoncefich = self.le_enonce2.toPlainText().encode('UTF-8')
        self.contenufich = self.le_soluce2.toPlainText().encode('UTF-8')
        if self.radbout_debut1.isChecked():
            self.niveaudeb = '# Niveau : débutant'
        if self.radbout_interme1.isChecked():
            self.niveaudeb = '# Niveau : intermédiaire'
        if self.radbout_expert1.isChecked():
            self.niveaudeb = '# Niveau : expert'

        self.contenu = self.niveaudeb + '\n' + self.textenonce + '\n' + self.enoncefich + '\n' + self.textsoluce + '\n' + self.contenufich

        Fiche.creationfich(self)
        self.le_nomfich2.clear()
        self.le_enonce2.clear()
        self.le_soluce2.clear()
        self.affichlistfich()

    def supprimerfich(self):
        """Fonction faisant le lien avec l'interface et la fonction suppressionfich"""

        fichselect = self.listwid_fichier.selectedItems()  # type list
        if not fichselect:
            return
        self.chfich = os.path.join(self.dosdata, self.nomfich + '.txt')
        self.suppressionfich()
        self.affichlistfich()

    def modifierfiche(self):
        """Fonction pour créer l'interface graphique de la modification de fiche."""

        # affichage fenêtre
        self.affichcreafich()
        # récupération du nom et du chemin d'accès de la fiche sélectionnée et affichage
        self.nomfich, self.chfich = self.selectfich()
        self.le_nomfich2.setText(self.nomfich)
        # affiche du niveau de la fiche sélectionnée
        if self.contenonce[0] == '# Niveau : débutant':
            self.radbout_debut1.setChecked(True)
        elif self.contenonce[0] == '# Niveau : intermédiaire':
            self.radbout_interme1.setChecked(True)
        else :
            self.radbout_expert1.setChecked(True)
        # récupération de l'énoncé de la fiche et affichage
        self.enoncefich = self.lirenoncefich().decode('UTF-8')
        self.le_enonce2.setText(self.enoncefich)
        # récupération et affichage de la solution de la fiche sélectionnée
        self.contenufich = self.lireconttout().decode('UTF-8')
        self.le_soluce2.setText(self.contenufich)  # le texte est placé dans l'interface
        self.affichlistfich()
        
    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("self.fenetrecreation", "Création d'une fiche", None, QtGui.QApplication.UnicodeUTF8))
        self.la_nomfich2.setText(QtGui.QApplication.translate("self.fenetrecreation", "Entrez le nom de la fiche :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce2.setText(QtGui.QApplication.translate("self.fenetrecreation", "Entrez l'énoncé de la fiche : ", None, QtGui.QApplication.UnicodeUTF8))
        self.la_soluce2.setText(QtGui.QApplication.translate("self.fenetrecreation", "Entrez la solution de la fiche :", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_debut1.setText(QtGui.QApplication.translate("self.fenetrecreation", "Niv. débutant", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_interme1.setText(QtGui.QApplication.translate("self.fenetrecreation", "Niv. intermédiaire", None, QtGui.QApplication.UnicodeUTF8))
        self.radbout_expert1.setText(QtGui.QApplication.translate("self.fenetrecreation", "Niv. expert", None, QtGui.QApplication.UnicodeUTF8))
    # gestion des thèmes

    def themesombre(self):
        """Affichage d'un thème sombre pour l'interface ( thème par défaut)."""

        f = QtCore.QFile("./interface/theme/interface_sombre.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        self.setStyleSheet(stylesheet)

    def themeclair(self):
        """Affichage d'un thème clair pour l'interface"""

        f = QtCore.QFile("./interface/theme/interface_claire.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        self.setStyleSheet(stylesheet)


app = QtGui.QApplication([])        # création de l'application
fenetre = FenetrePrincipale()       # instanciation de la fenêtre principale J'ai maintenant un objet fenetre
fenetre.show()                      # affichage de la fenêtre
app.exec_()                         # exécution de l'application
