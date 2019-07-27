import numpy as np
"""
author -> veenit kumar shukla
details -> drift approach
"""
a=[]
n=int(input("enter the amount of the data"))
i=0
while i<n:
    a.append(int(input()))
    i=i+1
h=int(input("enter the year you want to know the trend"))
arr=np.array(a)
j = arr[n-1]  + ((h-n)*(a[n-1]-a[0]))/(n-1)
print (j)