import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

def vapor_box(x_shift, y_shift, extra):
    xyzs=[
    [-1.5, -0.4],
    [0.7, -1.25],
    #[1.2, 1.2],
    ]
    plt.gca().add_patch(plt.Rectangle(xy=(-2+x_shift, -2+y_shift), width=4, height=4, fc='none', ec='black', lw=2))
    for xyz in xyzs:
        plt.gca().add_patch(plt.Circle((xyz[0]+x_shift, xyz[1]+y_shift),0.5, fc='black'))
    if extra:
        plt.gca().add_patch(plt.Circle((1.2+x_shift, 1.2+y_shift),0.5, fc='blue'))
    plt.text(-1.65+x_shift, 1.5+y_shift, '1', fontsize=16, color='blue', horizontalalignment='center', verticalalignment='center')

def liquid_box(x_shift, y_shift, extra):
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
    plt.gca().add_patch(plt.Rectangle(xy=(-2+x_shift, -2+y_shift), width=4, height=4, fc='none', ec='black', lw=2))
    for xyz in xyzs:
        plt.gca().add_patch(plt.Circle((xyz[0]+x_shift, xyz[1]+y_shift),0.5, fc='black'))
    if extra:
        plt.gca().add_patch(plt.Circle((-0.2+x_shift, 0.2+y_shift),0.5, fc='blue'))
    plt.text(-1.65+x_shift, 1.5+y_shift, '2', fontsize=16, color='blue', horizontalalignment='center', verticalalignment='center')

vapor_box(-4, 3, extra=True)
plt.text(-4, 0, '+', fontsize=28, horizontalalignment='center', verticalalignment='center')
liquid_box(-4, -3, extra=False)

plt.text(0, 1, r'$1$ to $2$', fontsize=16, horizontalalignment='center', verticalalignment='center')
plt.gca().annotate("", xy=(-1.5, 0.5), xytext=(1.5, 0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.gca().annotate("", xy=(-1.5, -0.5), xytext=(1.5, -0.5), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -1, r'$2$ to $1$', fontsize=16, horizontalalignment='center', verticalalignment='center')

vapor_box(4, 3, extra=False)
plt.text(4, 0, '+', fontsize=28, horizontalalignment='center', verticalalignment='center')
liquid_box(4, -3, extra=True)
plt.axis('scaled')
plt.axis('off')
plt.savefig('gibbs_particle.png', bbox_inches='tight', transparent=True, dpi=300)
