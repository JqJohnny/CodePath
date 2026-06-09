# Problem 1
"""
Understand
Input: Two lists, length n

Output: Dictonary

Constraints: i <= 0 < n and len(artists) == len(set_times).
"""

def lineup(artists, set_times):
    result = {}
    for i in range(len(artists)):
        result[artists[i]] = set_times[i]

    return result


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

print(lineup(artists1, set_times1))

# Problem 2
"""
Understand - Search the artist, find day, time, and stage.
Input: Artist name, Festival schedule (dictonary)

Output: Dictonary

Constraints: If it does not exist return a specific message
"""

def get_artist_info(artist, festival_schedule):
    # schedule = festival_schedule.get(artist)
    # if schedule:
    #     return schedule
    # return {"message": "Artist not found"}
    return festival_schedule.get(artist, {"message": "Artist not found"})

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))

# Problem 3
"""
Understand - Loop through it and add the total number
Input: Dictonary

Output: Integer

Constraints: Dictonary is empty
"""

def total_sales(ticket_sales):
    total = 0
    for x in ticket_sales.values():
        total += x
    
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales)) 