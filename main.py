class Student:
  def __init__(self, name):
    self.name = name

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

ford = Garage()
ford.cars.append('Fiesta')

print(ford[0])

xx