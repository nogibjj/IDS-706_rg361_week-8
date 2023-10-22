"""
Measure the time Taken to calculate factorial of 31
"""
import time


def main():
    start = time.time()
    n = 31
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    end = time.time()
    print((end - start) / 10**-9, end="")
    return 0


if __name__ == "__main__":
    main()
