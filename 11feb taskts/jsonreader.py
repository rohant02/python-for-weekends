import json

# Load the JSON file
with open('clues.json') as f:
    data = json.load(f)

# Extract relevant information
artifact_name = data['artifact']['name']
theft_location = data['theft']['location']
theft_date = data['theft']['date']
suspects = data['suspects']

# Analyze the clues
print("The stolen artifact is:", artifact_name)
print("The theft occurred at:", theft_location)
print("Date of theft:", theft_date)

