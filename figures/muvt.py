
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

shift = -4
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((0.5+shift, -1.5),0.25, fc='black'))
#plt.gca().add_patch(plt.Circle((1+shift, -0.5),0.25, fc='red', edgecolor='red', fill=None, linestyle='dashed'))
#plt.gca().add_patch(plt.Rectangle(xy=(-0.25+shift, -1), width=2, height=2, fc='none', ec='black', lw=2, linestyle='dashed'))
#plt.text(shift+1.5, 1.5, r'$V$', horizontalalignment='center', verticalalignment='center', fontsize=16)

plt.gca().annotate("", xy=(-1.8, 1), xytext=(1.8, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.text(0, 1.5, 'insert', horizontalalignment='center', verticalalignment='center', fontsize=16)
plt.gca().annotate("", xy=(-1.8, -1), xytext=(1.8, -1), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
plt.text(0, -0.5, 'delete', horizontalalignment='center', verticalalignment='center', fontsize=16)

shift = 4
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((0.5+shift, -1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((1+shift, -0.5),0.25, fc='blue'))
#plt.text(1+shift, -0.5, 't', horizontalalignment='center', verticalalignment='center', fontsize=16, color='white')
#plt.gca().add_patch(plt.Rectangle(xy=(-0.25+shift, -1), width=2, height=2, fc='none', ec='black', lw=2, linestyle='dashed'))
#plt.text(shift, 0.75, r'$v$', horizontalalignment='center', verticalalignment='center', fontsize=16)


plt.axis('scaled')
plt.axis('off')
#plt.show()
plt.savefig('muvt.png', bbox_inches='tight', transparent=True, dpi=300)
