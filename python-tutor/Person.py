"""person1 = {"firstname":"Aungkoon", "lastname": "Kongpet", "gender": "Male", "birthdate": "1993-04-05"}
person2 = {"firstname":"Aungkoon", "lastname": "Kongpet", "gender": "Male", "birthdate": "1993-04-05"}
person3 = {"firstname":"Aungkoon", "lastname": "Kongpet", "gender": "Male", "birthdate": "1993-04-05"}
result = person1["salary"] * 12
result = person1["salary"] * 12
result = person1["salary"] * 12
"""

class Person(): # custom datatype
    #properties/attributes/fields
    firstname: str
    lastname: str
    gender: str
    birthdate: str
    salary: float

    def __init__(self, firstname, lastname, gender, birthdate, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.birthdate = birthdate
        self.salary = salary

    def yearSalary(self) -> float:
        return self.salary * 12

    def getAge(self) -> int:
        dateSplit = self.birthdate.split("-")
        return 2022 - int(dateSplit[0])


per1 = Person("David", "Homes", "Male", "1992-04-05", 80000) #Object
per2 = Person("Sara", "Homes", "Female", "1991-05-05", 60000)
print(per1.firstname)
print(per2.birthdate)

print(per1.yearSalary())
print(per2.yearSalary())
print(per1.getAge())
print(per2.getAge())




