import csv
import re
import string

# Initialize variables for calculations
highest_level = float('-inf')  # Initialize to negative infinity to find the max
lowest_level = float('inf')    # Initialize to positive infinity to find the min
total_levels = 0               # Sum of all valid water levels
valid_level_count = 0          # Number of valid water level entries

# Open the CSV file
with open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    highest_date_time = None   # To store the date and time of the highest water level
    lowest_date_time = None    # To store the date and time of the lowest water level

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

        # Print the raw water level value and its character codes for debugging
        print(f"Raw water level value: '{water_level_str}'")
        print(f"Character codes: {[ord(char) for char in water_level_str]}")

        # Remove all non-printable characters
        water_level_str = ''.join(filter(lambda x: x in string.printable, water_level_str))

        # Remove non-numeric characters (if any)
        water_level_str = re.sub(r'[^\d.-]', '', water_level_str)

        # Replace non-breaking spaces with regular spaces and strip
        water_level_str = water_level_str.replace('\xa0', ' ').strip()

        # Remove any remaining Unicode spaces
        water_level_str = ''.join(water_level_str.split())

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

        # Update the highest and lowest water levels observed so far
        if water_level > highest_level:
            highest_level = water_level
            highest_date_time = f"{date} {time}"

        if water_level < lowest_level:
            lowest_level = water_level
            lowest_date_time = f"{date} {time}"

        # Add to the total water level and increase the count
        total_levels += water_level
        valid_level_count += 1

# Calculate the average water level
if valid_level_count > 0:
    average_level = total_levels / valid_level_count
else:
    average_level = None

# Print the results
if highest_date_time and lowest_date_time:
    print(f"The highest water level was {highest_level} ft, observed on {highest_date_time}.")
    print(f"The lowest water level was {lowest_level} ft, observed on {lowest_date_time}.")
    print(f"The average water level during the period was {average_level:.2f} ft.")
else:
    print("No valid water levels found in the file.")
