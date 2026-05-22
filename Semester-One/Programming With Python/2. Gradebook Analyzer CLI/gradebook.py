# Name: Prabhat Bhatia
# Date: 04/11/2025
# Project: GradeBook Analyzer

import csv

# Task 1: Welcome Message
def welcome_msg():
    print("-----------------------------------------")
    print("GradeBook Analyser by Prabhat Bhatia")
    print("\nHow would you like to load data?")
    print("1. Manual Entry (Type names and marks one by one)")
    print("2. CSV Import (Load a .csv file)")
    print("Q. Quit")
    print("-----------------------------------------")

# Task 2: (a) Data Entry
def get_manual_marks():
    print("\n=> Manual Data Entry ")
    print("\nEnter student name and marks (0-100).\n")

    marks_dict = {}
    while True:
        name = input("Enter student name: ").strip()
        try:
            score_input = input(f"Enter {name}'s mark (0-100): \n")
            score = int(score_input)
            if score in range(0,101):
                marks_dict[name] = score
                print(f"-> Added {name} with {score} marks.")
            else:
                print("!! Invalid mark. Please enter a number between 0 and 100.")
        
        except ValueError:
            print(f"\n'{score_input}' is not a valid number. Please try again for {name}.")

        ch = input("\nDo you want to enter more names? [Y/N]: ").strip().lower()
        if ch == 'n':
            break
            
    print(f"\nManual entry complete. {len(marks_dict)} students recorded.")
    return marks_dict

# Task 2: (b) CSV Import
def get_csv_marks():
    print("\n=>CSV Data Import")
    fname = input("Enter the name of the csv file: ").strip()

    marks_dict = {}

    try:
        with open(fname, "r") as f:
            robj = csv.reader(f)

            for row in robj:
                if len(row) >= 2:  # Should have atleast 2 columns to be valid
                    name = row[0].strip().title()  # Row 1 = Take name
                    score_string = row[1].strip()  # Row 2 = Take score as a string first

                    try:
                        score = int(score_string) # Now, try to convert
                        
                        if name and 0 <= score <= 100:
                            marks_dict[name] = score
                        else:
                            print(f"  [Warning] Skipping data (score out of range): {row}")
                    
                    except ValueError:
                        print(f"Skipping: {row}")

    except FileNotFoundError:
        print(f"\n-> ERROR! File not found: '{fname}'")
        return None
    
    except Exception as e:
        print(f"\n-> ERROR: {e}")
        return None

    else:
        print(f"\nCSV import complete. {len(marks_dict)} students loaded from '{fname}'.")
        return marks_dict
    
# Task 3: Statistical Analysis Functions
def calculate_average(marks): # Takes the marks dict and returns the average.
    s_list = list(marks.values())
    if not s_list:
        return None
    total = sum(s_list)
    num = len(s_list)
    return total / num

def calculate_median(marks):  # Takes the marks dict and returns the median.
    values = sorted(marks.values())
    if not values:
        return None
    n = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        return values[n // 2]

def find_max_score(marks):  # Takes the marks dict and returns the highest score.
    s_list = list(marks.values())
    if not s_list:
        return 0
    return max(s_list)

def find_min_score(marks):  # Takes the marks dict and returns the lowest score.
    s_list = list(marks.values())
    if not s_list:
        return 0
    return min(s_list)

def print_stats(marks):
    num_students = len(marks)
    avg_score = calculate_average(marks)
    med_score = calculate_median(marks)
    max_val = find_max_score(marks)
    min_val = find_min_score(marks)

    max_name = ""
    min_name = ""
    for name, score in marks.items():
        if score == max_val:
            max_name = name
        if score == min_val:
            min_name = name

    # Print the report
    print("\n-- Class Statistics --")
    print(f"Total Students:   {num_students}")
    print(f"Average Score:    {avg_score}")
    print(f"Median Score:     {med_score}")
    print(f"Highest Score:    {max_val} (by {max_name})")
    print(f"Lowest Score:     {min_val} (by {min_name})")

# Task 4: Grade Assignment 
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        grades[name] = get_letter_grade(score)
    
    print("Letter grades have been assigned.")
    return grades

def print_grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for g in grades.values():
        dist[g] += 1
    print("\n-- Grade Distribution --")
    print(f"Grade A: {dist['A']} student(s)")
    print(f"Grade B: {dist['B']} student(s)")
    print(f"Grade C: {dist['C']} student(s)")
    print(f"Grade D: {dist['D']} student(s)")
    print(f"Grade F: {dist['F']} student(s)")

# --- Task 5: Pass/Fail Filter ---
def print_p_f_filter(marks, pass_mark=40): # Uses list comprehensions for tasks
    failed_names = [name for name, score in marks.items() if score < pass_mark]
    passed_names = [name for name, score in marks.items() if score >= pass_mark]

    print(f"\n-- Pass/Fail Analysis (Passing = {pass_mark}) --")
    print(f"Total Passed: {len(passed_names)}")
    print(f"Students: {', '.join(passed_names)}")
    print(f"\nTotal Failed: {len(failed_names)}")
    print(f"Students: {', '.join(failed_names)}")

# Task 6: Results Table
def print_results_table(marks, grades):  
    print("\n-- Full Student Report --")
    print("Name\tMarks\tGrade")
    print("--------------------------")
    for name, score in sorted(marks.items()):
        print(name, score, grades[name], sep="\t")
    print("--------------------------")

# Bonus Task: 
def export_to_csv(marks, grades):# Exports the final report to a CSV file.
    choice = input("Would you like to export this full report to a CSV file? (y/n): ").strip().lower()
    if choice != 'y':
        print("Skipping export")
        return

    fname = input("Enter a name for your export file:: ").strip()
        
    try:
        with open(fname, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Marks', 'Grade'])
            for name, score in sorted(marks.items()):
                writer.writerow([name, score, grades[name]])
                
        print(f"\nSuccess! Report exported to '{fname}'")
        
    except Exception as e:
        print(f"\nERROR! Could not write to file. {e}")

# Main Program
def main():
    while True:
        welcome_msg()
        choice = input("Your choice (1, 2, or Q): ").strip().lower()
        marks_data = None

        if choice == '1':
            marks_data = get_manual_marks()
        elif choice == '2':
            marks_data = get_csv_marks()
        elif choice == 'q':
            print("\nEnding code.")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or Q.")
            continue

        if marks_data:
            print_stats(marks_data)
            grades_data = assign_grades(marks_data)
            print_grade_distribution(grades_data)
            print_p_f_filter(marks_data, pass_mark=40)
            print_results_table(marks_data, grades_data)
            export_to_csv(marks_data, grades_data)

        print("\n" + "="*40)
        rep = input("Do you want to repeat the process? (y/n): ").strip().lower()
        if rep != 'y':
            print("\nEnding code.")
            break


main()
