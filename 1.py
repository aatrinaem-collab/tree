class TreeNode:
    def __init__(self, val=0, left=None, right=None): #это структура используется
        self.data = val
        self.left = left
        self.right = right

def build_tree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1) # левый потомок - так определяется связь родитель-потомок
    root.right = build_tree(arr, 2 * i + 2) # правый
    
    return root

arr = [1, 2, 3, 4, 5, 6, 7]
tree_root = build_tree(arr, 0)
