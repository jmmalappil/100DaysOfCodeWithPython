print("Welcome to the tip calculator!")

# Take total bill as input from user
total_bill = float(input("What was the total bill?"))

# Take the tip to be provided as input from user
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))

# Take input from user on how many members are splitting the bill
people = int(input("How many people to split the bill?"))

# Calculate the total bill along with tip
bill_with_tip = total_bill + (tip/100) * total_bill

# Calculate the bill for each member
shared_bill = round((bill_with_tip / people),2)

# Print the shared bill for each member
print(f"Each person should pay: ${shared_bill}")
