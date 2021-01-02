values = ['A', 'P']
numbers = [1, 2] 

dictionary = {
  values[i]: numbers[i]
  for i in range(len(values))
}

print(dictionary)