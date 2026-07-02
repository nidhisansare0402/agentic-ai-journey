# Building my first AI agent.
# Agent class
class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def respond(self, message: str) -> str:
        print(f"{self.name} ({self.role}) received message: {message}")


# Agent objects
teacher = Agent("Rohini", "Teacher")
recruiter = Agent("Rohit", "Recruiter")
analyst = Agent("Rohit", "Data Analyst")
career_mentor = Agent("CareerBot", "Career Mentor")

# Testing the agents
teacher.respond("Can you explain the concept of linear regression?")
recruiter.respond("What are the key skills you're looking for in a candidate?")
analyst.respond("Can you help me analyze this dataset?")
career_mentor.respond("I can help you with career-related advice.")