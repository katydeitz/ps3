import csv
import re
import string

# Open the CSV file
with open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    highest_level = float('-inf')  # Initialize to negative infinity to find the max
    highest_date_time = None       # To store the date and time of the highest water level

    # Skip the header
    next(reader)

    # Loop through each row in the file
    for row in reader:
        # Check if there are enough columns
        if len(row) < 4:
            continue

        # Extract the date, time, and water level (assuming they're in the 1st, 2nd, and 4th columns)
        date = row[0].strip()
        time = row[1].strip()
        water_level_str = row[3].strip()

        # Print the raw water level value and its character codes to debug non-numerical characters
        #print(f"Raw water level value: '{water_level_str}'")
        #print(f"Character codes: {[ord(char) for char in water_level_str]}")

        # Remove all non-printable characters
        water_level_str = ''.join(filter(lambda x: x in string.printable, water_level_str))

        # Remove non-numeric characters
        water_level_str = re.sub(r'[^\d.-]', '', water_level_str)

        # Replace non-breaking spaces with regular spaces and strip
        water_level_str = water_level_str.replace('\xa0', ' ').strip()

        # Remove any remaining Unicode spaces
        water_level_str = ''.join(water_level_str.split())

        # Print the cleaned water level value for debugging
        #print(f"Cleaned water level value: '{water_level_str}'")

        # Skip if the water level is empty
        if not water_level_str:
            print("Skipping empty water level")
            continue

        # Try converting the cleaned water level to a float
        try:
            water_level = float(water_level_str)
        except ValueError:
            print(f"Skipping invalid water level after cleaning: '{water_level_str}'")
            continue

        # Check if this is the highest water level observed so far
        if water_level > highest_level:
            highest_level = water_level
            highest_date_time = f"{date} {time}"

# Print the result
if highest_date_time:
    print(f"The highest water level was {highest_level} ft, observed on {highest_date_time}.")
else:
    print("No valid water levels found in the file.")
