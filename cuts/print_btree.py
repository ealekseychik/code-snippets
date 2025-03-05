# Print a binary tree going down levels changing direction every level
# (from left to right then right to left then left to right then right to left)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_btree(root_node: TreeNode) -> None:
    queue = deque([root_node])
    right2left = False
    while queue:
        level_len = len(queue)
        level_vals = []
        for _ in range(level_len):
            node = queue.popleft()
            level_vals.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        if right2left:
            level_vals.reverse()

        right2left = not right2left
        print(level_vals)
