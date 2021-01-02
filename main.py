list1 = ['A', 'P', 'D', 'E']
list2 = ['A', 'P', 'B']

list = [
  value
  for value in list2
  if value.lower() in [val.lower() for val in list1]
]

print(list)