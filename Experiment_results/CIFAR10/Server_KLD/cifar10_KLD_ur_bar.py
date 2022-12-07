import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0.01', '0.05', '0.1', '0.15', '0.2']
unl_fr = [22*42/22,  32.37 * 42/32.37  ,42 * 42/42 , 26.49*42/26.49, 21.46*42/21.46 ]
unl_br = [20.31*42/22, 24.77 * 42/32.37   ,41.04* 42/42, 22.97*42/26.49, 16.70*42/21.46]
unl_self_r = [18.76*42/22, 25 * 42/32.37 ,41.16* 42/42, 22.78*42/26.49, 18.06*42/21.46 ]
unl_hess_r = [21.82*42/22,  42 * 42/32.37,21.82*42/42, 21.82*42/26.49, 21.82*42/21.46 ]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Origin', hatch='/')
plt.bar(x - width / 8, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
#plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD to Retrain', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 60, 10)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='lower right', fontsize=15)

# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.xlabel('$\\beta$' ,fontsize=20)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar_KLD_ur_bar.png', dpi=400)
plt.show()
