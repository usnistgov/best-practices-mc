import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)

#circles=[
#[-0.5, 1.2], [0.7, 1.2],
#[-1.2, 0], [1.2, 0],
#[-0.5, -1.2], [0.7, -1.2],
#]
#
##plt.axes()
#for circle in circles:
#    plt.gca().add_patch(plt.Circle((circle[0], circle[1]),0.8, fc='lightgrey'))
#for circle in circles:
#    plt.gca().add_patch(plt.Circle((circle[0], circle[1]),0.4, fc='grey'))
#plt.gca().set_facecolor('red')
#plt.figure(facecolor='yellow')

# old circle and box
plt.gca().add_patch(plt.Circle((0, 0),0.05, fc='red'))
plt.text(-0.05, -0.15, r'$\mathbf{r}_o$', fontsize=24, color='red')
dv=0.5
plt.gca().add_patch(plt.Rectangle(xy=(-dv, -dv), width=2*dv, height=2*dv, fc='none', ec='red', lw=2))
#plt.gca().add_patch(plt.Circle((0., 0.),0.5, fc='none', ec='red', linestyle='--'))

# new circle and box
xyo=[0.5, 0.4]
plt.gca().add_patch(plt.Circle((xyo[0], xyo[1]),0.05, fc='blue'))
plt.text(xyo[0]+0.075, xyo[1]-0.05, r'$\mathbf{r}_n$', fontsize=24, color='blue')
plt.gca().add_patch(plt.Rectangle(xy=(-0.4+xyo[0], -0.4+xyo[1]), width=0.8, height=0.8, fc='none', ec='blue', lw=2))

# double arrows
shift=0.02
plt.gca().annotate("", xy=(xyo[0]-0.025+shift, xyo[1]-0.025), xytext=(0.025+shift, 0.025*3/2), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
shift=-0.02
#plt.gca().annotate("", xy=(xyo[0]-0.025+shift, xyo[1]-0.025), xytext=(0.025+shift, 0.025*3/2), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
plt.gca().annotate("", xy=(xyo[0]-0.025+shift, xyo[1]-0.025), xytext=(0.025+shift+0.1, (0.025)*3/2+0.1*4/5), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))
#plt.gca().annotate("", xy=(xyo[0]-0.025+shift, xyo[1]-0.025), xytext=(0.025+shift, 0.025*3/2), arrowprops=dict(arrowstyle="<-", lw=2, color='blue'))

# delta
plt.gca().annotate("", xy=(-0.5, -0.55), xytext=(0.5, -0.55), arrowprops=dict(arrowstyle="<->", lw=2, color='red'))
plt.text(-0.1, -0.75, r'$\delta_o$', fontsize=24, color='red')
plt.gca().annotate("", xy=(0.1, 0.75), xytext=(0.9, 0.75), arrowprops=dict(arrowstyle="<->", lw=2, color='blue'))
plt.text(0.4, 0.85, r'$\delta_n$', fontsize=24, color='blue')

plt.axis('scaled')
plt.axis('off')
#plt.xlim([-0.5, 1.])
#plt.ylim([-0.85, 1.])
plt.savefig('lhs_nvt.png', bbox_inches='tight', transparent=True, dpi=300)
