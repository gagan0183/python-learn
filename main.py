def before_and_after(func):
  print("Before")
  func()
  print("After")

def greet():
  print("Hello")

before_and_after(greet)