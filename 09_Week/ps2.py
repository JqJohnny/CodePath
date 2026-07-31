from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root


"""
Write a function to return the zigzag level order traversal of a binary tree.
In a zigzag traversal, the nodes are visited level by level, but the direction
alternates between left-to-right and right-to-left for each level.

Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]

Explanation:
Level 1: [3] (left-to-right)
Level 2: [20, 9] (right-to-left)
Level 3: [15, 7] (left-to-right)

plan: 

if not root:
    return []
queue = deque{[root]}
stack = []
arrays = []
counter = 0

while queue or stack:
    if counter % 2 == 0: # use queue
        values = []
        while queue:
            curr = queue.popleft()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            values.append(curr)
        arrays.append(values)

    else: # use stack
        values = []
        while stack:
            curr = stack.pop()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            values.append(curr)
        arrays.append(values)
    counter += 1

return arrays





"""


def zigzag(root):
    if not root:
        return []
    queue = deque([root])
    stack = []
    arrays = []
    counter = 0

    while queue or stack:
        values = []
        if counter % 2 == 0:  # use queue
            while queue:
                curr = queue.popleft()
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                values.append(curr.val)
            arrays.append(values)

        else:  # use stack
            while stack:
                curr = stack.pop()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                values.append(curr.val)
            arrays.append(values)
        counter += 1

    return arrays


def zigzag_tree(root, level, result):
    if root is None:
        return result

    if len(result) <= level:
        result.append(deque())

    if level % 2 == 0:
        result[level].append(root.val)
    else:
        result[level].appendleft(root.val)

    zigzag_tree(root.left, level + 1, result)
    zigzag_tree(root.right, level + 1, result)

    return [list(d) for d in result]


tree_with_just_values = [1, 2, 3, 4, None, 5, 6]
val_tree = build_tree(tree_with_just_values)

print(zigzag(val_tree))

tree = [3, 9, 20, None, None, 15, 7]
tree_built = build_tree(tree)

# print(zigzag_tree(val_tree, 0, result=[]))

print(zigzag(tree_built))

"""
Problem 1
Understand: A balanced display is a binary tree in which the difference in 
the height of the two subtrees of every node never exceeds one.
Input: root of binary tree
Output: Boolean, True if balanced, false otherwise
Constraints: Empty Tree
"""


def is_balanced(display):
    if display is None:
        return True

    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    left = height(display.left)
    right = height(display.right)

    return abs(left - right) <= 1 and is_balanced(display.left) and is_balanced(display.right)

        


baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"]
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \"
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)

print(is_balanced(display1)) 
print(is_balanced(display2))

