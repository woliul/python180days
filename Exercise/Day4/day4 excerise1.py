#Create a dictionary for a student with keys
student_info={
    "Name":str(input("Enter your Name:")),
    "Age":int(input("Enter your Age:")),
    "Grade":float(input("Enter your Grade:")),
    "Subject":str(input("Enter your Subject:")),
}

print(student_info)
print(student_info["Subject"])

for key in student_info.keys():
    if student_info[key] == student_info["Subject"]:
        print(key)
        break
for value in student_info.items():
    if value[1] == student_info["Subject"]:
        print(value)
        break
