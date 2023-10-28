import json


# List of names
names = [
    "Ava", "Bella", "Cara", "Diana", "Eva", "Una", "Ivy", "Nora",
    "Fiona", "Grace", "Hazel", "Iris", "Jade", "Kara", "Lila",
    "Mira", "Nina", "Olive", "Piper", "Quinn", "Rosa", "Skye",
    "Tara", "Vera", "Willa", "Zara"
]

# Dictionary to hold the names and their unique IDs
names_to_ids = {}

# Generate a uniqe ID for each name and add it to the dictionary
for i, name in enumerate(names, start=1):
    unique_id = f"{name[:3].upper()}{i:03}"
    names_to_ids[unique_id] = name

# Convert the dictionary to a JSON string
json_data = json.dumps(names_to_ids, indent=4)

# Write the JSON string to a file
with open("Responses/Waking Name/NameID.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("Done!")

