import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

plt.gca().add_patch(plt.Rectangle(xy=(-2, -2), width=4, height=4, fc='none', ec='black', lw=2))
plt.gca().add_patch(plt.Circle((-0.5, 1.75),0.25, fc='black'))
#plt.gca().add_patch(plt.Circle((-0.5, -1.5),0.25, fc='black'))
plt.gca().add_patch(plt.Circle((1, -0.5),0.25, fc='black'))

shift=6
fac=1.25
plt.gca().add_patch(plt.Rectangle(xy=(-2/fac+shift, -2/fac), width=4/fac, height=4/fac, fc='none', ec='blue', lw=2))
plt.gca().add_patch(plt.Circle((-0.5/fac+shift, 1.75/fac),0.25, fc='blue'))
#plt.gca().add_patch(plt.Circle((-0.5/fac+shift, -1.5/fac),0.25, fc='blue'))
plt.gca().add_patch(plt.Circle((1/fac+shift, -0.5/fac),0.25, fc='blue'))
plt.gca().annotate("", xy=(2.5, -0.3), xytext=(4, -0.3), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.gca().annotate("", xy=(2.5, -0.8), xytext=(4, -0.8), arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
plt.text(3.25,0.7, 'particle\nscaling', horizontalalignment='center', verticalalignment='center', fontsize=12)

shift=-6
plt.gca().add_patch(plt.Rectangle(xy=(-2/fac+shift, -2/fac), width=4/fac, height=4/fac, fc='none', ec='red', lw=2))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.75),0.25, edgecolor='red', linestyle='dashed', fill=None))
#plt.gca().add_patch(plt.Circle((-0.5+shift, 1.75),0.25, fc='black'))
#plt.gca().add_patch(plt.Circle((-0.5+shift, -1.5),0.25, fc='black'))
#plt.gca().add_patch(plt.Circle((-0.5+shift, -1.5+4/fac),0.25, edgecolor='red', linestyle='dashed', fill=None))
plt.gca().add_patch(plt.Circle((-0.5+shift, 1.75-4/fac),0.25, fc='black'))
#plt.text(-0.5+shift, 1.75-4/fac, 'X', horizontalalignment='center', verticalalignment='center', fontsize=12, color='red')
plt.gca().add_patch(plt.Circle((1+shift, -0.5),0.25, fc='black'))
plt.gca().annotate("", xy=(-2.5, -0.3), xytext=(-4, -0.3), arrowprops=dict(arrowstyle="<-", lw=2, color='red'))
plt.gca().annotate("", xy=(-2.5, -0.8), xytext=(-4, -0.8), arrowprops=dict(arrowstyle="->", lw=2, color='red', linestyle='dashed'))
plt.text(-3.25,-0.85, '/', horizontalalignment='center', verticalalignment='center', fontsize=14, color='red')
plt.text(-3.25,1.25-0.3, 'no\nparticle\nscaling', horizontalalignment='center', verticalalignment='center', fontsize=12)

plt.axis('scaled')
plt.axis('off')
#plt.show()
plt.savefig('npt.png', bbox_inches='tight', transparent=True, dpi=300)
