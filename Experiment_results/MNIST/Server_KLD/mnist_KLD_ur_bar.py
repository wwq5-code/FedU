import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['0.1', '0.5', '1', '1.5', '2']

unl_fr = [237*238/237, 302*238/302, 329 * 238/329 , 281*238/281, 234*238/234 ]
unl_br = [233*238/237, 309*238/302, 333.25* 238/329, 311*238/281, 245.53*238/234 ]
unl_self_r = [228*238/237, 304*238/302, 345* 238/329, 307*238/281, 255*238/234 ]
# unl_hess_r = [,  3, 9, 10]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 4, unl_fr, width=0.148, label='Retrain', hatch='/')
plt.bar(x - 0, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 4, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
# plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD to Retrain', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 260, 50)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='lower right', fontsize=15)
plt.xlabel('$\\beta$' ,fontsize=20)
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
plt.savefig('mnist_KLD_ur_bar.png', dpi=400)
plt.show()
