cars = ["ok", "ok", "faulty", "ok"]

for status in cars:
  if status == "faulty":
    break;
  print(f"The car has {status} status")
else:
  print("All cars are shipped successfully")