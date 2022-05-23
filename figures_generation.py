#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:00:09 2022

@author: mauricio
"""
import numpy as np
from matplotlib import pyplot as plt
import os
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter


os.chdir('/home/mocelim/Documents/grace_jscatter')
 
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

x = []
y = []
for line in open('teste.dat', 'r'):
    lines = [i for i in line.split()]
    x.append(float(lines[0]))
    y.append(float(lines[8]))
    
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


plt.xticks(np.arange(0, len(x)+1, 2.5))
plt.yticks(np.arange(0, max(y), 0.25))


plt.xlabel('Weighted')
plt.ylabel('ECN')
plt.plot(x, y, c = 'r', marker= '.', linestyle=' ', label='ECN')
plt.legend(loc='best', fontsize='x-large', edgecolor="black", framealpha=1, fancybox=False)

plt.tick_params(axis="y",direction="in",length=10)
plt.tick_params(axis="x",direction="in", length=10)





plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")


plt.show()



  


