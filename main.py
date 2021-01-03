operations = {
  "average": lambda seq: sum(seq) / len(seq),
  "total": lambda seq: sum(seq),
  "max": lambda seq: max(seq)
}

values = [10, 100, 1000]

average = operations["average"](values)
print(f"Average of the values: {average}")
total = operations["total"](values)
print(f"Total value: {total}")
max = operations["max"](values)
print(f"Max value: {max}")