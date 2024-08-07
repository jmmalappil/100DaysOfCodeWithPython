# numbers = [2,3,5,7]
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# num_list = [n*2 for n in range(1,5)]
# print(num_list)

# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# names_cap = [name.upper() for name in names if len(name) > 5]
# print(names_cap)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(text) for text in list_of_strings]
# result = [number for number in numbers if number%2 == 0]
# print(result)

# with open("file1.txt") as f1:
#     numbers_file1 = f1.read().splitlines()
#
# with open("file2.txt") as f2:
#     numbers_file2 = f2.read().splitlines()
#
# numbers_file1 = [int(num) for num in numbers_file1]
# numbers_file2 = [int(num) for num in numbers_file2]
#
# result = [num for num in numbers_file1 if num in numbers_file2]
# print(result)

# import random
# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
#
# passed_students = {student:score for (student,score) in students_scores.items() if int(score) > 50 }
# print(students_scores)
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# print(words)
# result = {word:len(word) for word in words}
# print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp*9/5) + 32 for (day,temp) in weather_c.items()}

print(weather_f)


