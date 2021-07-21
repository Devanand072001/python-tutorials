class Student:

    def __init__(self, name, age, couse):
        self.StudentName = name
        self.StudentAge = age
        self.studentCourse = couse


def studentDetails():
    print("enter the details of student\n")
    name = input("name of student: ")
    age = int(input("age of student: "))
    course = input("course of student: ")
    return name, age, course


studen1name, student1age, student1course = studentDetails()
student1 = Student(studen1name, student1age, student1course)

print("\n Details of ", studen1name)
for key, value in student1.__dict__.items():
    print(key, " : ", value)

student2Name, student2Age, student2Course = studentDetails()
student2 = Student(student2Name, student2Age, student2Course)
print("\n details of ", student2Name)
for key, value in student2.__dict__.items():
    print(key, " : ", value)
