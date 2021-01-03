# higher order function
# first class function
def before_and_after(func):
  print("Before")
  func()
  print("After")

# first class function
def greet():
  print("Hello")

before_and_after(greet)