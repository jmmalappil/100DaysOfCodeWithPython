# which number do you want to check?
number = int(input("Please provide the number to check even or odd:"))

# Use modulo to check the remainder on division of the number by 2
if number % 2 == 0:
    print(f"The provided number {number} is even")
else:
    print(f"The provided number {number} is odd")