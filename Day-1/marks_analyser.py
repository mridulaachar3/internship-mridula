# Student Marks Analyzer

name = input("Enter your name: ")
course = input("Enter your course: ")

try:
    age = int(input("Enter your age: "))
except:
    age = 0
    print("Invalid age entered")

print("\nStudent Details")
print("Name:", name)
print("Course:", course)
print("Age:", age)

print("\nEnter marks for 3 subjects")

mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))

total = mark1 + mark2 + mark3
avg = total / 3
percent = (total / 300) * 100

print("\nTotal =", total)
print("Average =", avg)
print("Percentage =", round(percent, 2), "%")

if avg >= 40:
    print("Result: PASS")
    passed = True
else:
    print("Result: FAIL")
    passed = False

if percent >= 80:
    grade = "Excellent"
elif percent >= 60:
    grade = "Good"
elif percent >= 40:
    grade = "Average"
else:
    grade = "Need Improvement"

print("Grade:", grade)

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("All subjects cleared")
    cleared = True
else:
    print("One or more subjects below 35")
    cleared = False

if passed and cleared:
    print("Eligible for next course")
else:
    print("Not eligible for next course")