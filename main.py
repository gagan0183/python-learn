class Student:
  def __init__(self, new_name, new_grades):
    self.name = new_name
    self.grades = new_grades

  def average(self):
    return sum(self.grades)/len(self.grades)

student_one = Student('Name', [100, 1000])

print(student_one.average())