import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

fig, ax = plt.subplots()

diff=5
csize=2

# old
plt.gca().add_patch(plt.Circle((-diff, 0), csize, facecolor='white', edgecolor='red', linestyle='solid', lw=2))
plt.text(-diff,0, 'old', horizontalalignment='center', verticalalignment='center', fontsize=25, color='red')

# old to new
plt.gca().annotate("", xy=(-diff, 2.2), xytext=(-2.2, diff), arrowprops=dict(arrowstyle="<-", lw=2, color='red', connectionstyle="arc3,rad=.25"))
plt.text(-diff-0.2, diff, r'$\alpha_{o\rightarrow n}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='red', rotation=0)
#plt.text(0,2.5, r'$p_o\alpha_{o\rightarrow n}\pi_{o\rightarrow n}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='red')

# old to somewhere else
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-10, 2.8), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-9, 3.8), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-9.5, 3.3), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-10, 0), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-10, 0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.gca().annotate("", xy=(-7.2, 0), xytext=(-10, -0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.text(0, 2, r'$1-\pi_{o\rightarrow n}$', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')
#plt.text(-9, 1, r'$1-\alpha_{o\rightarrow n}$', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

# new temp
plt.gca().add_patch(plt.Circle((0, diff), csize, facecolor='white', edgecolor='black', linestyle='dotted', lw=2))
plt.text(0, diff, r'new', horizontalalignment='center', verticalalignment='center', fontsize=25, color='black')

# accept
plt.gca().annotate("", xy=(2.2, diff), xytext=(diff, 2.2), arrowprops=dict(arrowstyle="<-", lw=2, color='red', connectionstyle="arc3,rad=.25"))
plt.text(diff, diff, r'$\pi_{o\rightarrow n}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='red', rotation=0)

# reject
#plt.gca().annotate("", xy=(-1, 3), xytext=(-3, 1), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))

# new
plt.gca().add_patch(plt.Circle((diff, 0), csize, facecolor='white', edgecolor='blue', linestyle='solid', lw=2))
plt.text(diff,0, 'new', horizontalalignment='center', verticalalignment='center', fontsize=25, color='blue')

# new to old
plt.gca().annotate("", xy=(diff, -2.2), xytext=(2.2, -diff), arrowprops=dict(arrowstyle="<-", lw=2, color='blue', connectionstyle="arc3,rad=0.25"))
plt.text(diff, -diff, r'$\alpha_{n\rightarrow o}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='blue', rotation=0)
#plt.text(0,-2.5, r'$p_n\alpha_{n\rightarrow o}\pi_{n\rightarrow o}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='blue')

# new to somewhere else
#plt.gca().annotate("", xy=(7.2, 0), xytext=(10, -2.8), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(7.2, 0), xytext=(9.5, -3.3), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(7.2, 0), xytext=(9, -3.8), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))
#plt.gca().annotate("", xy=(7.2, 0), xytext=(10, 0), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.gca().annotate("", xy=(7.2, 0), xytext=(10, -0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.gca().annotate("", xy=(7.2, 0), xytext=(10, 0.5), arrowprops=dict(arrowstyle="<-", lw=2, color='black', linestyle='dotted'))
#plt.text(0, -2, r'$1-\pi_{n\rightarrow o}$', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')
#plt.text(9, 1, r'$1-\alpha_{n\rightarrow o}$', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

# old temp
plt.gca().add_patch(plt.Circle((0, -diff), csize, facecolor='white', edgecolor='black', linestyle='dotted', lw=2))
plt.text(0, -diff, r'old', horizontalalignment='center', verticalalignment='center', fontsize=25, color='black')

# accept
plt.gca().annotate("", xy=(-2.2, -diff), xytext=(-diff, -2.2), arrowprops=dict(arrowstyle="<-", lw=2, color='blue', connectionstyle="arc3,rad=0.25"))
plt.text(-diff, -diff, r'$\pi_{n\rightarrow o}$', horizontalalignment='center', verticalalignment='center', fontsize=25, color='blue', rotation=0)

# reject
#plt.gca().annotate("", xy=(1, -3), xytext=(3, -1), arrowprops=dict(arrowstyle="<-", lw=2, color='black', connectionstyle="arc3,rad=.25", linestyle='dotted'))

plt.axis('scaled')
plt.axis('off')

im = plt.imread('key_figure_spce.png')
newax = fig.add_axes([0.39,0.37,0.25,0.25], anchor='C', zorder=1)
#newax = fig.add_axes([0.41,0.4,0.2,0.2], anchor='C', zorder=1)
newax.imshow(im)
newax.axis('off')

#plt.show()
plt.savefig('key_figure.png', bbox_inches='tight', transparent=True, dpi=300)
