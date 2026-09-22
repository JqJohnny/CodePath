"""
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list with the name of all friends the current villager and new_contact have in common.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        pass
Example Usage:

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))
Example Output:

['Raymond', 'Fauna']
[]

Understand:
Plan: Loop thorough self, in new_contract
Input: Two instances of the class Villager
Output: Return a list with names of all friends in common
Constraints:
"""


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        result = []
        for friend in self.friends:
            if friend in new_contact.friends:
                result.append(friend.name)
        return result


bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))

"""
Problem 2

A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.

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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
Example Usage:

print_linked_list(kk_slider)
Example Output:

K.K. Slider -> Harriet -> Saharah -> Isabelle

Understand:
Plan: Start from the head node, print each node sequentially until reaching the end of the list
Input: linked list head
Output: Print of the linked list starting from the head
Constraints: List could be empty
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


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)

"""
Problem 3
Understand: write add task() takes in the head (node) of a linked list, we want to add a node to the front of their tas klist
Plan: make the task nodes next the head of the linked list
Input: head of a linked list (node)
Output: return the new node
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


def add_first(head, task):
    new_task = Node(task)
    new_task.next = head
    return new_task


task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))

"""
Problem 4
Understand: Iterate through linked list, divide each value by 2
Plan: Start with head node, move through list in while loop dividing by 2, set curr_node to curr_node.next
Input: head_node: Node[int]
Output: head_node: Node[int]
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


def halve_list(head):
    curr = head
    while curr:
        curr.value = curr.value / 2
        curr = curr.next
    return head


# Example Usage
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

"""
Problem 5
Understand: We are removing the tail.
Plan: Start with head and iterate through and we are going to check one ahead to see if its null.
If its None we know its the end and we can remove the tail.
Input: Head of list
Output: Head of modified list
Constraints: If the list is only one node
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


def delete_tail(head):
    node = head
    if node.next is None:
        return head

    while node.next.next is not None:  # 1 off
        node = node.next

    node.next = None
    return head


butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))

"""
Problem 6
Understand: Find the minimum value in the linked list
Plan: Start at the head, iterate through every node while keeping track of the smallest value seen so far
Input: Head of a linked list
Output: Minimum value of the linked list
Constraints: List could be empty -> None, List only have one value -> return that value
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


def find_min(head):
    current_minimum = float("inf")
    current_node = head
    while current_node:
        if current_node.value < current_minimum:
            current_minimum = current_node.value

        current_node = current_node.next

    return current_minimum


head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

"""
Problem 7
Understand: delete the node with the matching name from the linked list 
Plan:go through the linked list starting at head, check if curr_val.value == item, if it is prev next equal to curr.next
Input: head (node), item (str)
Output: return the head of the list
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


def delete_item(head, item):

    if head.value == item:
        head = head.next
        return head

    prev = head
    curr = head.next

    while curr:
        if curr.value == item:
            prev.next = curr.next  # bypass current node
            return head
        curr = curr.next
    return head


slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))

"""
Problem 8
Understand: We want to find the last node, set it as the new head.
Plan: Iterate the list, stop at the second to last node, outside the loop, 
assign that node to the head and set the second to last node.next to None
Input: 
Output: 
Constraints:
"""


def tail_to_head(head):
    curr = head
    while curr.next:
        curr = curr.next


daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad")
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
print_linked_list(tail_to_head(daisy))
