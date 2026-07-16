"""
Problem 1
Understand:
Input: a list of sorted integers, an integer value to be searched for
Output: True, if integer exists in list, else false
Constraints: 

Plan: 
1. if array empty return false
2. Use binary search
3. Define high variable, a low variable, calculate middle
4. if the middle is equal to key return true
5. if middle is higher than key, set low to euqal middle + 1
6. if middle is lower, high to equal middle - 1
7. iterate through the conditions until we reach low = high
8. return false
"""

def find_cruise_length(cruise_lengths, vacation_length):
    high = len(cruise_lengths) -1
    low = 0
    # High, low, mid are indicies
    while high != low:
        mid = (high + low) // 2

        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] > vacation_length:
            high = mid - 1
        else:
            low = mid + 1

    # check when equal just int case
    cruise_lengths[high]
            

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))