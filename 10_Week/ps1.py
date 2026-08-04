"""
Problem 1 - Slides

Write a function to perform a level order traversal (breadth-first search) of a binary tree and
return the values of the nodes in level order as a list of lists. Each inner list should represent
the values of the nodes at that level.
Example:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

understand:
given the root of a binary tree, return a list of lists of nodes, where each inner list represents the nodes on each level of the tree

match:
level order traversal
nested loop to keep track of the level

plan:
implement a regular level order traversal
have a separate length variable for the length of the queue
the length will be a marker for the end of each level
in an inner for loop, start with an empty list and keep appending nodes until the length var is reached
append that list to the result list
return the result list

"""

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


def level_order(root):
    result = []

    if not root:
        return result

    queue = deque([root])

    while queue:
        length = len(queue)
        curr_list = []

        for i in range(length):
            node = queue.popleft()
            curr_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(curr_list)

    return result


# root = [3, 9, 20, None, None, 15, 7]
# tree = build_tree(root)

# print(level_order(tree))

"""
Problem 2 - Slides

Write a function to find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Example:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 2
understanding:
find the minimum depth and return but the number
Match:
transversal
plan:
 find the length of all the nodes and

 helper(root, level)


"""

"""
def maxdepth(root):
    if not root: return 0
    return 1 + max(maxdepth(root.left), maxdepth(root.right))
"""


def mindepth(root):
    if not root:
        return 0
    return 1 + min(mindepth(root.left), mindepth(root.right))


# root = [3, 9, 20, None, None, 15, 7]
# tree = build_tree(root)

# print(mindepth(tree))


"""
Problem 1
Understand: Building a graph with each node and vertex representing an airport.
We want to create variable flights that represent the undirected graph
"""

# flights = {"JFK": ["LAX", "DFW"],
#             "LAX": ["JFK"],
#             "DFW": ["JFK", "ATL"],
#             "ATL": ["DFW"]}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

"""
Problem 2
As a flight coordinator for CodePath airlines, 
you have a 0-indexed adjacency list flights with n nodes
where each node represents the ID of a different destination 
and flights[i] is an integer array indicating that 
there is a flight from destination i to each destination in flights[i]. 
Write a function bidirectional_flights() that 
returns True if for every flight from a destination i to a destination j 
there also exists a flight from destination j to destination i. Return False otherwise.
"""


def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


# flights1 = [[1, 2], [0], [0, 3], [2]]
# flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))


"""
Problem 3
Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent 
a distinct destination and n[i][j] = 1 indicates that there exists a flight from destination 
i to destination j and n[i][j] = 0 indicates that no such flight exists. Given flights and an integer source 
representing the destination a customer is flying out of, return a list of all destinations the customer can reach from source
 on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.

Understand:
 Using the source we can get the specific array from the index
giving the direct routes
The direct routes are given in as a list where each index represents a direct route
Input: Flights (adjacency matrix) and source (int),
Output: List of direct flights
Constraints:

Plan: Use the source mapped to flights, and get the specfic routes for that airport
append that index if the value is 1 (direct route exists)

return result
"""


def get_direct_flights(flights, source):
    result = []
    source_array = flights[source]
    for i in range(len(source_array)):
        if source_array[i]:
            result.append(i)

    return result


# flights = [
#             [0, 1, 1, 0],
#             [1, 0, 0, 0],
#             [1, 1, 0, 1],
#             [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))

"""
Problem 4
Given a list of edges flights where flights[i]
 = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) from city a to city b,
  return an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] is an array denoting
   there is a flight from city a to each city in adj_dict[a].
understanding:
make a dictionary with the cities in the list the dictionary key will be the name of the city 
and the dictionary value is the still the name of the city but its a list of cities that can be vistted
Match :
make a dictionary ,use a for loop to go though the list
plan:
create an empty dictionary named adj_dict go through the list if the city is not in dictionary
 append it in the dictonary with an empty list  
 if its already in the dictionary
"""

"""
We can use a set, that way we dont get duplicates and change it to a list after

"""


def get_adj_dict(flights):
    pass


flights = [
    ["Cape Town", "Addis Ababa"],
    ["Cairo", "Lagos"],
    ["Lagos", "Addis Ababa"],
    ["Nairobi", "Cairo"],
    ["Cairo", "Cape Town"],
]
print(get_adj_dict(flights))
