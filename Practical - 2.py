#----------- Decorator Function ------------
def report_deco(func):
    def wrapper(*args,**kwargs):
        print("=" * 50)
        print("DYNAMIC REPORT GENERATOR".center(50))
        print("="*50)
        
        func(*args,**kwargs)
        
        print("=" * 50)
        print("END OF REPORT".center(50))
        print("="*50)
        
    return wrapper

#------------ CLass -----------    
class Library:
    
    library_name="MIT ADT Library"
    
    def __init__(self,student_name,book_name,):
        self.student_name = student_name
        self.book_name = book_name
        self.activities = []
        
    def add_activity(self,activity):
        self.activities.append(activity)
        
    @classmethod
    def change_library(cls,new_name):
        cls.change_name = new_name
        
    @staticmethod
    def message():
        print("Library Management System")
        
    def __str__(self):
        return f"Student Name: {self.student_name}\nBook name: {self.book_name}"
        
    def __len__(self):
        return len(self.activities)
        
        
    @report_deco
    def show_report(self):
        
        Library.message()
        print("Library:",Library.library_name)
        print(self)
        
        print("\nActivities:")
        
        for i, activity in enumerate(self.activities, start = 1):
            print(f"{i}.{activity}")
            
        print("\nTotal Activities: ",len(self))
        
        
l1 = Library("Aditya Deshpande", "Cyber Security")
l1.add_activity("Book Issued")
l1.add_activity("Completed Chapter 1")
l1.add_activity("Returned on Time")

Library.change_library("Central Digital Library")

l2 = Library("Prabhu Patil", "Python Programming")
l2.add_activity("Book issued")
l2.add_activity("Renewed for 7 days")
l2.add_activity("Returned Successfully")

l3 = Library("Pratik Kshirsagar", "Data Science")
l3.add_activity("Book Issued")
l3.add_activity("Completed Reading")
l3.add_activity("Book Returned")




while True:
    
    print("\n========== MENU ==========")
    print("1. View Report 1")
    print("2. View Report 2")
    print("3. View Report 3")
    print("4. View All Reports ")
    print("5. Change Library Name")
    print("6. Exit")
    
    choice= int(input("Enter your Choice:"))
    
    if choice == 1:
        l1.show_report()
    
    elif choice == 2:
        l2.show_report()
        
    elif choice == 3:
        l3.show_report()
        
    elif choice == 4:
        l1.show_report()
        l2.show_report()
        l3.show_report()
        
    elif choice == 5:
        new_name = input("Enter New Library Name:")
        Library.change_library(new_name)
        print("Library Name Updated Successfully")
    
    elif choice == 6:
        print("Thank You!")
        break