#!/usr/bin/env python
# -*- coding: utf-8 -

# on va toucher aux fichiers de système d'exploitation,
#               => On va donc importer le module os
import os
from glob import glob

class Fiche(object):
    """Cette classe regroupe toutes les opérations à effectuer sur les fiches."""
    def __init__(self, nomfich):

        self.nomfich = nomfich

        # déclaration des variables

        niveauint = '# Niveau : intermédiaire'
        niveauexp = '# Niveau : expert'

        # variable de test
        interniveau = 'Niveau : débutant'

    def dossierdata(self):
        """Vérification si le dossier data existe et je le crée s'il n'existe pas
            idem pour le fichier de départ."""

        # Vérifier si le dossier existe.
        if not os.path.exists(self.dosdata):
            # je crée le dossier et du même coup le fichier de départ aussi
            os.makedirs(self.dosdata)
        if not os.path.isfile(self.dosdata + '/' + self.nomfich + '.txt'):
            self.creafichinit()

    def creafichinit(self):
        """Vérification de l'existence de la fiche initial. Sinon, on l'a crée."""

        if not os.path.isfile(self.dosdata + '/' + self.nomfich + '.txt'):
            self.contenufich = self.niveaudeb + ('\n' * 2) + self.textenonce + ('\n' * 2) + self.textsoluce + ('\n' * 2)
            with open((self.dosdata + '/' + self.nomfich + '.txt'), 'w') as f:
                f.write(self.contenufich)

    def liredosfich(self):
        """Lit le nom des fiches dans le dossier data et les places dans une liste."""

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



    def lirecontfich(self):
        with open(self.chfich, 'r') as f:  # pour ouvrir la fiche
            contenufich = f.read().splitlines()  # on met le contenu dans une liste par ligne
            print(contenufich)

    def lirenoncefich(self):
        """Lire l'énoncé de l'exercice dans le fichier d'exercice."""

        with open((self.dosdata + '/' + self.nomfich + '.txt'), 'r') as f:

            self.contenonce = f.read().splitlines()  # on met le contenu dans une liste par ligne
            index1 = self.contenonce.index(self.textenonce)  # indice du début de l'énoncé dans la liste
            index2 = self.contenonce.index(self.textsoluce)  # indice de fin de l'énoncé dans la liste
            texte = (self.contenonce[index1: index2])  # le texte est compris entre énoncé et code en liste
            self.enoncefich = ""  # transformation de la liste en string
            for line in texte:
                self.enoncefich = self.enoncefich + str(line) + '\n'
            return self.enoncefich
