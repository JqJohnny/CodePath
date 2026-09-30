# You're working at a deli, and need to count the layers of a sandwich to make sure 
# you made the order correctly. Each layer is represented by a nested list. Given a 
# list of lists sandwich where each list [] represents a sandwich layer, write a 
# recursive function count_layers() that returns the total number of sandwich layers.

# Evaluate the time and space complexity of your solution. Define your variables 
# and provide a rationale for why you believe your solution has the stated time and space complexity.

# U: 
# - use recursion
# Input: nested lists
# Output: total # of sandwhich layers
# edge cases: if list is '[]', is zero?
# - assume valid input. Only brackets, assume closed brackets
# M: 
# - use recursion
# P:
# base case: if len of list is 1, return 1
# else let's traverse the nested lists
# implicit counter variable (return) to track layer count
# I: 
# R: 
# E: time complexity: O(N)
# space complexity: O(constant)

def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1
    return count_layers(sandwich[1]) + 1

#Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
#print(count_layers(sandwich2))
# Example Output:

# The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse 
# the order of the deli orders. Given a string orders where each individual order is separated by a single 
# space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
# for why you believe your solution has the stated time and space complexity.
"""
U: 
Input: String of orders
Output: String of orders in reverse
Assumption: Assume valid orders, split by spaces
M: Recursion
P: 
We use .split() to make a list of words
["Bagel", "Sandwich", "Coffee"]
Variable result = ""

I:
R:
E:
"""

def reverse_orders(orders):
    if orders == "" or len(orders) == 1:
        return orders
    list_of_orders = orders.split(" ")
    result = ""
    def helper(list_of_orders):
        nonlocal result
        if len(list_of_orders) == 0:
            return 0
        result += list_of_orders[-1] + ' '
        return helper(list_of_orders[:-1])

    helper(list_of_orders)
    return result

# print(reverse_orders("Bagel Sandwich Coffee"))
"""
Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
Example Output:

Coffee Sandwich Bagel
"""

"""The deli staff is in desperate need of caffeine to keep them going through their shift and 
has decided to divide the coffee supply equally among themselves. Each batch of coffee is 
stored in containers of different sizes and must remain whole when distributed among n staff. 
Write a recursive function can_split_coffee() that accepts a list of integers coffee representing 
the volume of each batch of coffee and returns True if the coffee can be split evenly by volume 
among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def can_split_coffee(coffee, n):
pass
Example Usage:

print(can_split_coffee([4, 4, 8], 2))
# total is 16. Even amount is 8. 
# check if each employee gets 8 without breaking down batches
# for batch 1: employee 1 gets 4
# for batch 2: employee 1 gets 4
# for batch 3: employee 3 gets 8

print(can_split_coffee([5, 10, 15], 4))
# total = 30, even = 30/4 = 7.5. return False immediately!

U: 
We are given batches of coffee, and when we are adding those coffee batches, their sum should be divisible by n.
(sum_of_bathces) % n == 0

Each coffee batch must be spilt evenly amongst employees
M:
1. Sum of elements in the list (recursion)
2. Regular % operation
Constraint: The batches are guaranteed to be an integer
P:
def can_split_coffee(coffee, n):
     # check if (sum_of_bathces) % n == 0: Return T/F

     total = variable which is the sum of array
     split = total / n
     isinstance(variable, float)
     def helper(coffee):
        # calculate the sum of coffee batches

I:
R:
E:
"""

def can_split_coffee(coffee, n):
    total = sum(coffee)
    if total % n != 0:
        return False
    split = total / n # The amount each employee should have
    quotas_completed = 0 # how many employees left to split batches amongst

    coffee.sort(reverse=True)
    if coffee[0] > split: # max number in batch is greater than split
        return False
    
    current_sum = 0
    index = 0
    while quotas_completed < n and len(coffee) > 0:        
        if coffee[index] + current_sum <= split:
            current_sum += coffee[index]
            coffee.pop(index)
            index -= 1
         
        index += 1

        if current_sum == split:
            quotas_completed += 1
            current_sum = 0
            index = 0

    if quotas_completed == n:
        return True

            


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))