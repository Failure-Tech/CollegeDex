import json
import random

def calculate_attack(rank):
    return 1420 * (71 ** (-rank / 250)) + 80

def calculate_health(rank):
    return 2450 * (49 ** (-rank / 250)) + 550

def add_random_values(collegedata):
    for entry in collegedata:
        try:
            # Ensure rank can be converted to a float
            rank = float(entry[1])
            print(rank)
            # Calculate and append attack and health values
            attack_value = calculate_attack(rank) #+ random.uniform(-75, 75)
            health_value = calculate_health(rank) #+ random.uniform(-200, 200)

            entry.append({
                "attack": attack_value,
                "health": health_value
            })
        except ValueError:
            print(f"Invalid rank value: {entry[1]}")
            continue  # Skip this entry if rank is invalid
    return collegedata

# Read original data
with open("collegeinfo.txt", 'r') as file:
    json_string = file.read()
    collegedata = json.loads(json_string)

# Add calculated attack and health values
collegedata_updated = add_random_values(collegedata)

# Save the updated data back to a file
with open("collegeinfo_updated.txt", 'w') as file:
    json.dump(collegedata_updated, file, indent=4)