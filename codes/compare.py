import time
import subprocess

def compare():
    #compare python and Rust execution time
    start = time.time()
    subprocess.call(["python", "codes/main.py"])
    end = time.time()
    python_time = end - start
    print(f"Python execution time: {python_time:.3E} seconds")

if __name__ == "__main__":
    compare()