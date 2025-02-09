# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0: # the terminal condition
        total += n # add n to the total
        n = int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line == "END": # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += quantity*price # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    str = str(input())
    while str != "STOP":
        if str.endswith("ed") or str.endswith("ing"):
            print(str)
        str = input()

elif task == "reverse_sum_palindrome":
    num = int(input())
    while num != -1:
        length = len(str(num))
        sum = 0
        i = 0
        while length > 0:
            sum = sum + int(str(num)[i])
            i += 1
            length -= 1
        if sum == int(str(sum)[::-1]):
            print(num)
        num = int(input())

elif task == "double_string":
    line = str(input())
    while line != "":
        print(line * 2)
        line = str(input())

elif task == "odd_char":
    s = str(input())
    while not s.endswith("."):
        print(s[::2], end = " ")
        s = str(input())
        if (s.endswith(".")):
            print(s[::2])

elif task == "only_even_squares":
    num = str(input())
    while num != "NAN":
        number = int(num)
        if number % 2 == 0:
            print(number*number)
        num = str(input())

elif task == "only_odd_lines":
    line = str(input())
    odd_lines = []
    lineNumber = 1
    while line != "END":
        if lineNumber % 2 != 0:
            odd_lines.insert(0, line)
        lineNumber += 1
        line = str(input())
    i = 0
    while i < len(odd_lines):
        print(odd_lines[i])
        i += 1
