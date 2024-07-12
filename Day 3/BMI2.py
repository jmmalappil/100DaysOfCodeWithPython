# 1st input: enter height in metres
height = input("Please provide the height in metres:")

# 2nd input: enter weight in kilograms
weight = input("Please provide the weight in kilograms:")

BMI = round(float(weight)/(float(height)**2),2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI} and you have a normal weight")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI} and you are slightly overweight")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI} and you are obese")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")