import numpy as np
"""
author -> Veenit Kumar Shukla
detail -> moving average of 3 months and 5 months
"""
a=np.array([5,8,7,8,8,9,7,9,5,7,5,8])
k=np.size(a)
l=[]
p=[]
i=0
while i<np.size(a):
    if(i>=2):
        p.append(round((a[i]+a[i-1]+a[i-2])/3,2))
    if(i>=4):
        l.append(round((a[i]+a[i-1]+a[i-2]+a[i-3]+a[i-4])/5,1))
    i=i+1
a1=np.array(p)
a2=np.array(l)
print(a1,a2)