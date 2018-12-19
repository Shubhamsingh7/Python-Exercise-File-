class Student:

    college_name="Raj Kumar Goel Institute of Technology"

    def __init__(self,name,age,branch,year,obj):
        self.name=name
        self.age=age
        self.branch=branch
        self.year=year
        self.marks=self.marks()

    def config(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Percentage={self.marks}")
        print(f"Branch={self.branch}")
        print(f"year={self.year}")
        print(f"College Name={Student.college_name}")


        class Marks:

            def __init__(self,maths,chemistry,physics):
                self.maths=maths
                self.physics=physics
                self.chemistry=chemistry




class StudentInfo:

    a=int(input("Enter number of Students:"))

    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    branch = input("Enter branch:")
    year = int(input("Enter Year:"))
    physics = float(input("Enter Physics marks:"))
    chemistry = float(input("Enter Chemistry marks:"))
    maths = float(input("Enter Maths marks:"))

    j=Student.Marks(68,89,62)

    i = Student(name, age, branch, year)
    print()
    i.config()
    print()










