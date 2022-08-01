
import numpy as np

a = np.array([1.0,4.55, 123, 0.567, 25.532])

print ('原数组：')
print (a)
print ('round 舍入后：')
print (np.around(a))
print (np.around(a, decimals = 1))
print (np.around(a, decimals = -1))
print('floor 向下取整：')
print(np.floor(a))
print('ceil 向上取整：')
print(np.ceil(a))