import math

tolerance = 0.000001

def newton(n, estimate=None, initial_estimate=1.0):
    if estimate is None:
        estimate = initial_estimate


    estimate = (estimate + n / estimate) / 2
    difference = abs(n - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(n, estimate, initial_estimate)

result = newton(10)
print(result)
