"""
Problem 1
You are in charge of overseeing the blueprint approval process for various architectural designs.
Each blueprint has a specific complexity level, represented by an integer.
Due to the complex nature of the designs, the approval process follows a strict order:

Blueprints with lower complexity should be reviewed first.
If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
Your task is to simulate the blueprint approval process using a queue. 
You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. 
Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

Return the order in which the blueprints are approved.
Example Output:

[1, 2, 3, 4, 5]
[2, 4, 5, 6, 7]

Understand: We are to use a queue
Input: List of integers
Output: List of integers (sorted in ascending order)

Match: Queue
Plan: 
Initalize an empty list
Queue
Iterate through the input,
Add to queue
Less goes to the front,
[1,2,3]
"""
import heapq

def blueprint_approval(blueprints):
    heapq.heapify(blueprints)
    result = []
    while blueprints:
        result.append(heapq.heappop(blueprints))

    return result
# print(blueprint_approval([3, 5, 2, 1, 4])) 
# print(blueprint_approval([7, 4, 6, 2, 5]))

"""
Problem 2
You are given an array floors representing the heights of different building floors.
Your task is to design a skyscraper using these floors, where each floor must be placed on top of a floor with equal or greater height. 
However, you can only start a new skyscraper when necessary, meaning when no more floors can be added to the current skyscraper according to the rules.

Return the number of skyscrapers you can build using the given floors.

Example Output:

Input: List of heights
Output: Integer number of skyscrapers
Match: Stack

4
4
2
"""

def build_skyscrapers(floors):
    res = 0
    stack = []
    for floor in floors:
        if not stack or stack[-1] <= floor:
            res += 1
        stack.append(floor)
    
    return res

# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

"""
Problem 3
You are an architect designing a corridor for a futuristic dream space. 
The corridor is represented by a list of integer values where each value represents the width of a segment of the corridor. 
Your goal is to find two segments such that the corridor formed between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.

Example Output:

Match: two pointer approach

Plan:
Decrease right or increase left as we go until they meet in the middle
When right < left, exit loop
For each iteration, calculate the area

49
1
"""

# Time: O(n)
# Space: O(1)

def max_corridor_area(segments):
    # Left pointer, right pointer
    left = 0
    right = len(segments) - 1
    # Keep track of max area as we go
    maxArea = 0

    # When right < left, exit loop
    while left < right:
        # Height is smallest value
        height = min(segments[right], segments[left])
        # Calculate max and see if we need to rewrite the current max
        # For each iteration, calculate the area
        maxArea = max(maxArea, (right - left) * height)

        # Decrease right or increase left as we go until they meet in the middle. Decrease or increase the smaller integer
        if segments[right] < segments[left]:
            right -= 1
        else:
            left += 1

    return maxArea

# print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
# print(max_corridor_area([1, 1]))

"""
Problem 4
You are an architect tasked with designing a dream building layout. The building layout is represented by a string s of even length n. 
The string consists of exactly n / 2 left walls '[' and n / 2 right walls ']'.

A layout is considered balanced if and only if:

It is an empty space, or
It can be divided into two separate balanced layouts, or
It can be surrounded by left and right walls that balance each other out.
You may swap the positions of any two walls any number of times.

Return the minimum number of swaps needed to make the building layout balanced.

Example Output:
1
2
0

Input: Strings
Output: Integers (indicating min number of swaps)

Plan: Count the number of imbalances
and the min number of swaps is imbalance-1 (min of 1 if there is an in balance)

Stack
sum = 0

"""
# Greedy approach?
def min_swaps(s):
    if not s:
        return 0

    stack = []
    total = 0
    current = 0
    for char in s:
        # print(total, current)
        if not stack:
            stack.append(char)
            total += 1
            continue

        if char == ']' and stack[-1] == "[":
            total -= 1
            stack.pop()
        else:
            stack.append(char)
            total += 1

        current = max(current, total)

    current = (current//2)
    if current // 2 > 1:
        current -= 1

    return current


print(min_swaps("][]["))
print(min_swaps("]]][[[")) # [[][]]]
print(min_swaps("[]"))
print(min_swaps("[]][]["))

