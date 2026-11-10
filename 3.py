from collections import deque
'''
обходим дерево по уровням до первого найденного листа
'''
def min_depth_bfs(root):
    if root is None:
        return 0
    queue = deque([(root, 1)]) # очередь из пар - узел и глубина 
    while queue:
        node, depth = queue.popleft()
        if node.left is None and node.right is None: #нашли лист?
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
