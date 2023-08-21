#Aim : Program to calculate Time complexity of any program

from time import *

t1= perf_counter()

lst=[1,-5,6,91,21,7,-2,8,4,-1,65,77,9,23,62]
print (lst)
lst.sort()
print(lst)
for i in range (1,10):
        if lst[i] > 0 :
            print(lst[i])

t2 = perf_counter()
print("total time required to execute program : " , (t2-t1))