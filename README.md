## SAT-problem-solver
This project includes CNF parsing and brute-force assignment checking

# How to Run Program

Requirements:
- Ensure Python 3.x is installed. You can check the version by running:
  python3 --version

# Making the Code Executable:
- If the sat file is not already executable, you can make it executable using: <br>
    - chmod +x /path/to/hw1/sat -> chmod +x /Users/fatoumatadembele/Desktop/cs242/hw1/sat

# Running the Code:
To run the code with a SAT problem file:
    - View the SAT problem file:
        - cat /path/to/hw1/sat-problem1.txt -> cat /Users/fatoumatadembele/Desktop/cs242/hw1/sat

    - Execute the SAT solver on the problem file:
        -  ./sat < /path/to/hw1/sat-problem1.txt -> ./sat < /Users/fatoumatadembele/Desktop/cs242/hw1/sat

- Example from my terminal:
cat /Users/fatoumatadembele/Desktop/cs242/hw1/sat-problem1.txt
./sat < /Users/fatoumatadembele/Desktop/cs242/hw1/sat-problem1.txt

# Test Files and Expected Results
    sat-problem1.txt - Expected output: satisfiable
    sat-problem2.txt - Expected output: unsatisfiable
    sat-problem3.txt - Expected output: satisfiable
    sat-problem4.txt - Expected output: satisfiable
    sat-problem5.txt - Expected output: unsatisfiable
    sat-problem6.txt - Expected output: unsatisfiable
    sat-problem7.txt - Expected output: satisfiable

# References and Attributions

Python Documentation:
- The code utilizes itertools.product for generating combinations of truth assignments. 
- This function efficiently handles the iteration over all possible truth assignments.

Reference
Python itertools.product (https://docs.python.org/3/library/itertools.html#itertools.product)

Course Materials: 
The overall structure of the SAT problem solver, including CNF parsing and brute-force assignment checking, 
was inspired by general concepts discussed in lectures and course readings.

Original Code: 
All the code, except for the use of Python’s built-in libraries, was written by Fatima Dembele. 
No other code was copied or adapted from external sources beyond standard Python libraries.
