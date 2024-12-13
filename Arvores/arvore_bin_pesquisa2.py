class TreeNode: 
   def __init__(self,key,val,left=None,right=None,parent=None): 
        self.key = key 
        self.value = val 
        self.leftChild = left 
        self.rightChild = right 
        self.parent = parent 
 
 
class Tree: 
    def __init__(self): 
        self.root = None 
        self.size = 0 
 
    def method1(self,key,val): 
        if self.root: 
            self.method2(key,val,self.root) 
        else: 
            self.root = TreeNode(key,val) 
        self.size = self.size + 1 
 
    def method2(self,key,val,currentNode): 
        if key < currentNode.key: 
            if currentNode.leftChild: 
                self.method2(key,val,currentNode.leftChild) 
            else: 
                currentNode.leftChild = TreeNode(key,val,parent=currentNode) 
        else: 
            if currentNode.rightChild: 
                self.method2(key,val,currentNode.rightChild) 
            else: 
                currentNode.rightChild = TreeNode(key,val,parent=currentNode) 
 
    def method3(self,key): 
        if self.root: 
            response = self.method4(key,self.root) 
            if response: 
                return response.value 
            else: 
                return None 
        else: 
            return None 
            
    def method4(self,key,currentNode): 
        if not currentNode: 
            return None 
        elif currentNode.key == key: 
            return currentNode 
        elif key < currentNode.key: 
            return self.method4(key,currentNode.leftChild) 
        else: 
            return self.method4(key,currentNode.rightChild) 
        
    def method5(self): 
        if self.root: 
            self.method6(self.root) 

    def method6(self,currentNode): 
        if currentNode: 
            self.method6(currentNode.leftChild) 
            print(currentNode.value, end = "") 
            self.method6(currentNode.rightChild) 

mytree = Tree() 
mytree.method1(25,"a") 
mytree.method1(17,"e") 
mytree.method1(21,"g") 
mytree.method1(50,"a") 
mytree.method1(8,"r") 
mytree.method1(36,"l") 
mytree.method1(40,"i") 
var = mytree.method3(50) + mytree.method3(36) + mytree.method3(25) 
print (var) 
mytree.method5()
