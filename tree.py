class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []
        
        
    @property
    def value(self):
        return self._value
    
    
    @property
    def children(self):
        return self._children
    
    
    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self
            
    
    def remove_child(self, node):
        self._children.remove(node)
        node.parent = None
        
        
    @property
    def parent(self):
        return self._parent
    
    
    @parent.setter
    def parent(self, node):
        self._parent = node
        self.add_child(node)
        

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
