import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['1', '2', '3', '4', '5']
unl_fr = [42, 23.80 * 42/23.80 , 24.84*42/24.84, 28*42/28, 33.94*42/33.94]
unl_br = [26.77, 18.41* 42/23.80, 23.73*42/24.84, 21*42/28, 32*42/33.94]
unl_self_r = [26, 16.73* 42/23.80, 21.87*42/24.84, 24*42/28, 33*42/33.94]
unl_hess_r = [32.63,  21*42/23.80, 21.82*42/24.84, 24.74*42/28, 32.03*42/33.94]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Origin', color='royalblue', hatch='/')
plt.bar(x - width / 8, unl_br, width=0.148, label='BFU', color='gold', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='BFU-SS', color='green', hatch='++')
plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', color='red', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 60, 10)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='lower right', fontsize=15)
plt.xlabel('$K_e$' ,fontsize=20)
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
plt.savefig('cifar_KLD_ke_bar.png', dpi=200)
plt.show()
