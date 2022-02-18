#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:23:30 2022

@author: mauricio
"""
# =============================================================================
# ctrl + 4 comments all selected lines
# =============================================================================

import os
import shutil

# =============================================================================
# creates directories
# =============================================================================
root_path = '/home/mauricio/Documents/INPUTS_MD_KMEANS_STRUCTURES'
  
def createDirectories(number=10, name='Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_'):
    i=1
    for i in range(number):
        os.mkdir(name+"%02d" % (i))
    i+=1
os.chdir('/home/mauricio/Documents')
createDirectories()
createDirectories(10,'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_')
createDirectories(10,'La40O60_paw_pbe+u_1.125enmax_1kd_opt_')
createDirectories(10, 'La72O108_paw_pbe+u_1.125enmax_1kd_opt_')
createDirectories(10, 'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_')
createDirectories(10, 'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_')
    
# =============================================================================
#copying job,kpoints, potcar and INCAR to all directories
#requires a folder with the inputs and a folder for creating subdirectories
# =============================================================================
os.chdir('/home/mauricio/Documents/INPUTS_MD_KMEANS_STRUCTURES')
src='/home/mauricio/Documents/inputs1'
src_files = os.listdir(src)
for directory in os.listdir(root_path):
    aux=directory
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy(full_file_name, aux)


