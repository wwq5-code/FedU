

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['1', '2', '3', '4', '5']
unl_fr = [0.5, 0.5 , 0.5, 0.5, 0.5]
unl_br =     [1.3, 1.5, 1.33, 1.57, 1.7]
unl_self_r = [1.0, 1.481, 1.0, 1.46, 1.875]
unl_hess_r = [1.28,  1.9, 1.71, 1.026, 1.7]
org =        [12.9, 13.5, 15.22, 25.7, 37.8]



plt.figure()
#plt.figure(figsize=(8, 5.3))

l_w=5.5
m_s=15

plt.plot(x, org, color='cyan',  marker='s',  label='Origin',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_br, color='orange',  marker='x',  label='FedU',linewidth=l_w,  markersize=m_s)
plt.plot(x, unl_self_r, color='g',  marker='*',  label='FedU-U',linewidth=l_w, markersize=m_s)


# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Backdoor Accuracy (%)' ,fontsize=24)
my_y_ticks = np.arange(0 ,44,8)
plt.yticks(my_y_ticks,fontsize=20)

plt.xlabel('$K_u$' ,fontsize=20)
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
plt.savefig('stl_backacc_ke_curve.pdf', format='pdf', dpi=200)
plt.show()