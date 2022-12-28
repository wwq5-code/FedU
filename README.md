# IBFU

# Information Bottleneck Federated Unlearning (IBFU) and IBFU-SS

### Prerequisites

```
python = 3.8
pytorch = 1.4.0
matplotlib
numpy
```

### Running the experiments

1. To run the IBFU and IBFU-SS on MNIST
```
python /Federated_learning/BackdoorFedUnl/BackdoorFedAvg.py
```

2. To run the IBFU and IBFU-SS on CIFAR10
```
python /Federated_learning/BackdoorFedUnl/backdoorUnl_cifar/CIFAR10_3u_10e.py
```

3. To run our reproduced and improved HFU on MNIST
```
python /Federated_learning/Unl-subtract_hessian/backdoor_FedHessian.py
```

4. To run our reproduced and improved HFU on CIFAR
```
python /Federated_learning/Unl-subtract_hessian/Hessian_backddor_CIFAR/cifar_hessian_u/hessian_cifar_temp.py
```