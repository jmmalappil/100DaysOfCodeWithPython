# Write your code below this line 👇
def prime_checker(number):
    if number% 2 == 0 or number%3 ==0 or number%5 ==0 or number%7 ==0:
        print(f"Number {number} is not prime")
    else:
        print(f"Number {number} is prime")



# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Please provide the number:"))  # Check this number
prime_checker(number=n)