"""
Understand:
Match: Stack object
Plan: Stack, stack of canceled
Input: List
Output: List of IDs that remain
Constraints: Empty list,
"""


def manage_stage_changes(changes):
    # if len(changes) == 0:
    #     return []
    canceled = []
    result = []
    for change in changes:
        command = change.split()
        if len(command) == 2:  # Schedule X
            result.append(command[1])
        else:
            if command[0] == "Cancel":  # Cancel
                canceled.append(result.pop())
            else:  # Reschedule
                result.append(canceled.pop())

    return result


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]))
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))
# print(manage_stage_changes([]))


# Problem 2
"""
Understand: Priorities, Queue, Is priority unique? No. Numbers dont have to be consecutive
Match: deque, dictionary (priority: queue)
Plan: 
    loop through each tuple
    if priority is not in dictionary
        add priority and create a queue with the element
    else
        add the element to the end of the queue with the priority key value in the dictionary

    Ex. [(2, "A"), (2, "B")]
    problem: sort the keys takes O(log n )
Input: Requests (List of tuples)
Output: Order of which perfomrances are processed, list
Constraints: Empty list, 
"""
from collections import deque


# input is a list of tuples
def process_performance_requests(input):
    priorities = {}
    for request in input:
        # this line doesn't work then
        priority = request[0]
        name = request[1]
        if priority in priorities:
            priorities[priority] = name
        else:
            priorities[priority] = deque([name])

    list = sorted(priorities.items(), reverse=True)
    output = []
    for _, queue in list:
        for item in queue:
            output.append(item)

    return output
    # queues =  [x[1] for x in list]
    # return [str(x) for x in queues]


# [5, deque(['Music']), 3, deque(['Dance']), 1, deque(['Drama'])]
# [4, deque(['Concert']), 3, deque(['Stand-up Comedy']), 2, deque(['Poetry']), 1, deque(['Magic Show'])]
# [5, deque(['Keynote Speech']), 4, deque(['Panel Discussion']), 3, deque(['Film Screening']), 2, deque(['Workshop']), 1, deque(['Art Exhibition'])]
# PS C:\Projects\CodePath>

"""
still a dequeue
but we need to get every element in the queue not just the first
ye either new line and loop through again for each
why does it return deque in the string, i think we are still nested by 1
['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
"""


print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
print(
    process_performance_requests([
        (2, "Poetry"),
        (1, "Magic Show"),
        (4, "Concert"),
        (3, "Stand-up Comedy"),
    ])
)
print(
    process_performance_requests([
        (1, "Art Exhibition"),
        (3, "Film Screening"),
        (2, "Workshop"),
        (5, "Keynote Speech"),
        (4, "Panel Discussion"),
    ])
)
