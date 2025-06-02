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
plt.gca().add_patch(plt.Circle((0.75+shift, 1.5),0.25, fc='blue'))
plt.text(0.75+shift, 1.5, 'i', horizontalalignment='center', verticalalignment='center', fontsize=12, color='white')
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),1.3, fc=(0, 1, 0, 0.5)))
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),0.5, fc='white'))
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),0.25, fc='black'))
plt.text(0.5+shift, -0.5, 'j', horizontalalignment='center', verticalalignment='center', fontsize=12, color='white')
plt.gca().add_patch(plt.Circle((-0.5+shift+1/1.2/np.sqrt(2), -0.5-1/1.2/np.sqrt(2)),0.25, fc='black'))
plt.text(-0.5+shift-0.9/np.sqrt(2), -0.5+0.9/np.sqrt(2), r'$v_{AV}$', horizontalalignment='center', verticalalignment='center', fontsize=18, color='black')

plt.gca().annotate("", xy=(-1.8, 1), xytext=(1.8, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='red'))
plt.text(0, 1.5, r'out$\rightarrow$in', horizontalalignment='center', verticalalignment='center', fontsize=16)
plt.gca().annotate("", xy=(-1.8, -1), xytext=(1.8, -1), arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
plt.text(0, -0.5, r'in$\rightarrow$out', horizontalalignment='center', verticalalignment='center', fontsize=16)

shift = 4
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),1.3, fc=(0, 1, 0, 0.5)))
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),0.5, fc='white'))
plt.gca().add_patch(plt.Circle((0.5+shift, -0.5),0.25, fc='black'))
plt.text(0.5+shift, -0.5, 'j', horizontalalignment='center', verticalalignment='center', fontsize=12, color='white')
plt.gca().add_patch(plt.Circle((0.5+shift+1/1.8/np.sqrt(2), -0.5+1/1.8/np.sqrt(2)),0.25, fc='blue'))
plt.text(0.5+shift+1/1.8/np.sqrt(2), -0.5+1/1.8/np.sqrt(2), 'i', horizontalalignment='center', verticalalignment='center', fontsize=12, color='white')
plt.gca().add_patch(plt.Circle((-0.5+shift+1/1.2/np.sqrt(2), -0.5-1/1.2/np.sqrt(2)),0.25, fc='black'))
plt.text(-0.5+shift-0.9/np.sqrt(2), -0.5+0.9/np.sqrt(2), r'$v_{AV}$', horizontalalignment='center', verticalalignment='center', fontsize=18, color='black')


plt.axis('scaled')
plt.axis('off')
#plt.show()
plt.savefig(basename+'.pdf', bbox_inches='tight', transparent=True)
