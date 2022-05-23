import numpy as np
import os
from pathlib import Path
from matplotlib import pyplot as plt
import os
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = '12'


os.chdir('/home/mocelim/Documents/teste')
filelist=os.listdir('/home/mocelim/Documents/teste')



with open(filelist[0], 'r') as f: 
    aux=f.readlines() 
    a = []
    b = []
    for line in aux:
        lines = [i for i in line.split()]
        a.append(float(lines[0]))
        b.append(float(lines[1]))
with open(filelist[1], 'r') as f: 
    aux=f.readlines() 
    m = []
    n = []
    for line in aux:
        lines = [i for i in line.split()]
        m.append(float(lines[0]))
        n.append(float(lines[1]))
        
fig, axs = plt.subplots(2, sharex=False)
axs[0].plot(a, b, marker= '.', linestyle='', c='k', label='1')
axs[1].plot(m, n, marker= '.', linestyle='', c='r', label='2')


for ax in axs:
    ax.tick_params(direction='in', bottom=True, top=True, left=True, right=True, length=8)
    ax.tick_params(which='minor',  direction='in', length=4, top=True, right=True)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.yaxis.get_ticklocs(minor=True)
    ax.xaxis.get_ticklocs(minor=True)
    ax.minorticks_on
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.legend(loc='best', fontsize='medium', edgecolor="black", framealpha=1, fancybox=False)
    ax.xaxis.set_ticks(np.arange(0, 4, 1))
    ax.yaxis.set_ticks(np.arange(2, 6, 1))
    



fig.text(0.5, 0.02, 'Distance (Å)', ha='center')
fig.text(0.05, 0.4, 'XXXXXXXX', ha='center', rotation=90)

plot_filename = 'teste'
plt.savefig(plot_filename, format="pdf")


       
        
