#!/usr/bin/env python
# -*- coding: utf-8 -*-


# on va toucher aux fichiers de système d'exploitation,
#               => On va donc importer le module os
import os
from glob import glob


class Fiche(object):
    """Cette classe regroupe toutes les opérations à effectuer sur les fiches."""
    def __init__(self, nomfich):

        self.nomfich = nomfich

    def liredosfich(self):
        """Lit le nom des fiches dans le dossier data et les place dans une liste."""

        self.listfiches = glob(self.dosdata + '/*.txt')                                              # permet de récupérer tous les fichiers de type .txt
        self.listfiches = [os.path.splitext(os.path.split(n)[-1])[0] for n in self.listfiches]      # va nous permettre de récupérer juste le nom du fichier dans le chemin
        return self.listfiches

    def liredosfichselection(self):

        self.listfiches = glob(self.dosdata + '/*.txt')
        for i in self.listfiches:
            with open((i), 'r') as f:
                self.contenonce = f.read().splitlines()  # on met le contenu dans une liste par ligne
                if self.contenonce[0] == self.niveaudeb:
                    self.nomfich = os.path.splitext(os.path.split(i)[-1])[0]
                    self.listfichselect.append(self.nomfich)
        return self.listfichselect

    def lirenoncefich(self):
        """Lire l'énoncé de l'exercice dans le fichier d'exercice."""

        with open((self.dosdata + '/' + self.nomfich + '.txt'), 'r') as f:
            self.contenonce = f.read().splitlines()  # on met le contenu dans une liste par ligne
            index1 = self.contenonce.index(self.textenonce)  # indice du début de l'énoncé dans la liste
            index2 = self.contenonce.index(self.textsoluce)  # indice de fin de l'énoncé dans la liste
            texte = (self.contenonce[(index1 +1): index2])  # le texte est compris entre énoncé et code en liste
            self.enoncefich = ""  # transformation de la liste en string
            for line in texte:
                self.enoncefich = self.enoncefich + str(line) + '\n'
            return self.enoncefich

    def lirecont5lignes(self):
        """Permet de récupérer 5 lignes du contenu de la note"""

        with open((self.dosdata + '/' + self.nomfich + '.txt'), 'r') as f:
            cont5 = f.read().splitlines()                  # on met le contenu dans une liste par ligne                                       # on met le contenu dans une variable
            index1 = (cont5.index(self.textsoluce) + 1)                # indice du début du code dans la liste
            index2 = index1 + 5
            texte = (cont5[index1: index2])                # le texte est compris entre énoncé et code en liste
            contenu5 = ""                                    # transformation de la liste en string
            for line in texte:
                contenu5 = contenu5 + str(line) + '\n'
        return contenu5                                     # on retourne le contenu de la variable

    def lirecont10lignes(self):
        """Permet de récupérer  10 lignes du contenu de la note"""

        with open((self.dosdata + '/' + self.nomfich + '.txt'), 'r') as f:
            cont10 = f.read().splitlines()  # on met le contenu dans une liste par ligne                                       # on met le contenu dans une variable
            index1 = (cont10.index(self.textsoluce) + 1)  # indice du début du code dans la liste
            index2 = index1 + 10
            texte = (cont10[index1: index2])  # le texte est compris entre énoncé et code en liste
            contenu10 = ""  # transformation de la liste en string
            for line in texte:
                contenu10 = contenu10 + str(line) + '\n'
        return contenu10  # on retourne le contenu de la variable

    def lireconttout(self):
        """Permet de récupérer  tout le contenu de la note"""

        with open((self.dosdata + '/' + self.nomfich + '.txt'), 'r') as f:
            cont = f.read().splitlines()                   # on met le contenu dans une variable
            index1 = (cont.index(self.textsoluce) + 1)
            texte = (cont[index1: (len(cont))])
            contenufich = ""  # transformation de la liste en string
            for line in texte:
                contenufich = contenufich + str(line) + '\n'
        return contenufich  # on retourne le contenu de la variable

    def creationfich(self):
        """Fonction permettant de créer une fiche d'exercice à partir des données de la fonction donneescreatfich."""

        self.chfich = os.path.join(self.dosdata, self.nomfich + '.txt')

        with open(self.chfich, 'w') as f:
            f.write(self.contenu)

    def suppressionfich(self):
        """Fonction permettant la suppression d'une fiche."""

        os.remove(self.chfich)
