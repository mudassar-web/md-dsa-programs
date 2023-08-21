#Aim : Implementation of the Queue using a Python list.

class Queue:
# Creates an empty queue.
  def __init__(self):
    self.qList=list()

#Returns True if the queue is empty.
  def isEmpty(self):
    return len(self) == 0

# Returns the number of items in the queue.
  def __len__(self):
    return len(self.qList)

# Adds the given item to the queue.
  def enqueue(self,item):
    self.qList.append(item)

# Removes and returns the first item in the queue.
  def dequeue(self):
    if self.isEmpty():
      print("Cannot dequeue from an empty queue.")
    else:
      return self.qList.pop(0)

def main():
  Q=Queue()
  Q.enqueue(1)
  Q.enqueue(2)
  Q.enqueue(3)

  print("Length:",len(Q))
  
  print("1st Element=",Q.dequeue())
  print("2nd Element=",Q.dequeue())
  print("3rd Element=",Q.dequeue())

main()