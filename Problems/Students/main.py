class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = self.create_id()
        # calculate the id here

    def create_id(self):
        identity = self.name[0] + self.last_name + self.birth_year
        return identity


name, last_name, birth_year = [input() for i in range(3)]

student_one = Student(name, last_name, birth_year)
print(student_one.id)
