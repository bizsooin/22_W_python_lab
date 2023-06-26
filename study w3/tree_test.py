#!/usr/bin/env python
# coding: utf-8

# In[2]:


class TreeNode():
    def __init__(self, x:int , k: int) -> None:
        self.val = x
        self.arity = k
        self.child = [None]*k


# In[3]:


class Tree():
    
    def __init__(self, root: TreeNode) -> None:
        self.root = root
    
    def visit(self, node: TreeNode):
        print(node.val)
        
    def BFT(self):
        if self.root == None:
            return
        
        q = [self.root]
        
        while q:
            curNode = q.pop(0)
            
            self.visit(curNode)
        
            for childNode in curNode.child:
                if childNode:
                    q.append(childNode)
    
    def __DFT_preorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        
        self.visit(curNode)
        
        for childNode in curNode.child:
            self.__DFT_preorderHelp(childNode)
            
        
    def DFT_preorder(self):
        self.__DFT_preorderHelp(self.root)
        
    
    def __DFT_inorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        
        for i in range(len(curNode.child)):
            if i == 1:
                self.visit(curNode)
            
            self.__DFT_inorderHelp(curNode.child[i])
        
    def DFT_inorder(self):
        self.__DFT_inorderHelp(self.root)
        
    
    def __DFT_postorderHelp(self, curNode: TreeNode):
        if curNode == None:
            return
        
        for i in range(len(curNode.child)):
            self.__DFT_postorderHelp(curNode.child[i])
        
        self.visit(curNode)
    
    def DFT_postorder(self):
        self.__DFT_postorderHelp(self.root)


# In[ ]:




