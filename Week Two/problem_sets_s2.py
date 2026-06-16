# Problem Set
"""
Understand: We are looking for the most endangered
Input: List of dictonaries
Output: String based off population
Constraints: Empty list, singular dictonary
"""


def most_endangered(species_list):
    most_endanger = species_list[0]
    for x in species_list:
        if x["population"] < most_endanger["population"]:
            most_endanger = x
    # for x in range(len(species_list)):
    #     if species_list[x]["population"] < most_endanger["population"]:
    #         most_endanger = species_list[x]

    return most_endanger


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]

# print(most_endangered(species_list)["name"])

# Problem 2
"""
Understand: 
Input: endangered species and observed
Output: Number of endangered species
Constraints: case-sensitive
"""


def count_endangered_species(endangered_species, observed_species):
    # set_of_observed = set(observed_species)
    set_of_endangered = set(endangered_species)
    count = 0
    for x in observed_species:
        if x in set_of_endangered:
            count += 1

    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1))
# print(count_endangered_species(endangered_species2, observed_species2))


# Problem 4


def prioritize_observations(observed_species, priority_species):
    animals = {}
    result = []

    for animal in observed_species:
        animals[animal] = animals.get(animal, 0) + 1

    for animal in priority_species:
        if animal in animals:
            for i in range(animals.get(animal)):
                result.append(animal)
            animals.pop(animal)

    for animal in animals:
        for i in range(animals.get(animal)):
            result.append(animal)

    return result


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))

