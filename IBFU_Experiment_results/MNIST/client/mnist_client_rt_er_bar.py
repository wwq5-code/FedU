import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['2%', '4%', '6%', '8%', '10%']
unl_fr = [1*10*0.22*0.99, 1*10*0.22*0.99, 1*10*0.22*0.99, 1*10*0.22*0.99, 1*10*0.22*0.99]
unl_br = [0.02*10*0.22, 0.04*10*0.22, 0.06*10*0.22, 0.08*10*0.22, 0.1*10*0.22]
unl_self_r = [0.04*10*0.22, 0.08*10*0.22, 0.12*10*0.22, 0.16*10*0.22, 0.2*10*0.22]
unl_hess_r = [0.02*3*0.22 + 1*0.22,  0.04*8*0.22+ 1*0.22, 0.06*9*0.22+ 1*0.22, 0.08*10*0.22+ 1*0.22, 0.1*10*0.22+ 1*0.22]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Retrain', color='royalblue', hatch='/')
plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', color='red', hatch='-')

plt.bar(x - width / 8, unl_br, width=0.148, label='CRFU', color='gold', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='CRFU-SS', color='green', hatch='++')

# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 3, 0.5)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper right', fontsize=15)
plt.xlabel('$\it{EDR}$' ,fontsize=20)
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
plt.savefig('mnist_client_rt_er_bar.png', dpi=200)
plt.show()
