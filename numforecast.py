import numpy as np
import math
"""
author -> Veenit Kumar Shukla
detail -> Straight-line method for forecasting
"""
a=int(input())
array1=int(input())
aa1=np.array(array1)
aa1.resize(a)
print("enter the increase cost")
y=int(input())
for x in np.nditer(aa1,op_flags=['readwrite']):
    x[...]=x[...]+y
k=aa1[aa1.size-1] - aa1[0]
print((4/k)*100)
