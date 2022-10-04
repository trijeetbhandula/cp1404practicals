# 1st Program
"""To get user name, and then write it in a file "name.txt" """
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2nd Program
"""To open "name.txt" then read and print the name """
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# 3rd Program
"""Program to read only first two lines of "numbers.txt" and printing the sum of it"""
sum = 0
with open("numbers.txt", "r") as in_file:
    for i in range(2):
        sum += int(in_file.readline())
print(f"The sum of first two numbers is {sum}.")

# 4th Program
"""To print the total of all lines in "numbers.txt" """
in_file = open("numbers.txt", "r")
sum = 0
for line in in_file:
    number = int(line)
    sum += number
in_file.close()
print(f"The sum of all the lines is {sum}")
