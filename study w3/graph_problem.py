#!/usr/bin/env python
# coding: utf-8

# In[20]:


V = [0,1,2,3,4,5,6,7,8,9]
E = [(0,1), (1,4), (1,5), (4,6), (5,6), (5,7), (6,9), (7,8), (2,3)]


# In[27]:


from collections import deque


# In[38]:


class undi_graph():
    
    def __init__(self, V:list, E:list) -> None:
        self.V = V[:]
        self.neighbor = {}
        
        for v in V:
            self.neighbor[v] = []
        
        for (v, w) in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)
    
    
    def __DFTHelp(self, visited: list, v: int) -> None:
        if not visited[v]:
            visited[v] = True
            
            for w in self.neighbor[v]:
                self.__DFTHelp(visited, w)
                
            print(v)
    
    def DFT(self) -> None:
        if self.V:
            visited = {}
            
            for v in self.V:
                visited[v] = False
            
            for v in self.V:
                self.__DFTHelp(visited, v)
    
    
    def BFT(self) -> None:
        if self.V:
            visited = {}
            
            for v in self.V:
                visited[v] = False
            
            q = []
            
            for v in self.V:
                q.append(v)
                
                while q:
                    v = q.pop(0)
                    if not visited[v]:
                        visited[v] = True
                        print(v)
                        
                        for w in self.neighbor[v]:
                            q.append(w)
                        
                        #print(q)


# In[39]:


myGraph = undi_graph(V,E)


# In[40]:


myGraph.DFT()


# In[41]:


myGraph.BFT()

