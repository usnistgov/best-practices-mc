import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

def vapor_box(x_shift, y_shift, scale):
    xyzs=[
    [-1.5, -0.4],
    [0.7, -1.25],
    [1.2, 1.2],
    ]
    plt.gca().add_patch(plt.Rectangle(xy=(scale*-2+x_shift, scale*-2+y_shift), width=scale*4, height=scale*4, fc='none', ec='black', lw=2))
    for xyz in xyzs:
        plt.gca().add_patch(plt.Circle((scale*xyz[0]+x_shift, scale*xyz[1]+y_shift),0.5, fc='black'))
    plt.text(scale*-1.65+x_shift, scale*1.5+y_shift, '1', fontsize=16, color='blue', horizontalalignment='center', verticalalignment='center')

def liquid_box(x_shift, y_shift, scale):
    xyzs=[
    [0.01, -1.75],
    [1.6, -1.5],
    [1.4, -0.4],
    [1.2, 0.6],
    [1.7, 1.45],
    [0.4, 1.3],
    [-0.8, 1.45],
    [-1, -0.6],
    [-1.3, -1.6],
    [-1.2, 0.5],
    ]
    plt.gca().add_patch(plt.Rectangle(xy=(scale*-2+x_shift, scale*-2+y_shift), width=scale*4, height=scale*4, fc='none', ec='black', lw=2))
    for xyz in xyzs:
        plt.gca().add_patch(plt.Circle((scale*xyz[0]+x_shift, scale*xyz[1]+y_shift),0.5, fc='black'))
    plt.text(scale*-1.65+x_shift, scale*1.5+y_shift, '2', fontsize=16, color='blue', horizontalalignment='center', verticalalignment='center')

vapor_box(-4, 3, scale=1)
plt.text(-4, 0, '+', fontsize=28, horizontalalignment='center', verticalalignment='center')
liquid_box(-4, -3, scale=1)

plt.text(0, 1, r'$1$ to $2$', fontsize=16, horizontalalignment='center', verticalalignment='center')
plt.gca().annotate("", xy=(-1.5, 0.5), xytext=(1.5, 0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.gca().annotate("", xy=(-1.5, -0.5), xytext=(1.5, -0.5), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -1, r'$2$ to $1$', fontsize=16, horizontalalignment='center', verticalalignment='center')

scale=0.75
vapor_box(4, 3, scale=scale)
plt.text(4, 0.5, '+', fontsize=28, horizontalalignment='center', verticalalignment='center')
liquid_box(4, -3, scale=(2-scale**2)**0.5)
plt.axis('scaled')
plt.axis('off')
plt.savefig('gibbs_volume.png', bbox_inches='tight', transparent=True, dpi=300)
