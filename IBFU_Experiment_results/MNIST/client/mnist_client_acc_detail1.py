

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


y_bfu_back_acc =[0.971999979019165, 0.707999986410141, 0.0800000000745058, 0.009999999776482582, 0.0]
y_bfu_acc =  [0.9879999756813049, 0.9799999594688416, 0.9233333269755045, 0.8899999856948853, 0.8399999737739563]
y_ss_back_acc = [0.9819999933242798, 0.7794999957084656, 0.14449999686330556, 0.0, 0.0]
y_ss_acc = [0.9799999594688416, 0.9739999771118164, 0.9399999737739563, 0.9299999594688416, 0.9099999952316284]

y_hfu_back_acc= [0.9474999904632568, 0.17666666644314924, 0.0, 0.0,0]
y_hfu_acc = [0.993999969959259, 0.9666666388511658, 0.9099999666213989, 0.8799999642372131, 0.8499999642372131]


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

l_w=5.5
m_s=15

plt.plot(x, y_hfu_acc, color='r',  marker='p',  label='HFU',linewidth=l_w, markersize=m_s)

plt.plot(x, y_bfu_acc, color='orange',  marker='x',  label='CRFU',linewidth=l_w,  markersize=m_s)
plt.plot(x, y_ss_acc, color='g',  marker='*',  label='CRFU-SS',linewidth=l_w, markersize=m_s)
#plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')

# plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
# plt.plot(x, unl_br, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
# plt.plot(x, unl_self_r, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
# plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)

# plt.plot(x, y_unl_s, color='b', marker='^', label='Normal Bayessian Fed Unlearning',linewidth=3, markersize=8)
# plt.plot(x, y_unl_self_s, color='r',  marker='x',  label='Self-sharing Fed Unlearning',linewidth=3, markersize=8)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
# plt.plot(x, y_hessian_30_s, color='y',  marker='*',  label='Unlearning INFOCOM22',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
plt.xlabel('Epoch' ,fontsize=20)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(80 ,105,5)
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
plt.savefig('mnist_client_detail_acc.png', dpi=200)
plt.show()