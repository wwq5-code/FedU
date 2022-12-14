

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


y_bfu_back_acc =[0.9749999940395355, 0.7449999650319418, 0.30499999473492306, 0.02166666587193807, 0.008333333147068819]
y_bfu_acc =  [0.9966666499773661, 0.9883333047231039, 0.9583333134651184, 0.9483333230018616, 0.9316666523615519]
y_ss_back_acc = [0.9849999845027924, 0.7799999713897705, 0.34166665251056355, 0.02999999901900689, 0.004999999888241291]
y_ss_acc = [0.9899999797344208, 0.9883332947889963, 0.9833333094914755, 0.9633333086967468, 0.9583333134651184]

y_hfu_back_acc= [0.99, 0.28999999165534973, 0.0, 0.0,0]
y_hfu_acc = [0.986,0.9868333339691162, 0.8956666588783264, 0.8953333497047424, 0.87]


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
    y_bfu_acc[i] = y_bfu_acc[i]*100
    y_ss_back_acc[i] = y_ss_back_acc[i]*100
    y_ss_acc[i] = y_ss_acc[i]*100
    y_hfu_back_acc[i] = y_hfu_back_acc[i]*100
    y_hfu_acc[i] = y_hfu_acc[i]*100


plt.figure()
plt.plot(x, y_bfu_back_acc, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
plt.plot(x, y_ss_back_acc, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
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
my_y_ticks = np.arange(0 ,110,20)
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
plt.savefig('mnist_client_detail_backdoor.png', dpi=200)
plt.show()