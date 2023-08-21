#Aim : Program to demonstrate previously created Queue

from md_ds_prac5_1 import Queue
from time import *

def queueImplementation():
           Q=Queue()
           for i in range(1,11):                      
                      num=int(input("Enter Number:"))
                      Q.enqueue(num)
                      #Q.enqueue(i)
           
           print("Queue Length:",len(Q))

           for i in range(1,11):
                      if not(Q.isEmpty()):
                                 t1=perf_counter()
                                 num=int(Q.dequeue())
                                 print(num,"Square=",num*num)
                                 print(num,"Removed from Queue")
                                 t2=perf_counter()
                                 print("time take to process",num," is ",(t2-t1))
                      else:
                                 print("Queue is Empty")           


queueImplementation()