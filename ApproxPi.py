#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time

# PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
    realPi = math.pi

    # Ask user for decimal precision (up to 10)
    precision = int(input("Enter desired decimal precision (1 to 10): "))

    start = time.time()

    # Calculate pi using the approximation technique
    approxPi = 4 / 1
    sign = -1
    denom = 3

    # Loop until the level of precision is reached
    while round(approxPi, precision) != round(realPi, precision):
        approxPi = approxPi + (sign * 4 / denom)
        sign = sign * -1
        denom = denom + 2

    end = time.time()
    elapsedTime = end - start

    # Print results
    print(f"\nApproximation of π: {approxPi}")
    print(f"Actual value of π:  {realPi}")
    print(f"Rounded to {precision} decimal places.")
    print(f"Elapsed time: {elapsedTime:.6f} seconds")

    # Extra credit: Print the elapsed time 100 times
    for i in range(100):
        print(f"{elapsedTime:.6f} seconds")

if __name__ == '__main__':
    main()
