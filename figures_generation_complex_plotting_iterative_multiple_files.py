#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:00:09 2022

@author: mauricio
"""
import numpy as np
import os
from pathlib import Path
from matplotlib import pyplot as plt
import os
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter

os.chdir('/home/mocelim/Documents/teste')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = '14'

files_list=os.listdir('/home/mocelim/Documents/teste')

for filename in files_list: 
    with open(filename, 'r') as f:
        aux=f.readlines()
        x = []
        y = []
        z = []
        a = []    
        for line in aux[3:]:
            lines = [i for i in line.split()]
            x.append(float(lines[0]))
            y.append(float(lines[2]))
            z.append(float(lines[3]))
            a.append(float(lines[4]))
        
    fig, ax = plt.subplots()
    
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    
    ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()
    ax.xaxis.set_tick_params(which='minor',  direction='in', length=5,top=True)
    ax.yaxis.set_tick_params(which='minor',  direction='in', length=5,right=True)
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(labeltop=False, labelright=False)
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    
    
    plt.xticks(np.arange(0, len(x)+1, 2))
    plt.yticks(np.arange(5, max(y), 20))
    
    
    plt.xlabel('Distance (Å)')
    plt.ylabel('g(r)')
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.plot(x, y,c = 'k', marker= '', linestyle='solid', label='Ce')
    plt.plot(x, z,c = 'r', marker= '', linestyle='dotted', label='La')
    plt.plot(x, a,c = 'b', marker= '', linestyle='dashed', label='O')
    plt.legend(loc='best', fontsize='x-large', edgecolor="black", framealpha=1, fancybox=False)
    
    plt.tick_params(axis="y",direction="in",length=10)
    plt.tick_params(axis="x",direction="in", length=10)
    
    
    
    plot_filename = '{}_plot.pdf'.format(filename)
    plt.savefig(plot_filename, format="pdf")
            
    
    

