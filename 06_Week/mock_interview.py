"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return " -> ".join(result) if result else "Empty"

l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])

head = l1
l3 = []
while l1:
    l3.append(l1)
    l1 = l1.next
    if l2.next:
        l3.append(l2)
        l2 = l2.next


print_list(l3)

# Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6