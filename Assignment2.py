# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Gustavo Gonzalez
# Assignment Number: Lab2
# Due Date: 06/19/2026
# Purpose: The program is created to read a file of student data and display the students in order of their average grades.
# 1.


def main():
    # Read student data from a file and display them in order of their average grades.
    filename = "Assignment2input.txt"
    students = []

    # Read the student data from the file and accounting for formatting issues.
    with open(filename, "r", ) as file:
        for line in file:
            fields = line.split()
            if fields:
                name = fields[0]                                              # First field is the student's name
                average = sum(float(s) for s in fields[1:]) / len(fields[1:]) # Average the remaining score fields
                students.append((name, average)) 

    # Sort the students by their average grades in descending order and display them.
    for name, avg in sorted(students, key=lambda s: s[1], reverse=True):
        print(f"{name} {avg:.2f}")


if __name__ == "__main__":
    main()
