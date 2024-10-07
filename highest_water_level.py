# Open the file and initialize variables
highest_water_level = None
highest_water_level_date_time = ""
file_path = '/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv'

# Open the CSV file for reading
with open(file_path, 'r') as file:
    # Skip the header row (assuming the first row is a header)
    next(file)

    # Loop through each line in the file
    for line in file:
        # Split the line by commas (CSV)
        columns = line.strip().split(',')

        # Extract the date, time, and water level (assuming water level is in the 4th column)
        date = columns[0]
        time = columns[1]
        try:
            water_level = float(columns[4])  # Convert water level to a float
        except ValueError:
            continue  # Skip lines with invalid water level values

        # Check if this is the highest water level encountered
        if highest_water_level is None or water_level > highest_water_level:
            highest_water_level = water_level
            highest_water_level_date_time = f"{date} {time}"

# Report the highest water level and the date/time it was observed
if highest_water_level is not None:
    print(f"Highest Water Level: {highest_water_level} meters")
    print(f"Observed on: {highest_water_level_date_time}")
else:
    print("No valid water level data found.")
