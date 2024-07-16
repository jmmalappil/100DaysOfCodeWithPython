# Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    num_can = math.ceil((height*width)/coverage)
    print(f"You will need {num_can} cans of paint")




# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Please provide height of wall:")) # Height of wall (m)
test_w = int(input("Please provide width of wall:")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)