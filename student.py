class Student:
    
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
    
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"
    
    def __repr__(self):
        return f"Student(name='{self.name}', roll_number={self.roll_number}, grade='{self.grade}')"

