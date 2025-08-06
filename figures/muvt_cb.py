import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]

xyzs=[
[-0.01, 1.75],
[-1.6, 1.5],
[-1.4, 0.4],
[-1.2, -0.6],
[-1.7, -1.45],
[-0.4, -1.3],
[0.8, -1.45],
[1, 0.6],
[1.3, 1.6],
[1.2, -0.5],
]
trials=[
[-0.1, 0.1],
[0.7, 0.8],
[-1.4, 1.2],
[-1.4+2.8, -1.4],
]

def draw(xyzs, trials, shift):
    # box
    plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
    # particles
    for xyz in xyzs:
        plt.gca().add_patch(plt.Circle((xyz[0]+shift, xyz[1]),0.5, fc='black'))
    for itrial,trial in enumerate(trials):
        color = 'red'
        if itrial == 0: color = 'blue'
        plt.gca().add_patch(plt.Circle((trial[0]+shift, trial[1]),0.5, fc=color, edgecolor=color, fill=None, linestyle='dashed'))

draw(xyzs, trials, shift=-4)
draw(xyzs, list(), shift=4)
plt.gca().add_patch(plt.Circle((trials[0][0]+4, trials[0][1]),0.5, fc='blue', edgecolor='blue'))

plt.gca().annotate("", xy=(-1.8, 1), xytext=(1.8, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.text(0, 1.5, 'insert', horizontalalignment='center', verticalalignment='center', fontsize=16)
plt.gca().annotate("", xy=(-1.8, -1), xytext=(1.8, -1), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -0.5, 'delete', horizontalalignment='center', verticalalignment='center', fontsize=16)

plt.axis('scaled')
plt.axis('off')
plt.savefig(basename+'.pdf', bbox_inches='tight', transparent=True)
