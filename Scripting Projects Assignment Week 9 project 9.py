def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def compute_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

filename = 'numbers.txt'
lines = read_file(filename)
numbers = list(map(float, lines))
average = compute_average(numbers)

print(f"The average of the numbers in '{filename}' is: {average}")
