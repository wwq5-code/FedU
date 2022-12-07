import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['$K_e$ = 1', '$K_e$ = 2', '$K_e$ = 3', '$K_e$ = 4', '$K_e$ = 5']
unl_fr = [238, 221 * 238/221 , 237*238/237, 223*238/223, 281*238/281]
unl_br = [236, 216.25* 238/221, 233*238/237, 243.53*238/223, 315.7*238/281]
unl_self_r = [235, 213* 238/221, 228*238/237, 236*238/223, 305*238/281]
unl_hess_r = [234,  214*238/221, 221*238/237, 212*238/223, 262*238/281]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Retrain', hatch='/')
plt.bar(x - width / 8, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 260, 50)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='lower right', fontsize=15)

# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_KLD_ke_bar.png', dpi=400)
plt.show()
