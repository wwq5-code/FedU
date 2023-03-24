import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['20', '40', '60', '80', '100']
unl_fr = [20*10*0.22 , 20*10*0.22, 20*10*0.22 , 20*10*0.22 , 20*10*0.22   ]
unl_br = [13/2.5*10*0.22 , 9/2.5*10*0.22, 9/2.5*10*0.22, 8/2.5*10*0.22, 9/2.5*10*0.22  ]
unl_self_r = [11/2.5*10*0.22, 10/2.5*10*0.22, 9/2.5*10*0.22, 10/2.5*10*0.22, 10/2.5*10*0.22 ]
unl_hess_r = [9/2.5*10*0.22,  12/2.5*10*0.22, 17/2.5*10*0.22, 23/2.5*10*0.22, 25/2.5*10*0.22 ]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.figure()
#plt.subplots(figsize=(8, 5.3))
plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HFU', color='tomato', hatch='-')

plt.bar(x - width / 8 - width / 16 , unl_br, width=0.168, label='CRFU', color='orange', hatch='\\')
plt.bar(x + width / 8, unl_self_r, width=0.168, label='CRFU-SS', color='g', hatch='x')



# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 26*2, 8)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper left', fontsize=15)
plt.xlabel('K' ,fontsize=20)
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
plt.savefig('mnist_rt_clients_k_bar.png', dpi=200)
plt.show()
