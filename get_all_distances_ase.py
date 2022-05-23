#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:35:02 2020

@author: albert

"""
import numpy as np
import subprocess
import time
from ase import Atoms
from ase.io import read, vasp
import os


file_name = 'vesta.xyz'
my_file = open(file_name)
str_list = my_file.readlines()
my_file.close()

    
filefile = read(file_name)
data=filefile.get_all_distances()
print(data)

file = open("car.txt", "w")
for row in data:
    np.savetxt(file, row)
file.close
