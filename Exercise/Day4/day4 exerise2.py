#Modify the dictionary by adding a new key
student_info={
    "Name":str(input("Enter your Name:")),
    "Age":int(input("Enter your Age:")),
    "Grade":float(input("Enter your Grade:")),
    "Subject":str(input("Enter your Subject:")),
}

student_info["hobby"]=str(input("Enter your hobby:"))

print(student_info)