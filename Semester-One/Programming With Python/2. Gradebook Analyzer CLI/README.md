# GradeBook Analyzer CLI

> Command-line gradebook assistant for quick mark analysis and reporting.

## 1. Project Overview
The script helps lecturers enter or import student marks, run core statistics, assign letter grades, and export a tidy report.

## 2. Features
- **Two data entry modes** – type marks manually or import from a `.csv` file.
- **Class statistics** – average, median, highest score (with student), and lowest score (with student).
- **Automatic grading** – assigns letter grades (A–F) based on score thresholds.
- **Grade distribution** – counts how many students earned each letter grade.
- **Pass / fail filter** – list comprehension separates students using a configurable pass mark (default 40).
- **Tabbed summary table** – prints every student with marks and grade in a clean, tab-separated layout.
- **Optional CSV export** – save the generated report to a new file directly from the CLI.

## 3. Repository Structure
```
gradebook_analyser/
├── gradebook.py
├── students.csv        # example input (optional)
└── final_report.csv    # created when you export results (optional)
```

## 4. Setup & Usage
1. **Download** or clone this repository.
2. **Open a terminal** in the project folder:
   ```bash
   cd gradebook_analyser
   ```
3. **Run the program**:
   ```bash
   python gradebook.py
   ```
4. **Follow the on-screen menu** to choose:
   - `1` – **Manual Entry**: enter student names and marks interactively.
   - `2` – **CSV Import**: load marks from a CSV file in the same folder.
   - `Q` – Quit the application.

### CSV Format Guide
If you import data, make sure your file looks like this (no headers required but supported):
```csv
Name,Mark
Rohan Kumar,88
Priya Sharma,92
Amit Patel,58
```
Marks outside 0–100 or non-numeric values are skipped with a warning so you can fix them later.

## 5. Sample Runs
```
-----------------------------------------
GradeBook Analyser by Prabhat Bhatia

How would you like to load data?
1. Manual Entry (Type names and marks one by one)
2. CSV Import (Load a .csv file)
Q. Quit
-----------------------------------------
Your choice (1, 2, or Q): 1

=> Manual Data Entry 

Enter student name and marks (0-100).

Enter student name: Prabhat Bhatia
Enter Prabhat Bhatia's mark (0-100): 
88
-> Added Prabhat Bhatia with 88 marks.

Do you want to enter more names? [Y/N]: y
Enter student name: Suhani Yadav
Enter Suhani Yadav's mark (0-100): 
99
-> Added Suhani Yadav with 99 marks.

Do you want to enter more names? [Y/N]: y
Enter student name: Aayan Srivastwa
Enter Aayan Srivastwa's mark (0-100): 
58
-> Added Aayan Srivastwa with 58 marks.

Do you want to enter more names? [Y/N]: y
Enter student name: Kumar Partha
Enter Kumar Partha's mark (0-100): 
72
-> Added Kumar Partha with 72 marks.

Do you want to enter more names? [Y/N]: y
Enter student name: Aradhya Mathur
Enter Aradhya Mathur's mark (0-100): 
35
-> Added Aradhya Mathur with 35 marks.

Do you want to enter more names? [Y/N]: n

Manual entry complete. 5 students recorded.

-- Class Statistics --
Total Students:   5
Average Score:    70.4
Median Score:     72
Highest Score:    99 (by Suhani Yadav)
Lowest Score:     35 (by Aradhya Mathur)
Letter grades have been assigned.

-- Grade Distribution --
Grade A: 1 student(s)
Grade B: 1 student(s)
Grade C: 1 student(s)
Grade D: 1 student(s)
Grade F: 1 student(s)

-- Pass/Fail Analysis (Passing = 40) --
Total Passed: 4
Students: Prabhat Bhatia, Suhani Yadav, Aayan Srivastwa, Kumar Partha

Total Failed: 1
Students: Aradhya Mathur

-- Full Student Report --
Name    Marks   Grade
--------------------------
Prabhat Bhatia   88  B
Suhani Yadav     99  A
Aayan Srivastwa  58  D
Kumar Partha     72  C
Aradhya Mathur   35  F
--------------------------

Would you like to export this full report to a CSV file? (y/n): n
Skipping export

========================================
Do you want to repeat the process? (y/n): n

Ending code.
```

### 2. CSV Import (students.csv)
**Sample file:**
```csv
Name,Mark
Prabhat Bhatia,88
Suhani Yadav,99
Aayan Srivastwa,58
Kumar Partha,72
Aradhya Mathur,35

```

**Program output:**
```
-----------------------------------------
GradeBook Analyser by Prabhat Bhatia

How would you like to load data?
1. Manual Entry (Type names and marks one by one)
2. CSV Import (Load a .csv file)
Q. Quit
-----------------------------------------
Your choice (1, 2, or Q): 2

=>CSV Data Import
Enter the name of the csv file: students.csv

CSV import complete. 5 students loaded from 'students.csv'.

-- Class Statistics --
Total Students:   5
Average Score:    70.4
Median Score:     72
Highest Score:    99 (by Suhani Yadav)
Lowest Score:     35 (by Aradhya Mathur)
Letter grades have been assigned.

-- Grade Distribution --
Grade A: 1 student(s)
Grade B: 1 student(s)
Grade C: 1 student(s)
Grade D: 1 student(s)
Grade F: 1 student(s)

-- Pass/Fail Analysis (Passing = 40) --
Total Passed: 4
Students: Prabhat Bhatia, Suhani Yadav, Aayan Srivastwa, Kumar Partha

Total Failed: 1
Students: Aradhya Mathur

-- Full Student Report --
Name    Marks   Grade
--------------------------
Prabhat Bhatia   88  B
Suhani Yadav     99  A
Aayan Srivastwa  58  D
Kumar Partha     72  C
Aradhya Mathur   35  F
--------------------------

Would you like to export this full report to a CSV file? (y/n): y
Enter a name for your export file: final_report.csv

Success! Report exported to 'final_report.csv'

========================================
Do you want to repeat the process? (y/n): n

Ending code.

```

## 6. Author & Course
- Prabhat Bhatia
- B.Tech CSE Cyber Security(First Semester)
- 4th November 2025
- Programming With Python - Lab Assignment 2
