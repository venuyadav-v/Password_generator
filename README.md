Password Generator

A simple command-line password generator written in Python. It builds a random password using a custom mix of letters, special characters, and numbers based on user input.

Features
Prompts the user for how many letters, special characters, and numbers to include
Randomly selects characters from each category
Shuffles the final character list so the password isn't grouped by type
Prints the generated password to the console
Requirements
Python 3.x (no external libraries required — uses only the built-in random module)
Usage
Run the script:
bash
   python Project2.py
Enter the number of letters, special characters, and numbers when prompted.
The script will print the password-building steps and the final generated password.
Example
Welcome to the passsword generator!...
How many letters would you like in your password?4
How many spetial charactors would you like in your password?2
How many numbers would you like in your password?3
['G', 'k', 'q', 'T', '@', '#', '5', '1', '9']
['5', 'T', '@', 'G', '9', 'k', '#', 'q', '1']
5T@G9k#q1
Possible Improvements
Add input validation (currently negative numbers or non-numeric input will crash the program)
Avoid using char as a loop variable name conflicting with lists built via += (list concatenation vs. append)
Fix typos in variable names (spetial → special, final_passpord → final_password)
Add an option to copy the password directly to the clipboard
Allow the user to exclude ambiguous characters (like 0, O, l, 1)
License

Feel free to use and modify this project for personal or educational purposes.
