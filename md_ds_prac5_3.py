#Aim : Program to demonstrate Simple Stack Implementation.

from md_ds_prac5_2 import Stack

s=Stack()

print("Stack Empty:",s.isEmpty())
s.push(4)
s.push('dog')
print("Peek:",s.peek())
s.push(True)
print("Size:",s.size())
print("Stack Empty:",s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print("Size:",s.size())
s.push('c')
s.push('=')
s.push('a+b')
print("Size:",s.size())
print("Peek:",s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print("Size:",s.size())