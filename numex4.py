import numpy as np
"""
author -> Veenit Kumar Shukla
detail -> implementation of the linear equation with 2*2 matrix
"""
a=np.array([[2,-1],[3,2]],dtype=int)
b=np.array([4,13],dtype=int)
d=np.linalg.det([[2,-1],[3,2]])
print(np.sum(np.multiply(np.linalg.inv(a),b),axis=1).tolist())