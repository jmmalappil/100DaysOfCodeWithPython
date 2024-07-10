# Age as input
age = input("Please provide your age:")

# Max age limit
max_age = 90

# Calculate difference between max and current age
age_diff = 90 - int(age)

# Calculate the number of weeks left till max age
num_weeks = age_diff * 52

# Print the week left in life till max age
print(f"Weeks left in life is {num_weeks}")