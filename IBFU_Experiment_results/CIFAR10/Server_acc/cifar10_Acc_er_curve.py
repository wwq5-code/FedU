

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['2%', '4%', '6%', '8%', '10%']

unl_fr = [80.4, 80.5, 80.4, 80.3, 80.4]
unl_br = [79.97, 79.58, 78.98, 79.44, 78.98]
unl_self_r = [80.05, 80.45, 80.23, 80.17, 80.16]
unl_hess_r = [79.97,  79.29, 79.03, 79.19, 79.3]


plt.figure()
#plt.figure(figsize=(8, 5.3))
l_w=5.5
m_s=15
plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_br, color='orange',  marker='x',  label='CRF',linewidth=l_w,  markersize=m_s)
plt.plot(x, unl_self_r, color='g',  marker='*',  label='CTFU',linewidth=l_w, markersize=m_s)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(72 ,83,2)
plt.yticks(my_y_ticks,fontsize=20)

plt.xlabel('$\it{EDR}$' ,fontsize=20)
plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar_acc_er_curve.png', dpi=200)
plt.show()