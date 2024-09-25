class Student:
    def __init__(self):
        self.name = ""
        self.id_number = ""
        self.contact_number = ""
        self.branch_name = ""

    def getdata(self):
        self.name = input("Enter student name: ")
        self.id_number = input("Enter student ID number: ")
        self.contact_number = input("Enter student contact number: ")
        self.branch_name = input("Enter student branch name: ")

    def display(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Branch Name: {self.branch_name}")

student = Student()
student.getdata()
student.display()