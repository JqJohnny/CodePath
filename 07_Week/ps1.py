"""
Understand:
Input: List of strings (suits)
Output: Integer
Constraints: Empty list,
"""


def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1

    return count


# def count_suits_recursive(suits):
#     if not suits:
#         return 0

#     return count_suits_recursive(suits[1:]) + 1


def count_suits_recursive(suits):
    index = 0
    def recurse(suits, index):
        if suits[index] >= suits[-1]:
            return 1

        return recurse(suits, index + 1) + 1
        
    return recurse(suits, index)



# plan:
# start from index 0
# recursively while calling functinon we move index by 1
# base case - if index == suits[-1]

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

"""
n [n-n]
.
.
.
call
call
call
call [n-2] <- subarray
call [n-1] 
"""

"""
Problem 2
Understand: We are using a recursive approach
Input: Array of integers
Output: Total power (int)
Time Complexity: O(n)
Space Complexity: O(n)
"""


# def sum_stones(stones):
#     def recurse(suits, index):
#         if index==len(suits):
#             return 0

#         return recurse(suits, index + 1) + suits[index]
        
#     return recurse(stones, 0)


def sum_stones(stones):
    if not stones:
        return 0
    
    return stones[0] + sum_stones(stones[1:])


print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))


"""
Problem 3
Understand: find distinct elemenst in list
Input: List of strings
Output: Total number of distinct suits in the list
Constraints:
    empty list, then count =0 
Plan:

"""
# This works
def count_suits_iterative(suits):
    distinct_set = set()
    for s in suits:
        distinct_set.add(s)
        
    return len(distinct_set)

def count_suits_recursive(suits):
    pass

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))