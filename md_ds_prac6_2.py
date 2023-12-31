class BinaryTree():
    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setNodeValue(self,value):
        self.rootid = value
        
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left
            
    def printTree(self):
        if self != None:
            print(self.getLeftChild())
            print(self.getNodeValue())
            print(self.getRightChild())

# test tree
def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    myTree.printTree()

testTree()