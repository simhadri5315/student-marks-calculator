import csv

name = input("Enter Student Name: ")
m1 = float(input("Enter Python marks: "))
m2 = float(input("Enter Reasoning marks: "))
m3 = float(input("Enter Aptitude marks: "))

total = m1 + m2 + m3
percentage = total/3

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

with open("students.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, m1, m2, m3, total, percentage, grade])

print("------ Result ------")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
