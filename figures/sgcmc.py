import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]

shift = -4
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.5),0.25, fc='red'))
plt.gca().add_patch(plt.Circle((0.5+shift, -1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((1+shift, -0.5),0.25, fc='black'))

plt.gca().annotate("", xy=(-1.8, 1), xytext=(1.8, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.text(0, 1.5, r'type $i$ to $j$', horizontalalignment='center', verticalalignment='center', fontsize=16)
plt.gca().annotate("", xy=(-1.8, -1), xytext=(1.8, -1), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -0.5, r'type $j$ to $i$', horizontalalignment='center', verticalalignment='center', fontsize=16)

shift = 4
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.5),0.25, fc='red'))
plt.gca().add_patch(plt.Circle((0.5+shift, -1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((1+shift, -0.5),0.25, fc='red'))


plt.axis('scaled')
plt.axis('off')
#plt.show()
plt.savefig(basename+'.pdf', bbox_inches='tight', transparent=True)
