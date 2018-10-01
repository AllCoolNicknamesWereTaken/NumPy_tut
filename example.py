from numpy import *
a = arange(20).reshape(4,5)
print(a)
print(a.ndim)
print("wymiary  {}, typy {}".format(a.dtype.name, a.itemsize))
b = ones((2,3,5,6))
print(b.ndim)
c = empty_like(a)
a = a-c

d = a>(-45)
print(d)
#as array
# print(c*a)
# as matrix
d = random.random((2,3,6))
# print("minimum {}, maximum{}".format(d.min(),d.max()))
print(d)
print("min  kol {}, sum wiersze {}".format(d.min(axis=0), d.sum(axis=1)))
