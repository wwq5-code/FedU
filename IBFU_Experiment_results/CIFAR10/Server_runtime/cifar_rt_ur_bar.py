import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = [r'0.05', '0.1', '0.15', '0.2', '0.25']
unl_fr = [40*2*2.76, 40*2*2.76, 40*2*2.76, 40*2*2.76, 40*2*2.76]
unl_br = [4*2*2.76, 3*2*2.76, 3*2*2.76, 3*2*2.76, 1*2*2.76]
unl_self_r = [6*2*2.76, 5*2*2.76, 4*2*2.76, 3*2*2.76, 2*2*2.76]
unl_hess_r = [40*2*2.76,  8*2*2.76, 18*2*2.76, 18*2*2.76, 18*2*2.76]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots(figsize=(8, 5.3))
plt.bar(x - width / 4 - width / 8 , unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
plt.bar(x  - width / 16 , unl_br, width=0.168, label='IBFU', color='orange', hatch='\\')
plt.bar(x + width / 4, unl_self_r, width=0.168, label='IBFU-SS', color='g', hatch='x')


#plt.bar(x + width / 2 - width / 8 + width / 32, unl_hess_r, width=0.148, label='HFU', color='tomato', hatch='-')


#plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 260, 50)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper right', fontsize=15)
plt.xlabel('$\\beta_u$' ,fontsize=20)
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
plt.savefig('cifar_rt_ur_bar.png', dpi=200)
plt.show()
