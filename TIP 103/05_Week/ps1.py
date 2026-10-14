# PS 1, Version 1
"""As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list 
flights with n nodes where each node represents the ID of a different destination and 
flights[i] is an integer array indicating that there is a flight from destination i to 
each destination in flights[i]. Write a function bidirectional_flights() that returns True if 
for every flight from a destination i to a destination j there also exists a flight from 
destination j to destination i. Return False otherwise.

U: 
directional graph. 
input: 

integer array representing adjecent flights to flight i

output: boolean (true if bidirectional)

flights is empty, return True
flights is length 1. T/F? Depends if it points to itself: T, else: F


for each entry at index i, values for each entry in the list should also contain that index

M: 
traverse values for each entry at each index

P: 

initialize a var i representing the index
while loop i < len of flights
get entry of flights at i
initialize a boolean which represents if it contains i
for each entry:
    flights[entry] must have i: []

R: time complexity: O(V*E) * O(V), space complexity: O(1)

"""

def bidirectional_flights(flights):
    for i, entry in enumerate(flights):
        for val in entry:
            if i not in flights[val]:
                return False
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]] # [2]
flights3 = [[1, 2, 3], [0], [0], [2, 1]] 

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
print(bidirectional_flights(flights3))

"""
You are a pilot navigating a new airport and have a map of the airport represented as an 
undirected star graph with n nodes where each node represents a terminal in the airport 
labeled from 1 to n. You want to find the center terminal in the airport where the pilots' 
lounge is located.

Given a 2D integer array terminals where each terminals[i] = [u, v] indicates that there 
is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges connecting 
the center node ot every other node.

U: We want to find the center node of a star graph
Terminal[i] = A connection of an edge connecting two nodes

Input: Undirected Star graph
Output: Integer representing a node
M:
Frequency map
P:
We use a frequency map to keep a count of each number
I: 
R: time: O(E), space: O(V)
"""

def find_center(terminals):
    freq = {}
    for edge in terminals: # conection between terminals
        for terminal in edge: # node/vertix
            freq[terminal] = freq.get(terminal, 0) + 1
    return max(freq, key=freq.get)

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

"""
Problem 3
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations 
they can reach from a starting airport. The flight connections between airports are represented as an adjacency 
dictionary flights, where each key is a destination, and the corresponding value is a list of other destinations 
that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start location either through 
a direct flight or connecting flights with layovers. The list should be provided in ascending order by number of 
layovers required.

U: directed, unweighted graph 
Input: adjacency dictionary representing flights. k: dest, v: list of dest that are connected, start: string
Output: list in ascending order by layovers required representing destinations that are reachable through start
assume: start is present in flights. case-insensitive

M:
a stack represent nodes seen
BFS

P:


keep 
I
R

"""
def get_all_destinations(flights, start):
    stack = [start]
    seen = {start}
    result = [start]
    while stack:
        stack2 = []
        while stack:
            routes = flights[stack.pop()]
            for route in routes:
                if route not in seen:
                    stack2.append(route)
                    seen.add(route)
                    result.append(route)

        stack = stack2
    return result
    

# Beijing -> ["Mexico City", "Helsinki"] # Layovers 1 (stack 1)
# Helsinki -> ["Cairo", "New York"] (stack 2)
# Mexico City -> ["Sydney"] (stack 2)

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))