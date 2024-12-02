import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

circles=[
[-0.5, 1.2], [0.7, 1.2],
[-1.2, 0], [1.2, 0],
[-0.5, -1.2], [0.7, -1.2],
]

#plt.axes()
for circle in circles:
    plt.gca().add_patch(plt.Circle((circle[0], circle[1]),1, fc='lightgrey'))
for circle in circles:
    plt.gca().add_patch(plt.Circle((circle[0], circle[1]),0.5, fc='grey'))
#plt.gca().set_facecolor('black')
#plt.figure(facecolor='yellow')
plt.gca().add_patch(plt.Circle((0, 0),0.05, fc='red'))
plt.text(0.05, -0.05, r'$\mathbf{r}_o$', fontsize=24, color='red')
plt.gca().add_patch(plt.Rectangle(xy=(-0.5, -0.5), width=1, height=1, fc='none', ec='red', lw=2))
#plt.gca().add_patch(plt.Circle((0., 0.),0.5, fc='none', ec='black', linestyle='--'))
plt.gca().add_patch(plt.Circle((0.2, 0.3),0.05, fc='blue'))
plt.text(0.25, 0.25, r'$\mathbf{r}_n$', fontsize=24, color='blue')
plt.gca().add_patch(plt.Rectangle(xy=(-0.5+0.2, -0.5+0.3), width=1, height=1, fc='none', ec='blue', lw=2))
#plt.gca().add_patch(plt.Circle((0.2, 0.3),0.5, fc='none', ec='blue', linestyle='--'))
shift=0.02
plt.gca().annotate("", xy=(0.175+shift, 0.275), xytext=(0.025+shift, 0.025*3/2), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
shift=-0.02
plt.gca().annotate("", xy=(0.175+shift, 0.275), xytext=(0.025+shift, 0.025*3/2), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
#plt.gca().annotate("", xy=(0.175, 0.275), xytext=(0.025, 0.025*3/2), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))

# delta
plt.gca().annotate("", xy=(-0.5, -0.55), xytext=(0.5, -0.55), arrowprops=dict(arrowstyle="<->", lw=2, color='red'))
plt.text(-0.1, -0.75, r'$2\delta$', fontsize=24, color='red')

plt.axis('scaled')
plt.axis('off')
plt.xlim([-1., 1.])
plt.ylim([-1., 1.])
plt.savefig('dccb_draw.png', bbox_inches='tight', transparent=True, dpi=300)
