# """
# Input: head of a linked list
# Output: Boolean
# """

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     ans_set = set()
#     current = clues
#     while current:
#         if current.value not in ans_set:
#             ans_set.add(current.value)
#         else:
#             return True
#         current = current.next
        
#     return False

# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = None

# print(is_circular(clue1))

"""
Problem 2
Input: Head of linked list
Output: Return an array
Constraints:
"""

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_false_evidence(evidence):
#     ans_array = []
#     ans_set = set()
#     current = evidence
#     prev = None
#     while current:
#         if current.value not in ans_set:
#             ans_set.add(current.value)
#             prev = current
#         else:
#             # Store the end/start of the loop
#             ans_array.append(current.value)
#             if current == prev:
#                 break
#         current = current.next


#     return ans_array

# clue1 = Node("Unmarked sedan seen near the crime scene")
# clue2 = Node("The stolen goods are at an abandoned warehouse")
# clue3 = Node("The mayor is accepting bribes")
# clue4 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue4
# clue4.next = clue2

# clue5 = Node("A masked figure was seen fleeing the scene")
# clue6 = Node("Footprints lead to the nearby woods")
# clue7 = Node("A broken window was found at the back")
# clue5.next = clue6
# clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

"""
Problem 3
Understand: Values greater than (exclusive) threshhold
Input: Head of linked list
Output: Return head of partitioned list,
Constraints:
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    current = suspect_ratings
    new_list = Node(0)
    while current:
        if current.value > threshold:
            new_list.next = current
        current = current.next


suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))