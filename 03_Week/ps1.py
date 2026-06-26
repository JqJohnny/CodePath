# Problem 1
"""
Understand:
Input: (), {}, []
Output: Boolean
Constraints: No closing tag. Uneven amount of tags
Plan: Using a stack
"""


def is_valid_post_format(posts):
    stack = []
    dictonary = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    for x in posts:
        if x in dictonary.keys():
            stack.append(x)
        elif x in dictonary.values():
            if x != dictonary.get(stack[-1]):
                return False
            stack.pop()

    if len(stack) == 0:
        return True


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}"))
# print(is_valid_post_format("(]"))
# print(is_valid_post_format("({[)}]"))

# Problem 2
"""
Understand: 
Input: Queue
Output: Reversed queue
Constraints: 
Plan: Using a stack
"""


def reverse_comments_queue(comments):
    stack = []

    while len(comments):
        comment = comments.pop()
        stack.append(comment)

    return stack


# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# Problem 3
"""
Understand: 
Input: string (title)
Output: Boolean
Constraints: Ignore spaces, puncutation, and cases
Plan: Using a stack
"""

from collections import deque


def is_symmetrical_title(title):
    formatted_title = title.strip(",.!?")
    formatted_title = formatted_title.replace(" ", "")
    formatted_title = formatted_title.lower()
    dqueue = deque(formatted_title)
    while len(dqueue) > 1:
        if dqueue.popleft() != dqueue.pop():
            return False
    return True


print(is_symmetrical_title("A Santba at NASA...!"))
print(is_symmetrical_title("Social Media"))
