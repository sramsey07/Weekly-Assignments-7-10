import math

tolerance = 0.000001

def newton(n, estimate):
    
    estimate = (estimate + n / estimate) / 2
    difference = abs(n - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(n, estimate)

def main():
    while True:
        number = input("Enter a positive number or press enter to quit: ")
        if number == "":
            break
        number = float(number)
        estimate = float(input("Enter estimate of the square root: "))

        print("The program's estimate is ", newton(number, estimate))
        print("Python's estimate is ", math.sqrt(number))

if __name__ == "__main__":
    main()
