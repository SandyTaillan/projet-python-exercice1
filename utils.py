#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from glob import glob

chbase = os.path.dirname(__file__)
dosdata = os.path.join(chbase, 'data')
listfiches = sorted(glob(dosdata + '/*.txt'))
#niveaudeb = '# Niveau : débutant'
textenonce = '# Enoncé :'
textsoluce = '# Solution : '