import numpy as np

a = np.array([[1, 2, 3, 4, 5]])
print(a)
a.transpose(1,0)
a = a.T
# print(a.T)
print(a[0].item())