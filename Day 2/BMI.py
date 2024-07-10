# 1st input: enter height in metres
height = input("Please provide the height in metres:")

# 2nd input: enter weight in kilograms
weight = input("Please provide the weight in kilograms:")

BMI = round(float(weight)/(float(height)**2),2)

print("BMI for the provided input is:" + str(BMI))