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


def merge_list(list1, list2):
    head = curr = Node(0)

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return head.next


l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])

print(print_list(merge_list(l1, l2)))


# Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6
