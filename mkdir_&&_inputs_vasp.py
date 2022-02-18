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
  
list = ['Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_01','Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_02',
        'Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_03','Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_04',
        'Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_05','Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_06',
        'Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_07','Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_08',
        'Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_09','Ce40O80_paw_pbe+u_1.125enmax_1kd_opt_10',
        'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_01','Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_02',
        'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_03','Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_04',
        'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_05','Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_06',
        'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_07','Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_08',
        'Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_09','Ce72O144_paw_pbe+u_1.125enmax_1kd_opt_10',
        'La40O60_paw_pbe+u_1.125enmax_1kd_opt_01','La40O60_paw_pbe+u_1.125enmax_1kd_opt_02',
        'La40O60_paw_pbe+u_1.125enmax_1kd_opt_03','La40O60_paw_pbe+u_1.125enmax_1kd_opt_04',
        'La40O60_paw_pbe+u_1.125enmax_1kd_opt_05','La40O60_paw_pbe+u_1.125enmax_1kd_opt_06',
        'La40O60_paw_pbe+u_1.125enmax_1kd_opt_07','La40O60_paw_pbe+u_1.125enmax_1kd_opt_08',
        'La40O60_paw_pbe+u_1.125enmax_1kd_opt_09','La40O60_paw_pbe+u_1.125enmax_1kd_opt_10',
        'La72O108_paw_pbe+u_1.125enmax_1kd_opt_01','La72O108_paw_pbe+u_1.125enmax_1kd_opt_02',
        'La72O108_paw_pbe+u_1.125enmax_1kd_opt_03','La72O108_paw_pbe+u_1.125enmax_1kd_opt_04',
        'La72O108_paw_pbe+u_1.125enmax_1kd_opt_05','La72O108_paw_pbe+u_1.125enmax_1kd_opt_06',
        'La72O108_paw_pbe+u_1.125enmax_1kd_opt_07','La72O108_paw_pbe+u_1.125enmax_1kd_opt_08',
        'La72O108_paw_pbe+u_1.125enmax_1kd_opt_09','La72O108_paw_pbe+u_1.125enmax_1kd_opt_10',
        'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_01','Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_02',
        'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_03','Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_04',
        'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_05','Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_06',
        'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_07','Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_08',
        'Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_09','Ce20La20O70_paw_pbe+u_1.125enmax_1kd_opt_10',
        'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_01','Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_02',
        'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_03','Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_04',
        'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_05','Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_06',
        'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_07','Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_08',
        'Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_09','Ce36La36O126_paw_pbe+u_1.125enmax_1kd_opt_10']
  
for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)
    
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


