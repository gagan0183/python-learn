operations = {
  "average": lambda seq: sum(seq) / len(seq),
  "total": lambda seq: sum(seq),
  "max": lambda seq: max(seq)
}

values = [10, 100, 1000]

average = operations["average"](values)
total = operations["total"](values)
max = operations["max"](values)
print(f"Average of the values: {average}")
print(f"Total value: {total}")
print(f"Max value: {max}")