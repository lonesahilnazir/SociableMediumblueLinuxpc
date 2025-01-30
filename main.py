num = int(input("Enter Number: "))
str = str(num)
print(str[::-1])
total = 0
for s in str:
  total += int(s)
print(total)