class Student:
    def __init__(self, name: str, age: int, group: int, gpa: float):
        self.name = name
        self.age = age
        self.group = group 
        self.gpa = gpa
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Group: {self.group}")
    
    def get_scholarship(self) -> int:
        if self.gpa == 5:
            return 6000
        elif self.gpa < 5:
            return 4000
        return 0
    
    def __gt__(self, other) -> bool:
        return self.get_scholarship() > other.get_scholarship()

class ResearchStudent(Student):
    def __init__(self, name: str, age: int, group: int, gpa: float, research_topic: str):
        super().__init__(name, age, group, gpa)
        self.research_topic = research_topic
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Group: {self.group}, Research: {self.research_topic}")
    
    def get_scholarship(self) -> int:
        if self.gpa == 5:
            return 8000
        elif self.gpa < 5:
            return 6000
        return 0

# 测试用例
if __name__ == "__main__":
    student = Student("Alice", 20, 2023, 4.7)  
    researcher = ResearchStudent("Bob", 25, 2023, 5.0, "Quantum Computing")  
    
    student.show_info()
    print("Student scholarship:", student.get_scholarship())  
    
    researcher.show_info()
    print("Researcher scholarship:", researcher.get_scholarship())  
    
    print("Researcher > Student?", researcher > student)  # True