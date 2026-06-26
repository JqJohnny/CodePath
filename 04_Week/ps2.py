"""
Understand: Exact match on the sum of the two times
Input: List of integers - required time, List - time slots
Output: Boolean
Constraints: If the list wasnt sorted, empty list
"""


def find_task_pair(task_times, available_time):
    start = 0
    end = len(task_times) - 1

    while start < end:
        if task_times[start] + task_times[end] < available_time:
            start += 1
        elif task_times[start] + task_times[end] > available_time:
            end -= 1
        else:
            return True

    return False


task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

"""
Understand: Looking to minimize gaps in time end and start of times
Remember the ending time of the previous entry, and compare to the 
starting time of the current entry.
Input: List of tuples (Start, end)
Output: Integer
Constraints: If we are given one tuple, careful of converting time of 60
"""


def find_smallest_gap(work_sessions):
    min = float("inf")

    for index in range(len(work_sessions) - 1):
        if (
            (
                (work_sessions[index + 1][0] // 100) * 60
                + (work_sessions[index + 1][0] % 100)
            )
            - ((work_sessions[index][1] // 100) * 60 + (work_sessions[index][1] % 100))
        ) < min:
            min = (
                (work_sessions[index + 1][0] // 100) * 60
                + (work_sessions[index + 1][0] % 100)
            ) - (
                (work_sessions[index][1] // 100) * 60 + (work_sessions[index][1] % 100)
            )

    return min


work_sessions = [(900, 1100), (1300, 1500), (1900, 2100)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
