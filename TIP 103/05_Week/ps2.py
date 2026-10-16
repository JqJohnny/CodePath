"""
Problem 1
Understand: A given source is a tuple (destination, cost)
Input: We are given 3 inputs
A flight adjacency dictonary
A starting point - String
A endpoint - String
Output:
Integer (-1 if there is no route otherwise cost)
M:
DFS
P:
Seen set
DFS - Recursion
Helper function

I:
R:
E:
"""


def calculate_cost(flights, start, dest):
    seen = {start}
    result = 0
    if flights is None or len(flights) == 0:
        return -1

    def helper(curr, cost):
        nonlocal result
        if curr == dest:
            result = cost
        possible_flights = flights[curr]
        # If there are multiple possible destinations
        for flight in possible_flights:
            if flight[0] not in seen:
                seen.add(flight[0])
                helper(flight[0], cost + flight[1])

    helper(start, 0)

    if dest not in seen:
        return -1
    return result


flights = {
    "LAX": [("SFO", 50)],
    "SFO": [("LAX", 50), ("ORD", 100), ("ERW", 210)],
    "ERW": [("SFO", 210), ("ORD", 300)],
    "ORD": [("ERW", 300), ("SFO", 100), ("MIA", 400)],
    "MIA": [("ORD", 400)],
}

# print(calculate_cost(flights, "LAX", "MIA"))

flights2 = {}

# print(calculate_cost(flights2, "", ""))
flights3 = {
    "LAX": [("SFO", 50)],
    "SFO": [("LAX", 50), ("ORD", 100), ("ERW", 210)],
    "ERW": [("SFO", 210), ("ORD", 300)],
    "ORD": [("ERW", 300), ("SFO", 100)],
    "MIA": [("ORD", 400)],
}

# print(calculate_cost(flights3, "ERW", "MIA"))


"""
Problem 2
CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to 
reach all other airports. They track their current flight offerings in an adjacency dictionary flights where each key is 
an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in 
flights[i]. Assume that if there is flight from airport i to airport j, the reverse is also true.

Given flights, return the minimum number of flights (edges) that need to be added such that there is flight path from 
each airport in flights to every other airport.

"""

def min_flights_to_expand(flights):

    seen = set() # jfk, lax, sfo
    edges = -1
    def DFS(flight):
        destinations = flights[flight] # ['LAX', 'SFO']
        for dest in destinations:
            if dest not in seen:
                seen.add(dest)
                DFS(dest)

    for flight in flights:
        if flight not in seen:
            edges += 1
        DFS(flight)

    return edges
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX', 'ATL'],
    'ORD': ['ATL', 'JFK'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))

# Thank you! Good sesh :)
# yep :)