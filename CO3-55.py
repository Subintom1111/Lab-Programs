import csv
f=open("Data.csv",newline='')
csv_reader=csv.reader(f)
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))

