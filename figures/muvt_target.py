import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]

shift = -5

def make(shift):
    plt.gca().add_patch(plt.Rectangle(xy=(-2.5+shift, -2.5), width=5, height=5, fc='none', ec='black', lw=2))
    plt.gca().add_patch(plt.Circle((-2+shift, 0),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((-1+shift, 0),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((0+shift, 0),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((1+shift, 0),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((2+shift, 0),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((0+shift, 1),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((0+shift, 2),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((0+shift, -1),0.45, fc='black'))
    plt.gca().add_patch(plt.Circle((0+shift, -2),0.45, fc='black'))
    plt.gca().add_patch(plt.Rectangle(xy=(0.55+shift, -2.45), width=1.9, height=1.9, fc='none', ec='black', lw=2, linestyle='dashed'))
#    for y in np.arange(-1.5, 2.5, 1):
#        plt.plot([-2.5+shift, 2.5+shift], [y, y], linestyle='dashed', color='black')
#        plt.plot([y+shift, y+shift], [-2.5, 2.5], linestyle='dashed', color='black')
    plt.text(1.25+shift, -5/6-0.3-0.1, r'$v$', horizontalalignment='center', verticalalignment='center', fontsize=16, color='blue')

make(shift=-5)
#plt.gca().add_patch(plt.Circle((-1.85-5, +2),0.35, fc='blue'))

plt.gca().annotate("", xy=(-1.8, 1), xytext=(1.8, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.text(0, 1.5, 'insert', horizontalalignment='center', verticalalignment='center', fontsize=16)
plt.gca().annotate("", xy=(-1.8, -1), xytext=(1.8, -1), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -0.5, 'delete', horizontalalignment='center', verticalalignment='center', fontsize=16)

make(shift=5)
plt.gca().add_patch(plt.Circle((1.85+5, -1.85),0.35, fc='blue'))
#plt.gca().add_patch(plt.Circle((-1.85+5, +2),0.35, fc='blue'))

plt.axis('scaled')
plt.axis('off')
#plt.show()
plt.savefig(basename+'.pdf', bbox_inches='tight', transparent=True)
