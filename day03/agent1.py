class Agent1:
    "Represent a simple AI Agent"
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hello, I am {self.name}, and I work as a {self.role}.")
    
    @staticmethod
    def greet():
        print("Welcome to the AI Assistant!")

# Calling instance method using each object.
teacher = Agent1("Rohini", "Teacher")
teacher.greet()
teacher.introduce()

analyst = Agent1("Rohit", "Data Analyst")
analyst.greet()
analyst.introduce()

# Calling static method using class name.
Agent1.greet()
