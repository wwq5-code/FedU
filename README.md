# BFU

# Bayesain Federated Unlearning and BFU-SS

### Prerequisites

```
python = 3.8
pytorch = 1.4.0
matplotlib
numpy
```

### Running the experiments

1. To run the BFU and BFU-SS on MNIST
```
python /Federated_learning/BackdoorFedUnl/BackdoorFedAvg.py
```

2. To run the BFU and BFU-SS on CIFAR10
```
python /Federated_learning/BackdoorFedUnl/backdoorUnl_cifar/CIFAR_KLD_conve.py
```

3. To run the HFU on MNIST
```
python /Federated_learning/Unl-subtract_hessian/backdoor_FedHessian.py
```

4. To run the HFU on CIFAR
```
python /Federated_learning/Unl-subtract_hessian/Hessian_backddor_CIFAR/cifar_hessian_u/backdoor_FedHessian_er01_cifar.py
```