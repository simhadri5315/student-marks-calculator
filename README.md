# Student Marks & Grade Calculator (Python)

A simple Python console application that calculates a student's total marks, percentage and grade from three subjects.  
The result is also stored in a CSV file, which can be viewed later in applications like Excel.

---

## 📌 Features

- Accepts student name and 3 subject marks
- Calculates:
  - Total Marks
  - Percentage
  - Grade (A, B, C or Fail)
- Supports decimal marks (e.g., 99.5)
- Saves the result in a CSV file (`students.csv`)
- Can store multiple student records

---

## 🛠️ Technologies Used

- Python
- CSV File Handling
- File I/O (`open`, `read`, `write`)
- Conditional Statements (`if-elif-else`)
- Basic Input Validation (`float()`)

---

## 🚀 How to Run

### ▶️ Command

```bash
python student_marks.py


Input:
Enter Student Name: Ravi
Enter Subject 1 marks: 90
Enter Subject 2 marks: 85.5
Enter Subject 3 marks: 70

output:
------ Result ------
Name: Ravi
Total: 245.5
Percentage: 81.83
Grade: A

CSV file Output:

| Name | Sub1 | Sub2 | Sub3 | Total | Percentage | Grade |
| ---- | ---- | ---- | ---- | ----- | ---------- | ----- |
| Ravi | 90   | 85.5 | 70   | 245.5 | 81.83      | A     |


