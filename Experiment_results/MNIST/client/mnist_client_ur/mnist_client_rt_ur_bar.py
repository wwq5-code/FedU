import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0.1', '0.5', '1', '1.5', '2']

unl_fr = [10*0.22, 1*10*0.22, 1*10*0.22, 1*10*0.22, 1*10*0.22]
unl_br = [0.1*3*0.22, 0.1*5*0.22, 0.1*5*0.22, 0.1*4*0.22, 0.1*5*0.22]
unl_self_r = [0.2*3*0.22, 0.2*6*0.22, 0.2*7*0.22, 0.2*5*0.22, 0.2*6*0.22]
unl_hess_r = [1*2*0.22,  1*2*0.22, 2*0.22, 2*0.22, 2*0.22]

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
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 3, 0.5)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.xlabel('$\\beta$' ,fontsize=20)
plt.legend(loc='upper right', fontsize=15)

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
plt.savefig('mnist_client_rt_ur_bar.png', dpi=400)
plt.show()
