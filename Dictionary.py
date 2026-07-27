# Dictionary Example

student = {
    "Name": "Sangeetha",
    "Age": 20,
    "Branch": "AI&DS"
}

print(student)

print("Name:", student["Name"])

student["Age"] = 21

print("Updated Dictionary:", student)

for key, value in student.items():
    print(key, ":", value)
