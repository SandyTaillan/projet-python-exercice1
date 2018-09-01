#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import utils as utl
from glob import glob


class GestionFiche(object):
    """Cette classe regroupe toutes les opérations à effectuer sur les fiches.

    :param self.listfich_nom: dictionnaire regroupant les noms de fiches avec leur contenus
    :param self.fiches_afaire: contient les 'X' (fichiers pas fait)
    :param self.fiches_reussi: contient les 'ok' (fichiers réussis)
    :param self.fiches_selection: liste des noms de fiches correspondant au choix de l'utilisateur pour l'affichage

    :type self.listfich_nom: dict
    :type self.fiches_afaire: list
    :type self.fiches_reussi: list
    :type self.fiches_selection: list

    """

    def __init__(self):

        self.listfich_nom = {}
        self.fiches_afaire = []
        self.fiches_reussi = []
        self.fiches_selection = []

        self.nomfich = ""
        self.chfich = ""
        self.fiches_x = []
        self.fiches_ok = []
        self.choix = ""

    def liredosfich(self):
        """Lit le nom des fiches dans le dossier data et les place dans un dictionnaire
            avec indication de réussite ou non.

         liste_de_fiches : Liste avec tous les noms de fiches(nom du fichier)
         contenu_total :Liste de tout le contenu des fiches
         liste_de_fiches : list
         contenu_total: list
            """
        # initialisation des variables de la fonction
        self.fiches_afaire = []
        self.fiches_reussi = []
        liste_de_fiches = []
        contenu_total = []
        listfiches = sorted(glob(utl.dosdata + '/*.txt'))
        self.compte_C = ""

        for i in listfiches:
            liste_de_fiches.append(os.path.splitext(os.path.split(i)[-1])[0])
            with open(i, 'r') as f:
                contenu_fiche = f.read().splitlines()
                contenu_total.append(contenu_fiche)
                if contenu_fiche[2] == '# Réussite : ok':
                    self.fiches_reussi.append("ok")
                elif contenu_fiche[2] == '# Réussite : non':
                    self.fiches_afaire.append('X')
        # la ligne suivante me permet de mettre dans un dictionnaire le nom des fiches avec leur contenu respectif
        self.listfich_nom = {x: y for x, y in zip(liste_de_fiches, contenu_total)}
        listscore = self.fiches_afaire + self.fiches_reussi

        return liste_de_fiches, listscore

    def selectionfich(self):
        """Sélection des fiches par rapport aux boutons sélectionnés.

        self.choix: variable contenant le choix de l'utilisateur pour l'affichage des noms de fiches
        self.choix: string
        """

        self.fiches_selection = []
        self.fiches_reussi = []

        if self.choix == "A":
            for i in self.listfich_nom.keys():
                self.fiches_selection.append(i)
                if self.listfich_nom[i][2] == '# Réussite : ok':
                    self.fiches_reussi.append("ok")
                else:
                    self.fiches_reussi.append("X")

        elif self.choix == "B":
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][2] == '# Réussite : ok':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append('ok')

        elif self.choix == "C":
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][2] == '# Réussite : non':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append('X')

        elif self.choix == 'D':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : débutant':
                    self.fiches_selection.append(i)
                    if self.listfich_nom[i][2] == '# Réussite : ok':
                        self.fiches_reussi.append("ok")
                    else:
                        self.fiches_reussi.append("X")

        elif self.choix == 'E':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : débutant' and self.listfich_nom[i][2] == '# Réussite : ok':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append('ok')

        elif self.choix == 'F':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : débutant' and self.listfich_nom[i][2] == '# Réussite : non':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append("X")

        elif self.choix == 'G':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : intermédiaire':
                    self.fiches_selection.append(i)
                    if self.listfich_nom[i][2] == '# Réussite : ok':
                        self.fiches_reussi.append("ok")
                    else:
                        self.fiches_reussi.append("X")

        elif self.choix == 'H':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : intermédiaire' and \
                        self.listfich_nom[i][2] == '# Réussite : ok':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append("ok")

        elif self.choix == 'I':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : intermédiaire' and \
                        self.listfich_nom[i][2] == '# Réussite : non':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append("X")

        elif self.choix == 'J':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : expert':
                    self.fiches_selection.append(i)
                    if self.listfich_nom[i][2] == '# Réussite : ok':
                        self.fiches_reussi.append("ok")
                    else:
                        self.fiches_reussi.append("X")

        elif self.choix == 'K':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : expert' and self.listfich_nom[i][2] == '# Réussite : ok':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append("ok")

        elif self.choix == 'L':
            for i in self.listfich_nom.keys():
                if self.listfich_nom[i][1] == '# Niveau : expert' and self.listfich_nom[i][2] == '# Réussite : non':
                    self.fiches_selection.append(i)
                    self.fiches_reussi.append("X")

        return self.fiches_selection

    def lirenoncefich(self):
        """Lire l'énoncé de l'exercice dans le dictionnaire (self.listfich_nom) contenant l'exercice.

        enonce: énoncé de l'exercice récupéré du dictionnaire mais avec du texte que l'on ne veut pas afficher.
        index1: indice du début de l'énoncé dans la liste
        index2: indice de fin de l'énoncé dans la liste
        texte: énoncé de l'exercice tel que l'on veut qu'il s'affiche.
                      le texte est compris entre énoncé et code.
        enoncefich: énoncé de l'exercice sous forme de string tel que l'on souhaite l'afficher.

        enonce: list
        index1: integer
        index2: integer
        texte: list
        enoncefich: string
        """

        self.enoncefich = ""
        enonce = self.listfich_nom[self.nomfich]
        index1 = enonce.index(utl.textenonce)
        index2 = enonce.index(utl.textsoluce)
        texte = (enonce[(index1 + 1): index2])  # le texte est compris entre énoncé et code en liste
        for line in texte:
            self.enoncefich = self.enoncefich + str(line) + '\n'

        return self.enoncefich

    def lirecont5lignes(self):
        """Permet de récupérer les 5 premières lignes du contenu de la note."""

        contenu5 = ""
        cont5 = self.listfich_nom[self.nomfich]
        index1 = (cont5.index(utl.textsoluce) + 1)  # indice du début du code dans la liste
        index2 = index1 + 5
        texte = (cont5[index1: index2])             # le texte est compris entre énoncé et code en list
        for line in texte:
            contenu5 = contenu5 + str(line) + '\n'
        return contenu5

    def lirecont10lignes(self):
        """Permet de récupérer les 10 premières lignes du contenu de la note."""

        cont10 = self.listfich_nom[self.nomfich]
        index1 = (cont10.index(utl.textsoluce) + 1)
        index2 = index1 + 10
        texte = (cont10[index1: index2])
        contenu10 = ""
        for line in texte:
            contenu10 = contenu10 + str(line) + '\n'
        return contenu10

    def lireconttout(self):
        """Permet de récupérer tout le contenu de la note."""

        cont = self.listfich_nom[self.nomfich]
        index1 = (cont.index(utl.textsoluce) + 1)
        texte = (cont[index1: (len(cont))])
        contenufich = ""
        for line in texte:
            contenufich = contenufich + str(line) + '\n'
        return contenufich

    def modficherefaire(self):
        """Modification d'une fiche reussi en à refaire."""

        # Je veux récupérer chemin et le nom de la fiche à modifier.
        self.chfich = os.path.join(utl.dosdata, self.nomfich + '.txt')
        self.listfich_nom[self.nomfich][2] = '# Réussite : non'
        contenu = ""
        # puis je veux entrer dans cette fiche pour la modifier
        for i in self.listfich_nom.get(self.nomfich):
            # changer le contenu
            contenu = contenu + i + "\n"
        with open(self.chfich, 'w') as f:
            f.write(contenu)

    def modfichereussi(self):
        """Modification d'une fiche à refaire ne fiche réussie."""

        # Je veux récupérer chemin et le nom de la fiche à modifier.
        self.chfich = os.path.join(utl.dosdata, self.nomfich + '.txt')
        self.listfich_nom[self.nomfich][2] = '# Réussite : ok'
        contenu = ""
        # puis je veux entrer dans cette fiche pour la modifier
        for i in self.listfich_nom.get(self.nomfich):
            # changer le contenu
            contenu = contenu + i + "\n"
        with open(self.chfich, 'w') as f:
            f.write(contenu)

    def creationfich(self):
        """Fonction permettant de créer une fiche d'exercice à partir des données de la fonction donneescreatfich."""

        self.chfich = os.path.join(utl.dosdata, self.nomfich + '.txt')
        with open(self.chfich, 'w') as f:
            f.write(self.contenu)

    def suppressionfich(self):
        """Fonction permettant la suppression d'une fiche."""

        os.remove(self.chfich)

    def statfich(self):
        """Calcul pour déterminer le taux de réussite des fiches."""

        # Calcul pour la progressbar
        compte_A, compte_B = (len(self.fiches_reussi)), (len(self.fiches_afaire))
        if compte_A == 0:
            self.compte_C = 0
        else:
            self.compte_C = ((float(compte_A)) / (compte_A + compte_B)) * 100

        return self.compte_C