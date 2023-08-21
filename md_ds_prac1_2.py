# Aim : Program to calculate Time complexity of a program that print cube of each item in a list.

from time import *

t1= perf_counter()
lst=[1,-5,6,91,21,7,-2,8,4,-1,65,77,9,23,62,76,42,63,99,78]
print (lst)
lst.sort()
print(lst)
for i in range (0,20):
        cub=lst[i]**3
        print(cub)

t2 = perf_counter()
print("Time complexity for processing 20 elements is ",(t2-t1))
