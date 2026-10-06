# 10/6: Linked Listts & Trees

"""
Set1, #1
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.personality = personality
        self.furniture = []
        self.neighbor = neighbor

    def add_item(self, item_name):
        valid = set(["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"])

        if item_name in valid:
            self.furniture.append(item_name)


# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# problem 3:
def of_personality_type(townies, personality_type):
  ret = []
  for townie in townies:
      # print(townie.personality)
      if townie.personality == personality_type:
          ret.append(townie.name)
  return ret
  
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

"""
Problem 4
U: We need to go from the starting villager to the target villager
using neighbors
Input: Two villager objects
Output: Boolean - Whether the villagers are reachable
M: iterate through neighbors (for loop or while loop)
P: iterate through neighbors
I:
R:
E:
"""
'''
def message_received(start_villager, target_villager):
    villager = start_villager
    while villager.neighbor:
        if villager.neighbor == target_villager:
            return True
        villager = villager.neighbor

    return False                


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))


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
'''

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head is None:
        print("Aw! Better luck next time!")
        return None

    print(f"I caught a {head.fish_name}!")
    head = head.next

    return head



# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# Carp -> Dace -> Cherry Salmon
# I caught a Carp!
# Dace -> Cherry Salmon
# Aw! Better luck next time!
# None

def fish_chances(head, fish_name):
    if head is None:
        return round(0, 2)

    counter = 0
    fish_name_occurrences = 0 # duplicates/existence
    while head is not None:

        name = head.fish_name 

        if name == fish_name:
            fish_name_occurrences += 1

        counter+=1
        head = head.next
    
    if fish_name_occurrences == 0:
        return round(0, 2)
    
    return round(fish_name_occurrences/counter, 2)


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

# problem 8
def restock(head, new_fish):
  dummy_head = Node("")
  dummy_head.next = head
  curr = dummy_head
  while curr.next:
      curr = curr.next
  curr.next = Node(new_fish)
  return dummy_head.next   
  
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))

"""
Problem 1 - Set 2
"""
class Player:
    def __init__(self, character, kart):
        pass

player_one = Player("Yoshi", "Super Blooper")
print(player_one.character)
print(player_one.kart) 
print(player_one.items)