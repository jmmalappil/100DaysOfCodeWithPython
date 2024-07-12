print("Thank you for choosing Python Pizza Deliveries!")
total_bill = 0

# What size pizza do you want? S, M or L
size = input("What size pizza do you want? S, M or L")

#Do you want pepperoni? Y or N
add_pepperoni = input("Do you want pepperoni? Y or N")

#Do you want extra cheese? Y or N
extra_cheese = input("Do you want extra cheese? Y or N")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

if size == 'S':
    if add_pepperoni == 'Y':
        total_bill = small_pizza_price + 2
elif size == 'M':
    if add_pepperoni == 'Y':
        total_bill = medium_pizza_price + 3
elif size == 'L':
    if add_pepperoni == 'Y':
        total_bill = large_pizza_price + 3
else:
    print("You have provided a wrong choice of pizza.")

if extra_cheese == 'Y':
    total_bill+=1

print(f"Your final bill is ${total_bill}")
