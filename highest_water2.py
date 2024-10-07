# Open the CSV file
with open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv', 'r') as file:
    highest_level = float('-inf')  # Initialize to negative infinity to find the max
    highest_date_time = None       # To store the date and time of the highest water level

    # Skip the header (assuming the file has a header row)
    next(file)

    # Loop through each line in the file
    for line in file:
        #Strip any leading/trailing spaces or newlines
        line = line.strip()
        
        # Split the line by commas to extract the fields
        columns = line.split(',')

        # Extract the date, time, and water level (assuming they're in the 1st, 2nd, and 4th columns)
        date = columns[0]
        time = columns[1]
        try:
            water_level = float(columns[3])  # Convert the water level to a float
        except ValueError:
            continue  # Skip this line if water level cannot be converted to float

        # Check if this is the highest water level observed so far
        if water_level > highest_level:
            highest_level = water_level
            highest_date_time = f"{date} {time}"

# Print the result
if highest_date_time:
    print(f"The highest water level was {highest_level} ft, observed on {highest_date_time}.")
else:
    print("No valid water levels found in the file.")
