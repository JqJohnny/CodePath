"""
Problem 1
Understand:
Input: dictionary (key is the name, value is the integer)
Output: integer

Constraints:
"""

"""
def total_treasures(treasure_map):
    total = 0
    for treasure, value in treasure_map.items():
        total += value
        # print(treasure, value)
    return total

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2))
"""
"""
Problem 2
Understand: Use a set and count the length of the set
Input: String
Output: Boolean

Constraints:
"""
"""
def can_trust_message(message):
    unique = set(message)
    unique.remove(' ')
    if len(unique) == 26:
        return True
    
    return False
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
"""

"""
Problem 3
Understand:
Input: an array
Output: an array

Constraints:
seen = set()
duplicates = []
for x in chests:
if x in seen:
duplicates.append(x)
else:
seen.add(x)
return duplicates
"""
"""
def find_duplicate_chests(chests):
    freq = {}
    for x in chests:
        freq[x] = freq.get(x,0) + 1
    result = []
    for num,count in freq.items():
        if count == 2:
            result.append(num)
    return result

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
"""

"""
Problem 4
Understand:
Input:
Output:

Constraints:
"""
"""
def can_make_balanced(code):
    freq = {}
    for c in code:
        freq[c] = freq.get(c, 0) + 1
        
    #if set(freq.values()) != 2:
     #   return false
    #else:
     #   for c,v
    
    for c, v in freq.items():
        # print(v)
        
        freq[c] -= 1
        
        counts = set(freq.values())
        if len(counts) == 1:
            return True 
        
        freq[c] += 1
    return False


code1 = "arghh"
#[1,1,1,2] -> [1,2]
code2 = "haha"
#[2,2] -> [2]
code3 = "hahabbbccc"
#[2,2,3,3] -> [2,3] 
#   print(can_make_balanced(code1))
#print(can_make_balanced(code2)) 
#print(can_make_balanced(code3))
"""

"""
Problem 5
Understand:
Input: An integer array and an integer
Output: an array of two indicies

Constraints:
Plan: iterate the array, assume this item in the final result, and check if targets
- this item exist in the rest of the array
get index of item
"""


def find_treasure_indices(gold_amounts, target):
    print(gold_amounts, target)
    dictionary = {}
    for i, j in enumerate(gold_amounts):  # j = value
        # print(i,j)
        dictionary[j] = i
    print(dictionary)
    for k in dictionary.keys():
        if target - k in gold_amounts.remove(k):
            return [dictionary[k], dictionary[target - k]]


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))
print(find_treasure_indices(gold_amounts2, target2))
print(find_treasure_indices(gold_amounts3, target3))


"""
Problem 1
Understand:
Input: dictionary (key is the name, value is the integer)
Output: integer

Constraints:
"""
"""
def total_treasures(treasure_map):
    total = 0
    for treasure, value in treasure_map.items():
        total += value
        # print(treasure, value)
    return total

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2))
"""
"""
Problem 2
Understand: Use a set and count the length of the set
Input: String
Output: Boolean

Constraints:
"""
"""
def can_trust_message(message):
    unique = set(message)
    unique.remove(' ')
    if len(unique) == 26:
        return True
    
    return False
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
"""

"""
Problem 3
Understand:
Input: an array
Output: an array

Constraints:
seen = set()
duplicates = []
for x in chests:
if x in seen:
duplicates.append(x)
else:
seen.add(x)
return duplicates
"""
"""
def find_duplicate_chests(chests):
    freq = {}
    for x in chests:
        freq[x] = freq.get(x,0) + 1
    result = []
    for num,count in freq.items():
        if count == 2:
            result.append(num)
    return result

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
"""

"""
Problem 4
Understand:
Input:
Output:

Constraints:
"""
"""
def can_make_balanced(code):
    freq = {}
    for c in code:
        freq[c] = freq.get(c, 0) + 1
        
    #if set(freq.values()) != 2:
     #   return false
    #else:
     #   for c,v
    
    for c, v in freq.items():
        # print(v)
        
        freq[c] -= 1
        
        counts = set(freq.values())
        if len(counts) == 1:
            return True 
        
        freq[c] += 1
    return False


code1 = "arghh"
#[1,1,1,2] -> [1,2]
code2 = "haha"
#[2,2] -> [2]
code3 = "hahabbbccc"
#[2,2,3,3] -> [2,3] 
#   print(can_make_balanced(code1))
#print(can_make_balanced(code2)) 
#print(can_make_balanced(code3))
"""

"""
Problem 5
Understand:
Input: An integer array and an integer
Output: an array of two indicies

Constraints:
Plan: iterate the array, assume this item in the final result, and check if targets
- this item exist in the rest of the array
get index of item
"""


def find_treasure_indices(gold_amounts, target):
    print(gold_amounts, target)
    dictionary = {}
    for i, j in enumerate(gold_amounts):  # j = value
        # print(i,j)
        dictionary[j] = i
    print(dictionary)
    for k in dictionary.keys():
        if target - k in gold_amounts.remove(k):
            return [dictionary[k], dictionary[target - k]]


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))
print(find_treasure_indices(gold_amounts2, target2))
print(find_treasure_indices(gold_amounts3, target3))
