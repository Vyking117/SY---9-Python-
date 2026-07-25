class Student:
    def __init__(self, name, roll_no, division, marks):
        self.name = name
        self.roll_no = roll_no
        self.division = division
        self.marks = marks
        
    def show_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Division:", self.division)
        print("Marks:", self.marks)
        
    def result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
        print("----------------------")
        
s1 = Student("Aditya", 1, "9th", 85)
s2 = Student("Prabhu", 2, "9th", 72)
s3 = Student("Pratik", 3, "9th", 30)

s1.show_details()
s1.result()

s2.show_details()
s2.result()

s3.show_details()
s3.result()