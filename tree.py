class node:
    def __init__(self,v):
        self.value= v 
        self.leftChild:node =None
        self.RightChild:node =None
        
class BinarySearchTree:
    
    def __init__(self):
        self.__nodes=[]
        self.root:node=None
    def insert(self,value):
        if self.root is None:
            self.root = node(value)
        else:
            current_root =self.root
            while True:
                if value == current_root.value:
                    raise AssertionError(f"{value} already exists try adding a different value")
                
                if value < current_root.value:
                    if current_root.leftChild is None:
                        current_root.leftChild = node(value)
                        break
                    current_root = current_root.leftChild
                elif value > current_root.value: 
                        if current_root.RightChild is None:
                            current_root.RightChild = node(value)
                            break
                        current_root = current_root.RightChild
        
    def height(self):
        return self.__h(self.root)
    def __h(self,r:node):
        if r is None:
            return -1
        left_side = self.__h(r.leftChild)
        right_side = self.__h(r.RightChild)
        return 1 + max(left_side,right_side)
                   
    def find(self,v):
        return self.__f(self.root,v)
    def __f(self,r:node,v):
            if r is None:
                return False
            if r.value == v:
                return True
            if r.value == v:
                return True
            if v < r.value:
                return self.__f(r.leftChild,v)
            if v > r.value:
                return self.__f(r.RightChild,v)
        
    def min(self):
        return self.__m(self.root)
    def __m(self,r:node):
        if r is None:
            return 0
        if r.leftChild.leftChild == None:
            return r.leftChild.value
        return self.__m(r.leftChild)
            
    def max(self):
        return self.__mx(self.root)
    def __mx(self,r:node):
        if r is None:
            return 0
        if r.RightChild.RightChild == None:
            return r.RightChild.value
        return self.__mx(r.RightChild)
        
    def equals(self,tree):
        return self._e(self.root,tree.root)
    def _e(self,n,n2):
        if n is None and  n2 is None:
            return True
        if n is None or n2 is None:
            return False
       
        if n.value != n2.value:
            return False
        return self._e(n.leftChild,n2.leftChild) and  self._e(n.RightChild,n2.RightChild)
        
    def getNodesAtDistance(self,d):
        return self.__calDistance(self.root,d)
    
    def __calDistance(self, r: node, d):
        if d == 0 and r is not None:
            if r.value is not None:
                self.__nodes.append(r.value)
            return self.__nodes

        if r is None:
            
            return self.__nodes
        
        self.__calDistance(r.leftChild, d - 1)
        self.__calDistance(r.RightChild, d - 1)

        return self.__nodes
    
    def numEdges(self):
        return self.__edgesLeft(self.root,0) + self.__edgesRight(self.root,0)
    
    def __edgesLeft(self,root:node,count):
        count+=1
        if root is None:
            return count
        return self.__edgesLeft(root.leftChild,count) 
    
    def __edgesRight(self,root:node,count):
        if root is None:
            return count
        count+=1
        return self.__edgesRight(root.RightChild,count) 
                     
    






