from datetime import date

def calculate_age(dtob):
today = date.today()
return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

print("My Age is",calculate_age(date(1999,12,27)))

