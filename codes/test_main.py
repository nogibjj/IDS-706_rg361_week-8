"""
Compare Execution time of python and rust and log them
"""

import subprocess
from datetime import datetime
import os

def compare():
    """
    Compare Execution time of python and rust and log them
    """
    #set the working directory to codes
    os.chdir("/workspaces/IDS-706_rg361_week-8/codes")
    
    #set the log file
    log_file = "../summary.md"
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M") + " (UTC)"

    #create list to track times
    python_times = []
    rust_times = []

    #run each file 5 times to calculate average
    for i in range(5):
        result_python = subprocess.run(["python", "main.py"], capture_output=True)
        python_times.append(float(result_python.stdout))

        result_rust = subprocess.run(["cargo", "run", "--quiet"], capture_output=True)
        rust_times.append(float(result_rust.stdout))
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("# Summary file Generated at " + dt_string + "\n"+ "\n")

        #python time
        f.write("## Python Execution Times:\n")
        #Print python times
        for i in range(len(python_times)):
            f.write(f"Python Run {i+1} took: {python_times[i]:.2f} nano-seconds\n")
        #Print average  
        f.write(f"Average Python Execution Time: {sum(python_times)/len(python_times):.2f} nano-seconds\n"+ "\n")

        #rust time
        f.write("## Rust Execution Times:\n")
        #Print rust times
        for i in range(len(rust_times)):
            f.write(f"Rust Run {i+1} took: {rust_times[i]:.2f} nano-seconds\n")
        #Print average
        f.write(f"Average Rust Execution Time: {sum(rust_times)/len(rust_times):.2f} nano-seconds\n"+ "\n")

        #Compare
        f.write("## Comparison:\n")
        f.write(f"Average difference in execution times: {sum(python_times)/len(python_times) - sum(rust_times)/len(rust_times):.2f} nano-seconds\n")
        f.write(f"On an average Rust is {sum(python_times)/sum(rust_times):.2f} times faster than python\n")


if __name__ == "__main__":
    compare()