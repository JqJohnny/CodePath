# Problem 2

# Understand:
# Input:
# Output:
# Plan:


from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
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


# Problem 1

# Understand: Merge the two trees, and sum up any overlap
# Input: Two Trees
# Output: Merged Tree
# Plan: First check if trees are not valid --> return None
# then check individual trees, and if one is none --> return other Tree
# Both trees are valid --> sum both values, and assign to order1, then
# go left and right
# at the end, return order1

# class TreeNode():
#      def __init__(self, quantity, left=None, right=None):
#         self.val = quantity
#         self.left = left
#         self.right = right


def merge_orders(order1, order2):
    if order1 is None and order2 is None:
        return TreeNode(None)

    if order1 is None:
        return order2
    if order2 is None:
        return order1

    # If we get here, both tree nodes are valid
    print(f"order 1: {order1.val}")
    print(f"order 2: {order2.val}")
    order1.val += order2.val
    print(f"merged sum: {order1.val}")
    order1.left = merge_orders(order1.left, order2.left)
    order1.right = merge_orders(order1.right, order2.right)

    return order1


# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page


# Problem 2

# Understand: We are given a root, print a list of flavors by level
# Input: Root of binary tree (Design)
# Output: Flavors in levels order (list)
# Plan: Breadth first search, deque
# Add vanilla, iterate until queue empty
# [Vanilla]


class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def print_design(design):
    result = []
    queue = deque([design])
    while queue:
        curr = queue.popleft()
        result.append(curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return result


croquembouche = Puff(
    "Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry")
)

print(print_design(croquembouche))

# Space and Time complexity: O(N)


# Problem 3

# Understand: given a root of tree, return height of tree
# Input: root of binary tree (cake)
# Output: maximum number of tiers in cake (height)
# Plan:
# start from root
# if root is none: return 0
# return 1 + max ()


def max_tiers(cake):
    pass


# Using build_tree() function included at top of page
cake_sections = [
    "Chocolate",
    "Vanilla",
    "Strawberry",
    None,
    None,
    "Chocolate",
    "Coffee",
]
cake = build_tree(cake_sections)

print(max_tiers(cake))
