import time
import subprocess

def compare():
    #compare python and Rust execution time
    # start = time.time()
    result = subprocess.run(["python", "main.py"], capture_output=True)
    # end = time.time()
    python_time = result.stdout
    python_time = float(python_time)
    print(f"Python execution time: {python_time:.2f} nano-seconds")

    #subprocess.call(["cd", "codes"])
    
    # start = time.time()
    result = subprocess.run(["cargo", "run", "--quiet"], capture_output=True)
    # end = time.time()
    rust_time = result.stdout
    rust_time = float(rust_time)
    print(f"Rust execution time: {rust_time:.2f} nano-seconds")

   
    
    print(f"Difference: {python_time - rust_time:.2f} nano-seconds")
    print(f"Rust is {python_time/rust_time:.2f} times faster than python")
if __name__ == "__main__":
    compare()