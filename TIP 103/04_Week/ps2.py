# 10//8/26 Binary Trees & BST

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

print(survey_tree(magnolia))

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

print(sum_inventory(inventory))