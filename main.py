# This is a sample Python script.

import torch
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('PyCharm')
    for k in range(4):
        print(k)

    x = torch.randn(3,3)
    b = torch.randn(3,2)
    c = torch.eye(x.shape[0])
    a = c.eq(1)
    if False in a:
        print(a)
    # print(a)
    print(x)
    print(c)
    print(c@c.inverse())

    print(1-0.9**0)
    y = [1,2,3,4,5,6]
    t = [1,2,3,4,5,6,7]
    print(y[6:])
    print(np.mean(y))
    i=0
    for a, e in zip(y,t):
        print(a,e)
        i=i+1
        if i >=len(y):
            break
    a = torch.tensor([21]).float()
    b = torch.tensor([0.1]).float()
    # c = torch.tensor([2]).float()
    print(torch.log(a - b), torch.log(a) - torch.log(b))

    e_log_py = torch.exp(-torch.log(a))
    print(e_log_py)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
