# 10//8/26 Binary Trees & BST
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# print_tree helper function
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
    # gets rid of the None child for the leaf nodes 
    while result and result[-1] is None:
        print(result.pop())
    print(result)

# Instructor demo


"""
          1
        /   \
       2     3
      /     / \
     4     5   6
"""

# root = Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))
# print_tree(root)


"""
Problem 1
U:
Input: Root
Output: A list of the path from root to the Rightmost child
M:
Tree
P:

I:
R:
E:
"""
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  result = []
  while root:
    result.append(root.val)
    root = root.right

  return result

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
'''
"""
Set1, #2
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    path = []

    def traverse(node):
        if node is None:
            return
    
        path.append(node.val)
        traverse(node.right)

    traverse(root)

    return path

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))


"""
Problem 3
You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, 
you need to do a full survey of the tree to evaluate which sections need to be pruned.

Given the root of a binary tree representing the magnolia, return a list of the values of each node 
using a postorder traversal. In a postorder traversal, you explore the left subtree first, then the 
right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree.

Evaluate the time and space complexity of your function. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity. Assume 
the input tree is balanced when calculating time and space complexity.

"""
def survey_tree(root):
    vals = []
    def post_order_traverse(node):
        if node is None: # leaf node
            return # node.val
        
        if node.left:
            post_order_traverse(node.left)

        if node.right:
            post_order_traverse(node.right)
            
        vals.append(node.val)

    post_order_traverse(root)
    return vals

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))

def sum_inventory(inventory):
  counting_sum = 0
  def post_order_traverse(node):
    nonlocal counting_sum
    if node is None: # leaf node
        return # node.val
    
    if node.left:
        post_order_traverse(node.left)

    if node.right:
        post_order_traverse(node.right)
        
    counting_sum += node.val

  post_order_traverse(inventory)
  return counting_sum

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

# print(sum_inventory(inventory))

# cont'd problem 5
"""
Set1, #5
UNDERSTAND: 

The yield of the tree is calculated as follows:

If the node is a leaf node, the yield is the value of the node.
Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
> Input: root of binary tree
> Output: integer
> Edge cases:
MATCH:
Binary tree (post-order traversal)
PLAN:
Post-order traversal
Look at the left and right children, does the mathematical operation and returns
the current value.
REVIEW:
EVALUATE: Time: O(N), Space: O(H) H: height of tree
"""
def calculate_yield(root):
    if root.left is None and root.right is None:
        return root.val
    
    left = calculate_yield(root.left) 
    right = calculate_yield(root.right)
    return eval(str(left) + root.val + str(right))



root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

"""
Set1, #6
UNDERSTAND:
> Input: root of a binary tree
> Output: list of leave vals
> Edge cases: root -> return [root.val]
MATCH: DFS (root -> left -> right)
PLAN:
lst = []
helper function: pre-order DFS
DFS pre-order implemetation  

REVIEW:
EVALUATE: O(n) time; O(H) space
"""
def get_most_specific(taxonomy):
    lst = []

    def DFS_preorder(root):
        if root is None:
            return 
        if root.left is None and root.right is None:
            lst.append(root.val)
            return

        # left traversal
        DFS_preorder(root.left)

        # right traversal
        DFS_preorder(root.right)

    DFS_preorder(taxonomy)

    return lst
    


#            Plantae
#           /       \
#          /         \
#         /           \ 
# Non-flowering     Flowering
#    /      \       /        \
# Mosses   Ferns Gymnosperms Angiosperms
#                              /     \
#                         Monocots  Dicots


plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

# print(get_most_specific(plant_taxonomy))

"""
Set1, #7
UNDERSTAND:
> Input: threshold and root of tree
> Output: return int (number of old growth trees)
> Edge cases: if node.left and node.right is none, return.  if root is none, return.
MATCH:
PLAN: if node is > threshold, increment count
REVIEW:
EVALUATE:
"""
def count_old_growth(root, threshold):
    if root is None:
        return 0

    left = count_old_growth(root.left, threshold)
    right = count_old_growth(root.right, threshold)

    if root.val > threshold:
        return 1 + left + right

    return left + right

    


#      100
#      /  \
#     /    \
#   1200  1500
#   /     /  \
# 20    700  2600


forest = TreeNode(100, TreeNode(1200, TreeNode(20)), TreeNode(1500, TreeNode(700), TreeNode(2600)))

# print(count_old_growth(forest, 1000))

"""
Set1, #8
UNDERSTAND: 
> Input: Two binary tree roots
> Output: Boolean 
> Edge cases:
MATCH:
PLAN:
Recurse through both at the same time
and compare values
REVIEW:
EVALUATE: 
"""

def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None or root1.val != root2.val:
        return False

    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)


    #   1                1
    #  / \              / \
    # 2   3            2   3  

root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))


    #   1                1
    #  /                  \
    # 2                    2  


root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))

root5 = TreeNode(1, TreeNode(2))
root6 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))