#!/usr/bin/env python
# -*- coding: utf-8 -*-

# todo : mettre des logos au lieu de texte sur les boutons
# todo : écrire le nom du fichier avec les espaces + ok ou X directement dans le fichier
#            lors d'une phase de préparation des dossiers. Pour ne pas répéter toujours le code.
# todo : Créer les 2 boutons pour changer une fiche si exercice réussi ou pas.
# todo : diminuer le nbre de fonction pour voir tout, voir 10 lignes et tout voir
#           Je suis sûr que l'on peut le faire en 1 ou 2 fonctions

# En python 2.7 PySide 1

"""Le but de ce petit logiciel est de pouvoir faire des exercices en Python
   avec un classement de la difficulté et avec un petit système de gestion des
    exercices réussis ou pas. Il y a aussi la possibilité de ne voir qu'une partie de la solution
    pour savoir si on est dans la bonne voie ou pas."""

# Importation de différents modules Python.
import os
import utils as utl
from PySide import QtGui
from PySide import QtCore
# Importation des différents fichiers qui composent ce programme.
from interface_graphique.fenetreprincipale import Ui_ExercicesPython
from interface_graphique.fenetrecreafiche import Ui_fenetresecondaire
from interface_graphique.fenetremodiffiche import Ui_fenetretroisieme

from gestionfiche import GestionFiche as GestFich


class Main(QtGui.QMainWindow,  Ui_ExercicesPython, GestFich, Ui_fenetresecondaire, Ui_fenetretroisieme):
    """Cette classe représente la jonction entre la fenêtre principale de mon application et les calculs à proprement
        parlé. ( fiches gérées par GestFich."""

    def __init__(self):
        super(Main, self).__init__()     # permet d'hériter de QMainWindow

        # self.fiches_reussi = []
        # self.fiches_afaire = []
        self.contenu = ""
        self.textenonce = '# Enoncé :'
        self.textsoluce = '# Solution : '
        # self.fiches_ok = []
        # self.fiches_x = []
        # self.listfichselect = []

        # Déclaration de mes variables
        self.choix = ""
        self.niveaudeb = ""
        self.le_nomfich2 = ""

        # Appel des fonctions pour dessiner l'interface
        self.setupUi(self)
        # Appel de la fonction pour afficher les fiches
        self.affichlistfich()
        self.themesombre()
        self.connectioninterface()

    def connectioninterface(self):
        """ Pour connecter l'interface (via les boutons et menus) à la gestion des fiches."""

        self.btn_5lignes.clicked.connect(self.affich5lignes)
        self.btn_10lignes.clicked.connect(self.affich10lignes)
        self.btn_toutvoir.clicked.connect(self.affichconttotal)
        self.radbout_debut.clicked.connect(self.affichselectionfich)
        self.radbout_interme.clicked.connect(self.affichselectionfich)
        self.radbout_expert.clicked.connect(self.affichselectionfich)
        self.radbout_toutniv.clicked.connect(self.affichselectionfich)
        self.btexertout.clicked.connect(self.affichselectionfich)
        self.btexerfaire.clicked.connect(self.affichselectionfich)
        self.btexerreussi.clicked.connect(self.affichselectionfich)
        self.btn_faire.clicked.connect(self.afficharefaire)
        self.btn_reussite.clicked.connect(self.affichareussi)
        self.listwid_fichier.itemClicked.connect(self.affichenoncefich)
        self.actionFerm_fich.triggered.connect(self.fermerfichier)
        self.actionTheme_clair.triggered.connect(self.themeclair)
        self.actionTheme_sombre.triggered.connect(self.themesombre)
        self.actionCreer_exercice.triggered.connect(self.setupUIsecond)
        self.actionModifier_exercices.triggered.connect(self.afficherfich)
        self.actionSupprimer_exercices.triggered.connect(self.supprimerfich)
        self.actionAide_log.triggered.connect(self.affichinterfaceaide)
        self.action_Apropos.triggered.connect(self.affichinterfaceapropos)

    def affichlistfich(self):
        """Fonction permettant d'afficher les notes récupérées par la fonction liredosfich du fichier gestionfiche."""

        self.listwid_fichier.clear()            # nettoie la liste des fichiers
        self.listreussi_fichier.clear()         # nettoie la liste de note
        GestFich.liste_de_fiches, GestFich.listscore = self.liredosfich()
        self.listwid_fichier.addItems(GestFich.liste_de_fiches)
        self.listreussi_fichier.addItems(GestFich.listscore)

        self.compte_C = self.statfich()
        self.progressBar1.setValue(self.compte_C)

    def affichselectionfich(self):
        """Fonction pour afficher les notes selon leur niveau de difficulté et si elles sont réussies ou pas.

        self.choix: variable permettant de visualiser de différentes façons la liste de fiche
        self.choix: string
        """

        # cas de figure possible :

        # tous les niveaux et tous les exercices :
        if self.radbout_toutniv.isChecked() and self.btexertout.isChecked():
            self.choix = "A"
        # Tous les niveaux et réussis
        elif self.radbout_toutniv.isChecked() and self.btexerreussi.isChecked():
            self.choix = "B"
        # tous les niveaux et à faire
        elif self.radbout_toutniv.isChecked() and self.btexerfaire.isChecked():
            self.choix = "C"
        # Débutant et tous les exercices
        elif self.radbout_debut.isChecked() and self.btexertout.isChecked():
            self.choix = "D"
        # Débutant et réussis
        elif self.radbout_debut.isChecked() and self.btexerreussi.isChecked():
            self.choix = "E"
        # débutant et A faire
        elif self.radbout_debut.isChecked() and self.btexerfaire.isChecked():
            self.choix = "F"
        # intermédiaire et tous les exercices
        elif self.radbout_interme.isChecked() and self.btexertout.isChecked():
            self.choix = "G"
        # intermédiaire et réussis
        elif self.radbout_interme.isChecked() and self.btexerreussi.isChecked():
            self.choix = "H"
        # Intermédiaire et a faire
        elif self.radbout_interme.isChecked() and self.btexerfaire.isChecked():
            self.choix = "I"
        # Expert et tous les exercices
        elif self.radbout_expert.isChecked() and self.btexertout.isChecked():
            self.choix = 'J'
        # Expert et réussis
        elif self.radbout_expert.isChecked() and self.btexerreussi.isChecked():
            self.choix = "K"
        # expert et a faire
        elif self.radbout_expert.isChecked() and self.btexerfaire.isChecked():
            self.choix = "L"

        self.listwid_fichier.clear()
        self.listreussi_fichier.clear()
        self.selectionfich()

        self.listwid_fichier.addItems(self.fiches_selection)
        self.listreussi_fichier.addItems(self.fiches_reussi)

    def affichenoncefich(self):
        """Affichage de l'énoncé de la note sélectionnée
           en récupérant le nom et le chemin de l'exercice."""

        self.nomfich, self.chfich = self.selectfich()
        self.te_contenu.setText("")                 # nettoie la solution de l'exercice
        #
        # ATTENTION !
        #
        # pour la version python 3.5, plus besoin du decode
        # écrire simplement :
        # enoncefich = self.lirenoncefich()
        enoncefich = self.lirenoncefich().decode('UTF-8')
        self.te_enonce.setText(enoncefich)

    def affich5lignes(self):
        """Affichage de 5 lignes du contenu de la note."""

        self.nomfich, self.chfich = self.selectfich()
        contenu5 = self.lirecont5lignes().decode('UTF-8')
        self.te_contenu.setText(contenu5)

    def affich10lignes(self):
        """Affichage de 10 lignes du contenu de la note"""

        self.nomfich, self.chfich = self.selectfich()
        contenu10 = self.lirecont10lignes().decode('UTF-8')
        self.te_contenu.setText(contenu10)

    def affichconttotal(self):
        """Affichage du contenu complet de la note"""

        self.nomfich, self.chfich = self.selectfich()
        contenufich = self.lireconttout().decode('UTF-8')
        self.te_contenu.setText(contenufich)  # le texte est placé dans l'interface

    def afficharefaire(self):
        """Modification du'une fiche pour indiquer de le refaire et mise à jour de la liste
        des fichiers."""

        self.modficherefaire()
        self.affichselectionfich()
        self.compte_C = self.statfich()
        self.progressBar1.setValue(self.compte_C)

    def affichareussi(self):
        """Modification du'une fiche pour indiquer qu'elle est réussie et mise à jour de la liste
        des fichiers."""

        self.modfichereussi()
        self.affichselectionfich()
        self.compte_C = self.statfich()
        self.progressBar1.setValue(self.compte_C)

    def fermerfichier(self):
        """Action qui fermera définitivement l'application."""

        fenetreprincipale.close()

    def themeclair(self):
        """Affichage d'un thème clair pour l'interface"""

        f = QtCore.QFile("./interface_graphique/theme/interface_claire.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        self.setStyleSheet(stylesheet)

    def themesombre(self):
        """Affichage d'un thème sombre pour l'interface ( thème par défaut)."""

        f = QtCore.QFile("./interface_graphique/theme/interface_sombre.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        self.setStyleSheet(stylesheet)

    def affichcreafich(self):
        """Fonction permettant de récupérer les données de création d'une fiche d'exercice."""

        self.contenufich = ""
        self.enoncefich = ""
        self.nomfich = self.le_nomfich2.text()
        self.enoncefich = self.le_enonce2.toPlainText().encode('UTF-8')
        self.contenufich = self.le_soluce2.toPlainText().encode('UTF-8')
        if self.radbout_debut1.isChecked():
            self.niveaudeb = '# Niveau : débutant'
        if self.radbout_interme1.isChecked():
            self.niveaudeb = '# Niveau : intermédiaire'
        if self.radbout_expert1.isChecked():
            self.niveaudeb = '# Niveau : expert'
        test_alert = "# Ne pas toucher cette ligne jusquà # Enoncé. Sinon, le logiciel ne fonctionnera plus."
        mes_afaire = "# Réussite : non"
        self.contenu = test_alert + '\n' + self.niveaudeb + '\n' + mes_afaire + '\n' + self.textenonce + '\n' + self.enoncefich + '\n' + self.textsoluce + '\n' + self.contenufich
        self.contenu = GestFich.creationfich(self)
        self.le_nomfich2.clear()
        self.le_enonce2.clear()
        self.le_soluce2.clear()
        self.affichlistfich()

    def supprimerfich(self):
        """Fonction faisant le lien avec l'interface et la fonction suppressionfich."""

        fichselect = self.listwid_fichier.selectedItems()  # type list
        if not fichselect:
            return
        self.chfich = os.path.join(utl.dosdata, self.nomfich + '.txt')
        self.suppressionfich()
        self.affichlistfich()

    def selectfich(self):
        """Sélection de la note."""

        fichselect = self.listwid_fichier.selectedItems()  # type list
        if not fichselect:
            return
        self.nomfich = fichselect[-1].text()   # permet de récupérer juste le nom sélectionné
        self.chfich = os.path.join(utl.dosdata, '/', self.nomfich + '.txt')
        return self.nomfich, self.chfich

    def afficherfich(self):
        """Affichage de la fiche sélectionnée et possibilité de modification de celle-ci."""

        self.le_nomfich2 = ""

        # affichage fenêtre
        self.setupUItroisieme()
        # récupération du nom et du chemin d'accès de la fiche sélectionnée et affichage
        self.nomfich, self.chfich = self.selectfich()
        self.la_nomfich3.setText(self.nomfich)
        # lecture de l'énoncé
        self.enoncefich = self.lirenoncefich().decode('UTF-8')
        self.le_enonce3.setText(self.enoncefich)
        # affichage du niveau de la fiche sélectionnée
        if self.listfich_nom[self.nomfich][1] == '# Niveau : débutant':
            self.radbout_debut2.setChecked(True)
        elif self.listfich_nom[self.nomfich][1] == '# Niveau : intermédiaire':
            self.radbout_interme2.setChecked(True)
        else :
            self.radbout_expert2.setChecked(True)

        # récupération et affichage de la solution de la fiche sélectionnée
        self.contenufich = self.lireconttout().decode('UTF-8')
        self.le_soluce3.setText(self.contenufich)  # le texte est placé dans l'interface

    def modifierfich(self):
        """Fonction permettant de récupérer le contrenu de la fiche modifiée"""

        test_alert = "# Ne pas toucher cette ligne jusquà # Enoncé. Sinon, le logiciel ne fonctionnera plus."
        mes_afaires = "# Réussite : non"

        self.contenufich = ""
        self.enoncefich = ""
        self.nomfich = self.la_nomfich3.text()
        self.enoncefich = self.le_enonce3.toPlainText().encode('UTF-8')
        self.contenufich = self.le_soluce3.toPlainText().encode('UTF-8')
        if self.radbout_debut2.isChecked():
            self.niveaudeb = '# Niveau : débutant'
        if self.radbout_interme2.isChecked():
            self.niveaudeb = '# Niveau : intermédiaire'
        if self.radbout_expert2.isChecked():
            self.niveaudeb = '# Niveau : expert'

        self.contenu = test_alert + '\n' + self.niveaudeb + '\n' + mes_afaires + '\n' + self.textenonce + '\n'\
                       + self.enoncefich + '\n' + self.textsoluce + '\n' + self.contenufich
        self.contenu = GestFich.creationfich(self)
        self.la_nomfich3.clear()
        self.le_enonce3.clear()
        self.le_soluce3.clear()
        self.affichlistfich()

    def affichinterfaceaide(self):
        """Fonction pour créer une fenêtre d'aide avec un QMessageBox d'information."""

        phrase1 = "Ce programme est en cours de création, il peut donc contenir des bugs."
        phrase2 = "Veillez à ce qu'une fiche soit toujours sélectionnée pour la suppression, ou une modification " \
                  "d'une fiche."
        phrase3 = "Attention, la suppression d'une fiche est définitive et sans message d'alerte."
        phrase4 = phrase1.decode('UTF-8') + '\n' + phrase2.decode('UTF-8') + '\n'*2 + phrase3.decode('UTF-8')
        self.fenetreaide = QtGui.QMessageBox.information(self.fenetreprincipale_2, "Aide", phrase4)

    def affichinterfaceapropos(self):
        """fonction pour réaliser une fenêtre d'à-propos avec un QMessageBox d'information."""

        phrase1 = "<p>Ce programme a été réalisé par <strong>Sandy Taillan</strong> à partir " \
                  "du cours de Thibault Houdon sur Udemy.</p><br/> "
        phrase2 = "<p>Je remercie tout particulièrement <a href='https://github.com/Cardiox12'>@mielpops</a> " \
                  "pour m'avoir encouragé dans mon apprentissage de Python, "
        phrase3 = "et pour avoir réalisé les premiers challenges sur le Discord de Thibault.</p>"
        phrase4 = "<a href='https://www.dessins-plaisirs.fr/'>Mon site internet</a>"
        phrase5 = phrase1 + phrase2 + phrase3 + phrase4
        self.fenetreaide = QtGui.QMessageBox.information(self.fenetreprincipale_2, "A-propos", phrase5.decode('UTF-8'))


app = QtGui.QApplication([])
fenetreprincipale = Main()
fenetreprincipale.show()
app.exec_()
