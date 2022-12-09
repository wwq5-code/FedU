import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0.001', '0.01', '0.1', '1', '10']
unl_fr = [82.86*42/82.86,  22.101 * 42/22.101  ,24.84 * 42/24.84 , 39.49*42/39.49, 24.08*42/24.08]
unl_br = [75.08*42/82.86, 20.31 * 42/22.101   ,23.73* 42/24.84, 42.03*42/39.49, 28.07*42/24.08]
unl_self_r = [71.53*42/82.86, 18.76 * 42/22.101 ,21.87* 42/24.84, 42.17*42/39.49, 28.75*42/24.08 ]
unl_hess_r = [21.82*42/82.86,  42 * 42/22.101,21.82*42/24.84, 21.82*42/39.49, 21.82*42/24.08 ]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 4, unl_fr, width=0.148, label='Origin', color='royalblue',  hatch='/')
plt.bar(x - 0, unl_br, width=0.148, label='BFU', color='gold', hatch='**')
plt.bar(x + width / 4, unl_self_r, width=0.148, label='BFU-SS', color='green', hatch='++')

#plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD', fontsize=20)
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
