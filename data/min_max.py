#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Challenge # 4 Min or Max : 

# Notions abordées 
# - Boucle 
# - Conditions 

# Énoncé
# Garde forestier dans les merveilleuses plaines du Wyoming on vous 
# demande de recenser chaque arbre par la taille et ainsi trouver le 
# plus grand et le plus petit arbre.

#MIN

#Input : [7, 9, 10, 1, 2, 18]
#Output : 1 

#MAX

#Input : [7, 9, 10, 1, 2, 18] 
#Output : 18

malist = [7, 9, 10, 1, 2, 18]

malist.sort()
print(malist[0])
print(malist[-1])
	
