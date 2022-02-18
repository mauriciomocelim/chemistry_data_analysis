#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:38:59 2022

@author: mauricio
"""

import subprocess
import time
import os

folder = r"/home/mauricio/Downloads/script_cg_xyz"
old_name=os.listdir(folder)
for name in old_name:
    if name.endswith(".xyz"):
        aux = name
        new_name = 'vesta.xyz'
        os.rename(name, new_name)
        subprocess.Popen('./vesta_cg_cluster_3.x')
        time.sleep(2)
        os.rename('vesta_cg.xyz', aux)
os.remove('vesta.xyz')
os.remove('geometry_cg.in')