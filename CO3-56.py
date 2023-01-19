import csv
reader = csv.reader(open(&quot;Sample.csv&quot;))
no_lines= len(list(reader))
print(&quot;Number of lines in the given csv: &quot;)
print(no_lines)

