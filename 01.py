# Initialize a variable to store the sum of calibration values
total_sum = 0

# Open and read the input.txt file
with open('input.txt', 'r') as file:
    for line in file:
        # Remove leading and trailing whitespace from each line
        line = line.strip()
        
        # Check if the line is not empty
        if line:
            # Extract the first and last digits and convert them to integers
            first_digit = int(line[0])
            last_digit = int(line[-1])
            
            # Combine the digits to form a two-digit number
            calibration_value = first_digit * 10 + last_digit
            
            # Add the calibration value to the total sum
            total_sum += calibration_value

# Print the sum of all calibration values
print("The sum of all calibration values is:", total_sum)
