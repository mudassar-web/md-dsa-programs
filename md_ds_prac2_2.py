#Aim : Program to display the Fibonacci series upto nth term using recursive functions.

from time import *

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

t1=perf_counter()
# take input from the user
nterms = int(input("Enter n terms="))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci series:")
   for i in range(nterms):
       print(fibo(i))

t2=perf_counter()
print("Time complexity for ",nterms," terms is ",(t2-t1))