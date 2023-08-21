#Aim : Implementation of the Stack using a Python list.

class Stack:
  # Creates an empty stack.
  def __init__(self):
    self._theItems=list()
	
  # Returns True if the stack is empty or False otherwise.
  def isEmpty(self):
    return len(self)==0

  # Returns the number of items in the stack.
  def __len__(self):
    return len(self._theItems)

  # Returns the top item on the stack without removing it.
  def peek(self):
    if self.isEmpty():
        print("Cannot peek at an empty stack")
    else:
        return self._theItems[-1]

  # Removes and returns the top item on the stack.
  def pop(self):
    if self.isEmpty():
        print("Cannot pop from an empty stack")
    else:
        return self._theItems.pop()

  # Push an item onto the top of the stack.
  def push(self,item):
    self._theItems.append(item)

# Execution
PROMPT = "Enter an int value (<0 to end):"
myStack = Stack()
value = int(input(PROMPT))
while value >= 0 :
	myStack.push(value)
	value=int(input(PROMPT))
print("Length of Stack:",len(myStack))
while not myStack.isEmpty() :
	value = myStack.pop()
	print(value)
myStack.pop()
print("Length of Stack:",len(myStack))
myStack.push('james')
myStack.push('willam')
myStack.push('smith')
myStack.push('abby')
print("Peek at top:",myStack.peek())
print("Length of Stack:",len(myStack))
print(myStack.pop())
print("Length of Stack:",len(myStack))
print(myStack.pop())
print("Length of Stack:",len(myStack))
print(myStack.pop())
print("Length of Stack:",len(myStack))