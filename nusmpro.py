import numpy as np
"""
author->veenit kumar shukla
program of calculating the mean of the two array which yeilds same mean but different MAD
"""
a=np.array([2,2,4,4],dtype=np.int)
b=np.array([1,1,4,6],dtype=np.int)
k=np.mean(a)
l=np.mean(b)
print(k,l)
p=(np.sum(np.abs(k-a)))/np.size(a)
m=(np.sum(np.abs(l-b)))/np.size(b)
print(p,  m)