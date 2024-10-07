# Open the CSV file
with open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv', 'r') as file:
    highest_level = float('-inf')  # Initialize to negative infinity to find the max
    highest_date_time = None       # To store the date and time of the highest water level

    # Skip the header (assuming the file has a header row)
    next(file)

    # Loop through each line in the file
    for line in file:
        # Strip any leading/trailing spaces or newlines
        line = line.strip()

        # Split the line by commas to extract the fields
        columns = line.split(',')

        # Check if the line has enough columns (e.g., at least 4 columns)
        if len(columns) < 4:
            continue

        # Extract the date, time, and water level (assuming they're in the 1st, 2nd, and 4th columns)
        date = columns[0].strip()
        time = columns[1].strip()
        water_level_str = columns[3].strip()

        # Try converting the water level to a float
        try:
            water_level = float(water_level_str)
        except ValueError:
            # If conversion fails, skip this row
            print(f"Skipping invalid water level: {water_level_str}")
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
