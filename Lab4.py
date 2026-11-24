
from itertools import product

# 1. INFORMATION ABOUT ALL ITEMS

items = [
    {"name": "Rifle", "symbol": "r", "size": 3, "points": 25},
    {"name": "Pistol", "symbol": "p", "size": 2, "points": 15},
    {"name": "Ammo", "symbol": "a", "size": 2, "points": 15},
    {"name": "Medkit", "symbol": "m", "size": 2, "points": 20},
    {"name": "Inhaler", "symbol": "i", "size": 1, "points": 5},
    {"name": "Knife", "symbol": "k", "size": 1, "points": 15},
    {"name": "Axe", "symbol": "x", "size": 3, "points": 20},
    {"name": "Talisman", "symbol": "t", "size": 1, "points": 25},
    {"name": "Flask", "symbol": "f", "size": 1, "points": 15},
    {"name": "Antidote", "symbol": "d", "size": 1, "points": 10},
    {"name": "Supplies", "symbol": "s", "size": 2, "points": 20},
    {"name": "Crossbow", "symbol": "c", "size": 2, "points": 20}
]

 
# 2. VARIANT 9 SETTINGS

rows = 2
cols = 4

capacity = rows * cols

initial_points = 20

required_item = "d"


# 3. CALCULATE TOTAL POINTS

total_points = 0

for item in items:
    total_points += item["points"]

print("Total points of all items:", total_points)

# 4. FUNCTION TO CALCULATE SURVIVAL SCORE

def calculate_score(selected_items):

    taken_points = 0

    for item in selected_items:
        taken_points += item["points"]

    left_points = total_points - taken_points

    final_score = initial_points + taken_points - left_points

    return final_score


# 5. CREATE THE BACKPACK

def create_backpack(selected_items):

    cells = []

    # Add item symbols according to their size
    for item in selected_items:

        for i in range(item["size"]):
            cells.append(item["symbol"])

    # Fill empty cells
    while len(cells) < capacity:
        cells.append("_")

    # Create a two-dimensional backpack
    backpack = []

    for i in range(rows):

        start = i * cols
        end = start + cols

        backpack.append(cells[start:end])

    return backpack

# 6. FIND ALL VALID COMBINATIONS

valid_combinations = []

# Generate all possible combinations
for combination in product([0, 1], repeat=len(items)):

    selected_items = []

    # Select items marked with 1
    for i in range(len(items)):

        if combination[i] == 1:
            selected_items.append(items[i])

    # Calculate occupied cells
    used_cells = 0

    for item in selected_items:
        used_cells += item["size"]

    # Check backpack capacity
    if used_cells > capacity:
        continue

    # Check if the mandatory antidote is present
    has_antidote = False

    for item in selected_items:

        if item["symbol"] == required_item:
            has_antidote = True

    if has_antidote == False:
        continue

    # Calculate final survival score
    score = calculate_score(selected_items)

    # Check if survival score is positive
    if score > 0:

        valid_combinations.append(
            (selected_items, used_cells, score)
        )

# 7. DISPLAY THE RESULTS

print("       VARIANT 9 RESULTS")

print("Backpack size:", rows, "x", cols)
print("Backpack capacity:", capacity)
print("Illness: paranoia")
print("Mandatory item: Antidote")
print("Initial survival points:", initial_points)

print("\nNumber of valid combinations:",
      len(valid_combinations))


# Print every valid combination
for number, combination in enumerate(valid_combinations, start=1):

    selected_items = combination[0]
    used_cells = combination[1]
    score = combination[2]

    print("Combination:", number)

    # Create backpack
    backpack = create_backpack(selected_items)

    # Print backpack
    for row in backpack:
        print(row)

    # Print selected items
    print("Items:")

    for item in selected_items:
        print(item["name"], "-", item["symbol"])

    # Print additional information
    print("Used cells:", used_cells, "/", capacity)
    print("Final survival score:", score)

