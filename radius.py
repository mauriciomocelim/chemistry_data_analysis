#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:03:17 2022

@author: mocelim
"""

from ase.io import read, write
from pathlib import Path
import ase
import subprocess
import time
import math
import statistics
import numpy as np
from ase import Atoms
from ase.io import read, vasp
import os

#xyz files must be with cg at origin. 

#center of gravity at origin 
folder = list(Path('/home/mocelim/Documents/teste').rglob('vesta.xyz'))
for name in folder:
    aux=os.path.basename(name)
    os.chdir(name.parent) 
    atoms = read('vesta.xyz')
    atoms.center(vacuum=None,axis=(0, 1, 2),about=(0))
    ase.io.write('vesta.xyz', atoms)   

#calculating R and D --> R=\frac{(R_1 + \frac{D}{2})}{2}
#calculating R and D only requires the bigger distance between c.g. and a surface atom and the biggest distance between two surface atoms. 

#Calculating R_1
os.chdir('/home/mocelim/Documents/teste')
with open('distances_from_cg', 'r') as f: 
    x=[]
    file = f.readlines()
    for line in file:
        lines = [i for i in line.split()]
        x.append(float(lines[0]))
        x.sort()
#Calculating D
file_name = 'vesta.xyz'
my_file = open(file_name)
str_list = my_file.readlines()
my_file.close()
filefile = read(file_name)
data=filefile.get_all_distances()
file = open("all_distances", "w")
for row in data:
    np.savetxt(file, row)
file.close
with open('all_distances', 'r') as f1: 
    y=[]
    file1 = f1.readlines()
    for line1 in file1:
        lines1 = [i for i in line1.split()]
        y.append(float(lines1[0]))
        y.sort()

R=(x[-1] + (y[-1]/2))/2
print(R)
    
        
        

