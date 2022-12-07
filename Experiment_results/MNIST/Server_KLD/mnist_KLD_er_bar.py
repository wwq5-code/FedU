import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['1%', '5%', '10%', '15%', '20%']
unl_fr = [201*238/201, 255 * 238/255 , 237*238/237, 290*238/290, 237*238/237]
unl_br = [189*238/201, 253.25* 238/255, 233*238/237, 288.53*238/290, 244.7*238/237]
unl_self_r = [189*238/201, 246* 238/255, 228*238/237, 291*238/290, 237*238/237]
unl_hess_r = [190*238/201,  241*238/255, 221*238/237, 274*238/290, 225*238/237]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Origin', hatch='/')
plt.bar(x - width / 8, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('KLD to Retrain', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 260, 50)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.xlabel('$\it{EDR}$' ,fontsize=20)
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
plt.savefig('mnist_KLD_er_bar.png', dpi=400)
plt.show()
