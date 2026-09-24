# problem 1
"""
As the curator of an art gallery, you are organizing
a new exhibition.
You must ensure the collection of art pieces are balanced to attract the right range of buyers.

A balanced collection is one where the difference
between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece,
write a function find_balanced_subsequence() that returns the length of the longest
balanced subsequence.

A subsequence is a sequence derived from the array by deleting
some or no elements without changing the order of the remaining elements.

Example Output:

5
Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

2
0
"""


def find_balanced_subsequence(art_pieces):

    # make a frequency map
    # check for the longest sum of one number's count with the following number's count
    maxLen = 0
    freq = {}
    for n in art_pieces:
        freq[n] = freq.get(n, 0) + 1

    print(freq.items())
    for n in freq.keys():
        total = freq.get(n + 1, 0)
        if total == 0:
            continue
        maxLen = max(maxLen, (freq[n] + total))

    return maxLen


art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
#                 l      r
# maxCount = 1,
art_pieces2 = [1, 2, 3, 4]
art_pieces3 = [1, 1, 1, 1]
art_pieces4 = [1, 1, 3, 3]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
print(find_balanced_subsequence(art_pieces4))


def find_balanced(art_pieces):
    l = 0
    maxCount = 0
    r = 0
    wordSet = set()
    for r in range(1, len(art_pieces)):
        while art_pieces[l] > art_pieces[r]:
            if art_pieces[l] - art_pieces[r] != 1:
                l += 1
            else:
                art_pieces.remove(s[l])
                maxCount += 1

    return maxCount


print(find_balanced(art_pieces1))
print(find_balanced(art_pieces2))
print(find_balanced(art_pieces3))
print(find_balanced(art_pieces4))


"""
Problem 2
Your art gallery has just been shipped a new collection of numbered art pieces, and 
you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].
The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, 
and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces 
and returns True if the given array is an authentic array, and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.
"an array of length n + 1"
integer n twice
Input: List
Output: Boolean


Frequency map

"""


# O(2n) = O(n)
def is_authentic_collection(art_pieces):
    seen = set(range(1, len(art_pieces)))
    duplicate = False
    for art in art_pieces:
        if art in seen:
            seen.remove(art)
        elif art == len(art_pieces) - 1 and duplicate == False:
            duplicate = True
        else:
            return False

    if duplicate and len(seen) == 0:
        return True


collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]  #
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
