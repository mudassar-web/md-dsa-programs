#Aim: Program to find the factorial of a number using recursion

from time import *

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

t1=perf_counter()
# take input from the user
num = int(input("Enter a number: "))

# check is the number is negative
if num < 0:
   print("Factorial does not exist for negative numbers")
elif num == 0:
   print("Factorial of 0 is 1")
else:
   print("Factorial of ",num," is ",factorial(num))

t2=perf_counter()
print("Time complexity to calculate factorial of ",num," is ",(t2-t1))
