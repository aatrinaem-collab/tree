def maxMinMultiplication(data):
    if not data:
        return -1

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    #bst делаем
    def insert(root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)

        return root

    root = None
    for value in data:
        root = insert(root, value)
    min_node = root
    #ищем минимум - он самый левый по пути - не больше O(h) шагов
    while min_node.left is not None:
        min_node = min_node.left
    max_node = root
    #макс - он самый правый (аналогично)
    while max_node.right is not None:
        max_node = max_node.right

    return min_node.value * max_node.value

data = [8, 3, 10, -1, 6, 14, 4, 7, 13]
result = maxMinMultiplication(data)
print(result)  # 14
