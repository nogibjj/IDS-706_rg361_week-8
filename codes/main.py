import time
def main():
    start = time.time()
    n = 1000
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    end = time.time()
    print(f"Python execution time: {(end - start)/(10^6)} micro-seconds")
    pass

if __name__ == '__main__':
    main()