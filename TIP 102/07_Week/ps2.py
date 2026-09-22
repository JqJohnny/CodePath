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
    high = len(cruise_lengths) - 1
    low = 0
    # High, low, mid are indicies
    while high >= low:
        mid = (high + low) // 2

        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] > vacation_length:
            high = mid - 1
        else:
            low = mid + 1

    # check when equal just int case
    return False


# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

"""
Problem 2
Understand: Recursive, 
Input: List of ascending order by deck leve;, integer preferred_deck
Output: Integer, returns the index of preferred_deck, if does not exist return where it would be
Constraints: O(log n) time complexity

Plan:
1. Define a helper function that starts in the middle with step
2. Base case if step is 1 and already checked one/two over, means does not exist, and needs to be inserted
otherwise return index
3. If higher than index then we need to subtract step
4. If lower than index then we need to add step
5. Cut step in half and repeat, until base case.

"""


def find_cabin_index(cabins, preferred_deck):
    high = len(cabins) - 1
    low = 0

    def helper(high, low):
        # Base Case
        # return if < 0 > len
        if low == high and cabins[low] != preferred_deck:
            if preferred_deck > cabins[low]:
                return low + 1
            else:
                return low - 1

        mid = (high + low) // 2
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] > preferred_deck:
            high = mid - 1
        else:
            low = mid + 1
        return helper(high, low)

    return helper(high, low)


print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))



def search_range(nums, target):
    # Find leftmost occurrence
    left, right = 0, len(nums) - 1
    leftMost = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            leftMost = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


    # Find rightmost occurrence
    left, right = 0, len(nums) - 1
    rightMost = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            rightMost = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [leftMost, rightMost]

print(search_range([0,1,3,4,8,8,8,8], 8))