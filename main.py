age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[-2:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day}/{month}/{year+5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year+age}" # str: last birthday formatted as day/month/year
# day, month, year = 12,7,12
adding_10_m = month + 10 - 1
month = (adding_10_m % 12) + 1
year = year + (adding_10_m // 12)

tenth_month = f"{day}/{month}/{year}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month, fifth_birthday, last_birthday, sep=", ")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = f"{int(weight // 1)} kg {int((weight - (weight // 1))*1000)} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)
# print(adding_10_m // 12, month)