# -------------------- Decorator 1 --------------------
def login_required(func):
    def wrapper(*args, **kwargs):
        print("Login Successful")
        return func(*args, **kwargs)
    return wrapper
    
# -------------------- Decorator 2 --------------------
def activity_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Activity Logged: Viewing profile of {args[0].name}")
        return func(*args, **kwargs)
    return wrapper
    
# -------------------- Student Class --------------------
class Student:
    def __init__(self, name, roll_no, student_id, branch):
        self.name = name
        self.roll_no = roll_no
        self.student_id = student_id
        self.branch = branch
        
    @login_required
    @activity_logger
    def show_profile(self):
        print("\n----- Student Profile -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Student ID :", self.student_id)
        print("Branch :", self.branch)
        print("---------------------------")
    
# -------------------- Closure --------------------
def make_greeting(message):
    def greet(student):
        print(message + student.name)
    return greet
    
# -------------------- Creating Objects --------------------
student1 = Student("Rahul", 101, "MIT101", "Computer Engineering")
student2 = Student("Priya", 102, "MIT102", "Cybersecurity")

# -------------------- Display Profiles --------------------
student1.show_profile()
print()
student2.show_profile()
print()

# -------------------- Greeting Closures --------------------
welcome = make_greeting("Welcome ")
good_morning = make_greeting("Good Morning ")
good_evening = make_greeting("Good Evening ")

# -------------------- Using Closures --------------------
welcome(student1)
good_morning(student2)
good_evening(student1)
