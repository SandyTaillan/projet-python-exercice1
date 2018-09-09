#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import utils as utl
from glob import glob


class GestionFiche(object):
    """Cette classe regroupe toutes les opérations à effectuer sur les fiches. """

    def __init__(self):
        """Initialisation des variables liées aux fiches.

        :param self.dict_fich: Contient tous les nons des fiches ainsi que tout leur contenus
        :type self.dict_fich: dict

        """
        self.dictnom_fich = {}
        self.enoncefich = ""
        self.nomfich = ""
        self.chfich = ""
        self.compte_tot = 0
        self.choix = ""
        self.fiches_selection = []
        self.listscore = []
        self.compte_a = 0
        self.compte_b = 0
        self.contenu = ""

    def liredosfich(self):
        """Lit le nom des fiches dans le dossier data ainsi que leur contenu et les place dans un dictionnaire."""

        # déclaration des variables
        listfiches = sorted(glob(utl.dosdata + '/*.txt'))
        liste_de_fiches = []
        listcontfich = []

        # liste de nom des fichiers que je place dans une liste (listes_de_fiches)
        for chemin in listfiches:
            liste_de_fiches.append(os.path.splitext(os.path.split(chemin)[-1])[0])

        # je récupère le contenu des fiches que je mets dans une liste.
            with open(chemin, 'r') as f:
                cont_fich = f.read().splitlines()
                listcontfich.append(cont_fich)

        # Pour travailler, j'aurais besoin de coupler ces deux listes dans un dictionnaire.
        # la ligne suivante me permet de mettre dans un dictionnaire le nom des fiches avec leur contenu respectif
        self.dictnom_fich = {x: y for x, y in zip(liste_de_fiches, listcontfich)}

    def statfichglob(self):
        """Calcul pour déterminer le taux de réussite des fiches."""

        self.compte_a = 0
        self.compte_b = 0

        # 1er cas : stat globale
        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.compte_a += 1
            else:
                self.compte_b += 1
        if self.compte_a == 0:
            self.compte_tot = 0
        else:
            self.compte_tot = ((float(self.compte_a)) / (self.compte_a + self.compte_b)) * 100
        return self.compte_tot

    def statfichdeb(self):
        """Calcul pour déterminer le taux de réussite des fiches."""

        self.compte_a = 0
        self.compte_b = 0

        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][1] == '# Niveau : débutant' and self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.compte_a += 1
            else:
                self.compte_b += 1
        if self.compte_a == 0:
            self.compte_tot = 0
        else:
            self.compte_tot = ((float(self.compte_a)) / (self.compte_a + self.compte_b)) * 100
        return self.compte_tot

    def statfichinterm(self):
        """Calcul pour déterminer le taux de réussite des fiches."""

        self.compte_a = 0
        self.compte_b = 0

        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][1] == '# Niveau : intermédiaire' \
                    and self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.compte_a += 1
            else:
                self.compte_b += 1
        if self.compte_a == 0:
            self.compte_tot = 0
        else:
            self.compte_tot = ((float(self.compte_a)) / (self.compte_a + self.compte_b)) * 100
        return self.compte_tot

    def statfichexpert(self):
        """Calcul pour déterminer le taux de réussite des fiches."""

        self.compte_a = 0
        self.compte_b = 0

        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][1] == '# Niveau : expert' and self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.compte_a += 1
            else:
                self.compte_b += 1
        if self.compte_a == 0:
            self.compte_tot = 0
        else:
            self.compte_tot = ((float(self.compte_a)) / (self.compte_a + self.compte_b)) * 100
        return self.compte_tot

    def fich_cas_a(self):

        for nom in (sorted(self.dictnom_fich.keys())):
            self.fiches_selection.append(nom)
            if self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.listscore.append("ok")
                self.compte_a += 1
            else:
                self.listscore.append("X")
                self.compte_b += 1
        return self.fiches_selection, self.listscore

    def fich_cas_b(self):

        self.compte_a = 0
        self.compte_b = 0
        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.fiches_selection.append(nom)
                self.listscore.append('ok')
        return self.fiches_selection, self.listscore

    def fich_cas_c(self):

        self.compte_a = 0
        self.compte_b = 0
        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][2] == '# Réussite : non':
                self.fiches_selection.append(nom)
                self.listscore.append('X')
        return self.fiches_selection, self.listscore

    def fich_cas_d(self):

        self.compte_a = 0
        self.compte_b = 0
        for nom in (sorted(self.dictnom_fich.keys())):
            if self.dictnom_fich[nom][1] == '# Niveau : débutant':
                self.fiches_selection.append(nom)
                if self.dictnom_fich[nom][2] == '# Réussite : ok':
                    self.listscore.append("ok")
                else:
                    self.listscore.append("X")
        return self.fiches_selection, self.listscore

    def fich_cas_e(self):

        self.compte_a = 0
        self.compte_b = 0
        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : débutant' and self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.fiches_selection.append(nom)
                self.listscore.append('ok')
        return self.fiches_selection, self.listscore

    def fich_cas_f(self):

        self.compte_a = 0
        self.compte_b = 0
        for nom in self.dictnom_fich.keys():
                if self.dictnom_fich[nom][1] == '# Niveau : débutant'\
                        and self.dictnom_fich[nom][2] == '# Réussite : non':
                    self.fiches_selection.append(nom)
                    self.listscore.append("X")
        return self.fiches_selection, self.listscore

    def fich_cas_g(self):

        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : intermédiaire':
                self.fiches_selection.append(nom)
                if self.dictnom_fich[nom][2] == '# Réussite : ok':
                    self.listscore.append("ok")
                else:
                    self.listscore.append("X")
        return self.fiches_selection, self.listscore

    def fich_cas_h(self):

        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : intermédiaire' and \
                    self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.fiches_selection.append(nom)
                self.listscore.append("ok")
        return self.fiches_selection, self.listscore

    def fich_cas_i(self):

        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : intermédiaire' and \
                    self.dictnom_fich[nom][2] == '# Réussite : non':
                self.fiches_selection.append(nom)
                self.listscore.append("X")
        return self.fiches_selection, self.listscore

    def fich_cas_j(self):

        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : expert':
                self.fiches_selection.append(nom)
                if self.dictnom_fich[nom][2] == '# Réussite : ok':
                    self.listscore.append("ok")
                else:
                    self.listscore.append("X")
        return self.fiches_selection, self.listscore

    def fich_cas_k(self):

        for nom in self.dictnom_fich.keys():
            if self.dictnom_fich[nom][1] == '# Niveau : expert' and self.dictnom_fich[nom][2] == '# Réussite : ok':
                self.fiches_selection.append(nom)
                self.listscore.append("ok")
        return self.fiches_selection, self.listscore

    def fich_cas_l(self):

        for nom in self.dictnom_fich .keys():
            if self.dictnom_fich[nom][1] == '# Niveau : expert' and self.dictnom_fich[nom][2] == '# Réussite : non':
                self.fiches_selection.append(nom)
                self.listscore.append("X")
        return self.fiches_selection, self.listscore

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
        enonce = self.dictnom_fich[self.nomfich]
        index1 = enonce.index(utl.textenonce)
        index2 = enonce.index(utl.textsoluce)
        texte = (enonce[(index1 + 1): index2])  # le texte est compris entre énoncé et code en liste
        for line in texte:
            self.enoncefich = self.enoncefich + str(line) + '\n'

        return self.enoncefich

    def lirecont5lignes(self):
        """Permet de récupérer les 5 premières lignes du contenu de la note."""

        contenu5 = ""
        cont5 = self.dictnom_fich[self.nomfich]
        index1 = (cont5.index(utl.textsoluce) + 1)  # indice du début du code dans la liste
        index2 = index1 + 5
        texte = (cont5[index1: index2])             # le texte est compris entre énoncé et code en list
        for line in texte:
            contenu5 = contenu5 + str(line) + '\n'
        return contenu5

    def lirecont10lignes(self):
        """Permet de récupérer les 10 premières lignes du contenu de la note."""

        cont10 = self.dictnom_fich[self.nomfich]
        index1 = (cont10.index(utl.textsoluce) + 1)
        index2 = index1 + 10
        texte = (cont10[index1: index2])
        contenu10 = ""
        for line in texte:
            contenu10 = contenu10 + str(line) + '\n'
        return contenu10

    def lireconttout(self):
        """Permet de récupérer tout le contenu de la note."""

        cont = self.dictnom_fich[self.nomfich]
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
        self.dictnom_fich[self.nomfich][2] = '# Réussite : non'
        contenu = ""
        # puis je veux entrer dans cette fiche pour la modifier
        for i in self.dictnom_fich.get(self.nomfich):
            # changer le contenu
            contenu = contenu + i + "\n"
        with open(self.chfich, 'w') as f:
            f.write(contenu)

    def modfichereussi(self):
        """Modification d'une fiche à refaire ne fiche réussie."""

        # Je veux récupérer chemin et le nom de la fiche à modifier.
        self.chfich = os.path.join(utl.dosdata, self.nomfich + '.txt')
        self.dictnom_fich[self.nomfich][2] = '# Réussite : ok'
        contenu = ""
        # puis je veux entrer dans cette fiche pour la modifier
        for i in self.dictnom_fich.get(self.nomfich):
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
