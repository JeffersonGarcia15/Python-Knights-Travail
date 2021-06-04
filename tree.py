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
            # add root2 to root1's array of children, root1 is the parent of root2
            #node1.add_child(node2) node1 is self, node2 is node node2's parent is self=node1
            
    
    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None
        
        
    @property
    def parent(self):
        return self._parent
    
    
    @parent.setter
    def parent(self, node):
        if self._parent == node:
            return
        if self._parent:
            self._parent.remove_child(self)
        self._parent = node # self is node2
        if self._parent:
            node.add_child(self)
    
    
    def depth_search(self, value):
        if self._value == value:
            return self
        for child in self._children:
            # if child:
            node = child.depth_search(value)
            if node is not None:
                return node
        # return None


    def breadth_search(self, value):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current._value is value:
                return value
            # for child in current._children:
            queue.extend(current._children)
                # queue.append(child)
                
    
    def __repr__(self):
        return f'<Node {self.value}>'
    
    
    
# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
