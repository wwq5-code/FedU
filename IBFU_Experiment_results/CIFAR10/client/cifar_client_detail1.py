

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


y_bfu_back_acc =[0.2435, 0.10232, 0.0511333333080013593, 0.019999999552965164, 0.009999999776482582]
y_bfu_acc =  [0.9966666, 0.9374999, 0.8874999, 0.85, 0.80]

y_ss_back_acc = [0.43, 0.2013, 0.10333333080013593, 0.019999999552965164, 0.009999999776482582]
y_ss_acc =  [0.9966666, 0.9893213, 0.95323412, 0.9239894, 0.90]


y_hfu_back_acc= [0.2 , 0.0432443,  0.0100000000372529, 0.014999999664723873,  0.014999999664723873]

y_hfu_acc = [0.9966666, 0.9453, 0.924999, 0.8664999,  0.84]


x=[]
y_unl_s = []
y_unl_self_s =[]
y_nips_rkl_s =[]
y_hessian_30_s =[]
for i in range(5):
    # print(np.random.laplace(0, 1)/10+0.2)
    x.append(i)
    #y_fkl[i] = y_fkl[i*2]*100
    y_bfu_back_acc[i] = y_bfu_back_acc[i]*100
    #y_bfu_acc[i] = y_bfu_acc[i]*100
    y_ss_back_acc[i] = y_ss_back_acc[i]*100
    #y_ss_acc[i] = y_ss_acc[i]*100
    y_hfu_back_acc[i] = y_hfu_back_acc[i]*100
    #y_hfu_acc[i] = y_hfu_acc[i]*100


plt.figure()
plt.plot(x, y_bfu_back_acc, color='orange',  marker='x',  label='IBFU',linewidth=4,  markersize=10)
plt.plot(x, y_ss_back_acc, color='g',  marker='*',  label='IBFU-SS',linewidth=4, markersize=10)
#plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
plt.plot(x, y_hfu_back_acc, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)

# plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
# plt.plot(x, unl_br, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
# plt.plot(x, unl_self_r, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
# plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)


# plt.plot(x, y_unl_s, color='b', marker='^', label='Normal Bayessian Fed Unlearning',linewidth=3, markersize=8)
# plt.plot(x, y_unl_self_s, color='r',  marker='x',  label='Self-sharing Fed Unlearning',linewidth=3, markersize=8)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
# plt.plot(x, y_hessian_30_s, color='y',  marker='*',  label='Unlearning INFOCOM22',linewidth=3, markersize=8)


plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
plt.xlabel('Epoch' ,fontsize=20)
plt.ylabel('Backdoor Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(0 ,90,20)
plt.yticks(my_y_ticks,fontsize=20)
plt.xticks(x,fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("Fashion MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar_client_detail_backdoor.png', dpi=200)
plt.show()