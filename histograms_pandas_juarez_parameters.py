import numpy as np
import pandas as pd
import os
from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.ticker import FormatStrFormatter
from matplotlib import colors


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = '14'
plt.rcParams['figure.figsize'] = [8, 11.5]

os.chdir('/home/mocelim/Documents/teste')
filelist=os.listdir('/home/mocelim/Documents/teste')


with open('teste1', 'r') as f: 
    aux=f.readlines() 
    a = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        a.append(float(lines[3]))
with open('teste2', 'r') as f: 
    aux=f.readlines() 
    b = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        b.append(float(lines[3]))
with open('teste3', 'r') as f: 
    aux=f.readlines() 
    c = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        c.append(float(lines[3]))
with open('teste4', 'r') as f: 
    aux=f.readlines() 
    d = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        d.append(float(lines[3]))
with open('teste5', 'r') as f: 
    aux=f.readlines() 
    e = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        e.append(float(lines[3]))
with open('teste6', 'r') as f: 
    aux=f.readlines() 
    f1 = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        f1.append(float(lines[3]))
with open('teste7', 'r') as f: 
    aux=f.readlines() 
    g = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        g.append(float(lines[3]))
with open('teste8', 'r') as f: 
    aux=f.readlines() 
    h = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        h.append(float(lines[3]))
with open('teste9', 'r') as f: 
    aux=f.readlines() 
    i = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        i.append(float(lines[3]))
with open('teste10', 'r') as f: 
    aux=f.readlines() 
    j = []
    for line in aux[1:]:
        lines = [i for i in line.split()]
        j.append(float(lines[3]))
        
df1 = pd.DataFrame(a)
df2 = pd.DataFrame(b)
df3 = pd.DataFrame(c)
df4 = pd.DataFrame(d)
df5 = pd.DataFrame(e)
df6 = pd.DataFrame(f1)
df7 = pd.DataFrame(g)
df8 = pd.DataFrame(h)
df9 = pd.DataFrame(i)
df10 = pd.DataFrame(j)


fig, axes = plt.subplots(10, sharex=True)
df1.hist(ax=axes[0], grid=False, label='teste', color='w', ec='r', bins=100)
df2.hist(ax=axes[1], grid=False, color='r')
df3.hist(ax=axes[2], grid=False, color='r')
df4.hist(ax=axes[3], grid=False, color='r')
df5.hist(ax=axes[4], grid=False, color='r')
df6.hist(ax=axes[5], grid=False, color='k')
df7.hist(ax=axes[6], grid=False, color='k')
df8.hist(ax=axes[7], grid=False, color='k')
df9.hist(ax=axes[8], grid=False, color='k')
df10.hist(ax=axes[9], grid=False, color='k')

plt.subplots_adjust(wspace=0, hspace=0.05)


for ax in axes:
    ax.tick_params(direction='in', bottom=True, top=True, left=True, right=True, length=8)
    ax.tick_params(which='minor',  direction='in', length=4, top=True, right=True)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.yaxis.get_ticklocs(minor=True)
    ax.xaxis.get_ticklocs(minor=True)
    ax.minorticks_on
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.legend(loc='best', edgecolor="k", framealpha=0, fancybox=False, borderpad=0.2, handletextpad=0.25, handlelength=2)
    # ax.set_ylim(bottom=7, top=10)
    # ax.set_ylim(bottom=9, top=12)
    ax.set_title('  ')
    



# fig.text(0.5, 0.075, 'Temperature (K)', ha='center')
# fig.text(0.05, 0.475, 'Radius (Å)', ha='center', rotation=90)

plot_filename = 'teste'
plt.savefig(plot_filename, format="pdf", bbox_inches='tight')




