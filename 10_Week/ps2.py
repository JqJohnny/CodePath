'''
Problem 1
# U - Understand the problem
         # I: Inputs - Adjacency matrix, source, destination
         # O: Outputs - Boolean (true or false) True if there is a path from current location
         # Otherwise false
         # C: Constraints
         # E: Edge Cases

#M - Match (have you seen this problem before?)

# P - Plan your approach (written plan or pseudo code)
"""
Find a direct connection or a path there
Build a stack of possible routes,
Popping from the stack, add the next possible locations,
if at any point in the stack we are adding the destination we can return true
"""

# I - Implement

# R - Review (test run the code)

# E - Evaluate (time and space complexity?)
from collections import deque

def can_rebook(flights, source, dest):
    stack = deque([flights[source]])
    while stack:
        for index in range(len(stack[0])): # [0, 1, 0]
            if stack[0][index]: # True
                if index == dest:
                    return True
                stack.append(flights[index])
        stack.popleft()

    return False



flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))


'''
# Problem 2
# U - Understand the problem
# I: Inputs - Adjacency matrix, source, destination
# O: Outputs - Boolean (true or false) True if there is a path from current location
# Otherwise false
# C: Constraints
# E: Edge Cases

# M - Match (have you seen this problem before?)

# P - Plan your approach (written plan or pseudo code)
# dfs

# I - Implement

# R - Review (test run the code)

# E - Evaluate (time and space complexity?)
"""

def can_rebook(flights, source, dest):
    if source == dest:
        return True
    visited = set()
    def dfs(node):
        if node == dest:
            return True
        visited.add(node)
        for j in range(len(flights[node])):
            if flights[node][j] == 1 and j not in visited:
                if dfs(j):
                    return True
        return False
    return dfs(source)

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 

"""

# Problem 3
# U - Understand the problem
# I: Inputs - Adjacency matrix, start airport, destination airport
# O: Outputs - The minimum number of flights needed to reach the destination airport, if not possible, return -1
# C: Constraints
# E: Edge Cases

# M - Match (have you seen this problem before?)

# P - Plan your approach (written plan or pseudo code)
# dfs

# I - Implement

# R - Review (test run the code)

# E - Evaluate (time and space complexity?)

from collections import deque


# def counting_flights(flights, i, j):
#     queue = deque([flights[i]])
#     visited = {flights[i]}
#     n = len(flights)
#     if i == j:
#         return 0
#     count = 0
#     while queue:
#         count += 1
#         level_size = len(queue)
#         for index in range(level_size):  # [0, 1, 0]
#             node = queue.popleft()
#             for k in range(n):
#                 if flights[node][k] == 1 and k not in visited:  # True
#                     if k == j:
#                         return count
#                     visited.add()
#                 nextlevel.append(flights[index])
#         queue.popleft()
#         # if stack is empty
#         stack = deque(nextLevel)
#     return -1


# Example usage
# flights = [
#     [0, 1, 1, 0, 0],  # Airport 0
#     [0, 0, 1, 0, 0],  # Airport 1
#     [0, 0, 0, 1, 0],  # Airport 2
#     [0, 0, 0, 0, 1],  # Airport 3
#     [0, 0, 0, 0, 0],  # Airport 4
# ]

# print(counting_flights(flights, 0, 2))
# print(counting_flights(flights, 0, 4))


def counting_flights(flights, i, j):
    queue = [flights[i]]
    visited = set()
    count = 0
    while queue:
        count += 1
        nextlevel = []
        while queue:
            curr = queue.pop()
            for index in range(len(curr)):
                if curr[index]:
                    if index == j:
                        return count
                    nextlevel.append(flights[index])
        # if stack is empty
        queue = nextlevel

    return -1


flights = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0],  # Airport 4
]

print(counting_flights(flights, 0, 2))
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
