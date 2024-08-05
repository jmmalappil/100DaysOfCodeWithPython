NAME_FILE_PATH = "D:/100DaysOfCode/Day 24/Mail Merge/Input/Names/invited_names.txt"
LETTER_FILE_PATH = "D:/100DaysOfCode/Day 24/Mail Merge/Input/Letters/starting_letter.txt"
PLACEHOLDER = "[name]"

with open(NAME_FILE_PATH) as names_file:
    names = names_file.readlines()

with open(LETTER_FILE_PATH) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

