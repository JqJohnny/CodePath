"""
Problem 1
Understand: Instantiate the class villager
Input:
Output:
Constraints:
"""

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

# apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)
# print(apollo.species)
# print(apollo.catchphrase)
# print(apollo.furniture)

"""
Problem 2
Understand: We need to add a greet player method.
Input: Player name
Output: Print statement.
Constraints:
"""


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20:
            for char in new_catchphrase:
                if not char.isspace() and not char.isalpha():
                    print("Invalid")
                    return
            
            self.catchphrase = new_catchphrase
            print("Updated Catchphrase!")
    

bones = Villager("Bones", "Dog", "yip yip")

print(bones.greet_player(bones.name))



alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

"""
Problem 9
Understand: We need to add a greet player method.
Input: Player name
Output: Print statement.
Constraints:
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy
print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 