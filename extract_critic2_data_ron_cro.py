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

folder = list(Path('/home/mocelim/Documents/inputs_md_kmeans_structures_selected').rglob('run.cro'))
for name in folder:
    aux=os.path.basename(name)  #basename pega o nome do arquivo e não o nome do caminho todo.
    os.chdir(name.parent)  #pega o diretório e nao o arquivo POSCAR-->vai sempre indo na pasta anterior
    subprocess.call("awk '/La -> La/{print $4,$5,$6,$9}' run.cro >bond_lenghtsLa_La", shell=True)
    time.sleep(0.1)
    subprocess.call("awk '/Ce -> Ce/{print $4,$5,$6,$9}' run.cro >bond_lenghtsCe_Ce", shell=True)
    time.sleep(0.1)
    subprocess.call("awk '/O -> O/{print $4,$5,$6,$9}' run.cro >bond_lenghtsO_O", shell=True)
    time.sleep(0.1)
    subprocess.call("awk '/Ce -> La/{print $4,$5,$6,$9}''/La -> Ce/{print $4,$5,$6,$9}' run.cro >bond_lenghtsCe_La", shell=True)
    time.sleep(0.1)
    subprocess.call("awk '/O -> La/{print $4,$5,$6,$9}''/La -> O/{print $4,$5,$6,$9}' run.cro >bond_lenghtsLa_O", shell=True)
    time.sleep(0.1)
    subprocess.call("awk '/O -> Ce/{print $4,$5,$6,$9}''/Ce -> O/{print $4,$5,$6,$9}' run.cro >bond_lenghtsCe_O", shell=True)
    time.sleep(0.5)