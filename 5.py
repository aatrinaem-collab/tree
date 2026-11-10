class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSameTree(a, b):
    if a is None and b is None: #либо обоих узлов нет
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False 
    # иначе оба есть и равны - сравниваем их поддеревья

    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right) 

a = Node(1)
a.left = Node(2)
a.right = Node(3)
b = Node(1)
b.left = Node(2)
b.right = Node(3)

print(isSameTree(a, b))  
