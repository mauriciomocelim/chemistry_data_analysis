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
import math

folder = list(Path('/home/mocelim/Documents/md_structures_analysis').rglob('vacancy_histogram_distances_from_cg'))
for name in folder:
    aux=os.path.basename(name) 
    os.chdir(name.parent)  
    with open(aux, 'r') as f: 
        file = f.readlines()
    with open(aux,  'w') as f:
        for line in file:
            line = line.split()
            x=float(line[1])
            y=float(line[2])
            z=float(line[3])
            distance = math.sqrt((x**2+y**2+z**2))
            f.write('{}\n'.format(distance))
            
    
           
    
        
        


        
