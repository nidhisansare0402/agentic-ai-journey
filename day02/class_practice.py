class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"My name is {self.name} and I am enrolled in the {self.course} course.")

student1 = Student("Nidhi", "B.Tech IT")
student1.display_info() 

student2 = Student("Rahul", "Computer Engineering")
student2.display_info() 