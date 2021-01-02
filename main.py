list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
list = [value.lower() for value in list]

alphabet = input("Enter an alphabet: ")
if alphabet.lower() in list:
  print("Alphabet is present")