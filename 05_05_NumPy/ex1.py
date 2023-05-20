# We will use numpy to create arrays
# We will use numpy to create arrays
import numpy as np #we have a error because we don't have numpy installed
# we can install numpy using pip install numpy

a = np.array([1,2,3,4,5] , dtype = float)
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)

array = np.empty((3,4) , dtype = float)
print(array)

c = np.eye(3, 3, 1)
print(c)

m = np.ones( (2,3), dtype = float)
print(m)

n = np.zeros( (2,3), dtype = float)
print(n)

h = np.arange( 5 )
print(h)

i = np.arange( 2, 10, 2 )
print(i)



