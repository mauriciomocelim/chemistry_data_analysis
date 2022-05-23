#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:38:59 2022

@author: mauricio
"""

import subprocess
import time
import os
from pathlib import Path

folder = list(Path('/home/mocelim/Documents/teste').rglob('POSCAR'))
for name in folder:
    aux=os.path.basename(name)  #basename pega o nome do arquivo e não o nome do caminho todo.
    os.chdir(name.parent)  #pega o diretório e nao o arquivo POSCAR-->vai sempre indo na pasta anterior
    subprocess.call('/home/mocelim/Downloads/.critic2/critic2/build/src/critic2 run.cri run.cro', shell=True)
    time.sleep(1)