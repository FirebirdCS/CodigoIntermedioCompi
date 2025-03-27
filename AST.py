class Node:
    pass

class BinOp(Node):
    def __init__(self, op, left, right):
        self.op = op      
        self.left = left  
        self.right = right  

class Num(Node):
    def __init__(self, value):
        self.value = value 
