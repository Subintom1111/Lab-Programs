import csv
csv_string = &quot;&quot;&quot;a,b,c
d,e,f
g,h,i&quot;&quot;&quot;
print(&quot;Original string:&quot;)
print(csv_string)
lines = csv_string.splitlines()
print(&quot;List of CSV formatted strings:&quot;)
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print(&quot;\nList representation of the CSV file:&quot;)
print(parsed_csv)
