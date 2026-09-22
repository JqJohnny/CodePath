"""
Problem 1
Understand: were given a root of binary tree and we want to return all nodes with odd numbers
Input: root
Output: int
Constraints: empty tree node

plan: inorder traversal at each node check the value if the values odd we increment the odd leaf counter
after we return that

time complexity: 0(n)
space : 0(n)
"""

"""
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, 
return the number of Monstera leaves 🍃 that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe 
your solution has the stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf
 nodes which are nodes with no children.
"""
from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


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


def count_odd_splits(root):
    if root is None:
        return 0
    if root.left and root.left.val % 2 == 1:
        return count_odd_splits(root.left) + 1
    if root.right and root.right.val % 2 == 1:
        return count_odd_splits(root.right) + 1
    if root.val % 2 == 1:
        return 1
    if root.left:
        return count_odd_splits(root.left)
    if root.right:
        return count_odd_splits(root.right)

    return 0


# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

"""
Problem 2
Understand: We are starting at the root and we need to find a specific flower given alphabetical order
Input: Root of binary search tree "inventory", Target "flower"
Output: Boolean based on if flower is present or not
Constraints: Empty tree

Plan: Convert the the characters to an integer and compare to the target.
If we know the target is greater then its on the right otherwise on the left
"""


"""
Example Output:

3
Example 1 Explanation: Three Monstera leaves (nodes) have an odd number of fenestrations (3, 5, and 7).
0
"""
"""
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a
binary search tree (BST) where each node represents a plant in the store. The plants are organized according 
to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower()
that returns True if the flower is present in the garden and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time 
complexity.
"""
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    if inventory.val > name:
        return find_flower(inventory.left, name)
    elif inventory.val < name:
        return find_flower(inventory.right, name)

"""
'''
Example Usage:

"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""
'''
# using build_tree() function at top of page
"""""" """
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))
""" """"""
# Example Output:

# True
# False

"""
U: Input: Root of binary tree (not bst)
    Output: True/false


P:  Traverse entire tree, return True if found, False otherwise


"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def non_bst_find_flower(root, name):
    if root is None:
        return False

    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)


# Example Usage:

"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))
print(non_bst_find_flower(garden, "Sunflower"))
# Example Output:

# True
# False
"""
understand: we want to insert the plant into tree where it belongs, if it already exists there make it the already existing nodes right child
match: binary serach to find the location
input: root, name to insert
output: return root
plan: use binary search to find location, if node exists make new one right child just insert at desired location
"""


def add_plant(collection, name):
    curr = collection
    while curr:
        if curr.val == name:
            temp = curr.left
            curr.left = name
        if curr.val > name:
            curr = curr.left
        if curr.val < name:
            curr = curr.right


# Example Usage:

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))
# Example Output:

# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']
"""
Explanation: 
Tree should have the following structure:
           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe
 """
