filename = input("Enter the file name: ")
with open(filename) as file:
    lines = file.readlines()

number_lines = len(lines)
print(f"{number_lines} lines in file '{filename}'")

while True:
    try:
        line_number = int(input("Enter line number: "))
        if line_number == 0:
            break
        elif line_number < 1 or line_number > number_lines:
            print(f"Invalid line number. Must be between 1 and {number_lines}.")
        else:
            print(f"Line {line_number}: {lines[line_number - 1]}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
