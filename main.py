num = int(input("Enter Number: "))
str = str(num)
revStr = str[::-1]
total = 0
for s in str:
  total += int(s)
print(f"Sum of all digits = {total}")

print("Palindrome") if int(str) == int(revStr) else print("Not a palindrome")