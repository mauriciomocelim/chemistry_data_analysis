import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
import os
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
import pandas as pd

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = '12'
plt.rcParams['figure.figsize'] = [8, 11.5]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['agg.path.chunksize'] = 10000


os.chdir('/home/mocelim/Documents/teste')
filelist=os.listdir('/home/mocelim/Documents/teste')

with open('1', 'r') as f: 
    aux=f.readlines() 
    a = []
    b = []
    for line in aux:
        lines = [i for i in line.split()]
        a.append(float(lines[0]))
        b.append(float(lines[1]))
with open('2', 'r') as f: 
    aux=f.readlines() 
    c = []
    d = []
    for line in aux:
        lines = [i for i in line.split()]
        c.append(float(lines[0]))
        d.append(float(lines[1]))
with open('3', 'r') as f: 
    aux=f.readlines() 
    e = []
    f1 = []
    for line in aux:
        lines = [i for i in line.split()]
        e.append(float(lines[0]))
        f1.append(float(lines[1]))
with open('4', 'r') as f: 
    aux=f.readlines() 
    g = []
    h = []
    for line in aux:
        lines = [i for i in line.split()]
        g.append(float(lines[0]))
        h.append(float(lines[1]))
with open('5', 'r') as f: 
    aux=f.readlines() 
    i = []
    j = []
    for line in aux:
        lines = [i for i in line.split()]
        i.append(float(lines[0]))
        j.append(float(lines[1]))
with open('6', 'r') as f: 
    aux=f.readlines() 
    k = []
    l = []
    for line in aux:
        lines = [i for i in line.split()]
        k.append(float(lines[0]))
        l.append(float(lines[1]))

df1 = pd.DataFrame(a).rolling(200).mean().values.tolist()
df2 = pd.DataFrame(b).rolling(200).mean().values.tolist()
df3 = pd.DataFrame(c).rolling(200).mean().values.tolist()
df4 = pd.DataFrame(d).rolling(200).mean().values.tolist()
df5 = pd.DataFrame(e).rolling(200).mean().values.tolist()
df6 = pd.DataFrame(f1).rolling(200).mean().values.tolist()

df7 = pd.DataFrame(g).rolling(200).mean().values.tolist()
df8 = pd.DataFrame(h).rolling(200).mean().values.tolist()
df9 = pd.DataFrame(i).rolling(200).mean().values.tolist()
df10 = pd.DataFrame(j).rolling(200).mean().values.tolist()
df11 = pd.DataFrame(k).rolling(200).mean().values.tolist()
df12 = pd.DataFrame(l).rolling(200).mean().values.tolist()


fig, axs = plt.subplots(3,2, sharex=True, sharey=False)
axs[0,0].plot(a, b, marker= '', linestyle='-', c='k', label='$Ce_{40}O_{80}$')
axs[0,1].plot(c, d, marker= '', linestyle='-', c='r', label='$La_{40}O_{60}$')
axs[1,0].plot(e, f1, marker= '', linestyle='-', c='b', label='$Ce_{20}La_{20}O_{70}$')
axs[1,1].plot(g, h, marker= '', linestyle='-', c='k', label='$Ce_{72}O_{144}$')
axs[2,0].plot(i, j, marker= '', linestyle='-', c='r', label='$La_{72}O_{108}$')
axs[2,1].plot(k, l, marker= '', linestyle='-', c='b', label='$Ce_{36}La_{36}O_{126}$')
axs[0,0].plot(df1, df2, marker= '', linestyle='-', c='g', label='Average')
axs[0,1].plot(df3, df4, marker= '', linestyle='-', c='g', label='Average')
axs[1,0].plot(df5, df6, marker= '', linestyle='-', c='g', label='Average')
axs[1,1].plot(df7, df8, marker= '', linestyle='-', c='g', label='Average')
axs[2,0].plot(df9, df10, marker= '', linestyle='-', c='g', label='Average')
axs[2,1].plot(df11, df12, marker= '', linestyle='-', c='g', label='Average')


plt.subplots_adjust(wspace=0.25, hspace=0.05)

for ax in axs.flat:
    ax.tick_params(direction='in', bottom=True, top=True, left=True, right=True, length=8)
    ax.tick_params(which='minor',  direction='in', length=4, top=True, right=True)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.yaxis.get_ticklocs(minor=True)
    ax.xaxis.get_ticklocs(minor=True)
    ax.minorticks_on
    ax.legend(loc='best', edgecolor="k", framealpha=0, fancybox=False, borderpad=0.2, handletextpad=0.25, handlelength=1)
    ax.locator_params(axis='y', nbins=4)
    ax.locator_params(axis='x', nbins=5)  
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    
fig.text(0.3, 0.075, 'Temperature (K)', ha='center')
fig.text(0.725, 0.075, 'Temperature (K)', ha='center')
fig.text(0.05, 0.425, 'Potential Energy (eV)', ha='center', rotation=90)


plt.savefig('all_structures_pe_temperature.png', bbox_inches='tight')

