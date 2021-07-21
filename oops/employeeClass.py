class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


employee1 = Employee("devanand", 19, 50_000)
employee2 = Employee("bob", 17, 55_000)

print(employee1.__dict__)
employee1Dict = employee1.__dict__
employee2Dict = employee2.__dict__
print("details of ", employee1.name)
for key, value in employee1Dict.items():
    print(key, " : ", value)
print("\ndetails of employee ", employee2.name)
for key, value in employee2Dict.items():
    print(key, " : ", value)
