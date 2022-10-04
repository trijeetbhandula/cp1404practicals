import random

for i in range(1, 21):
    print(random.randint(5, 20), end=", ")  # line 1
print()

for i in range(1, 21):
    print(random.randrange(3, 10, 2), end=", ")  # line 2
print()

for i in range(1, 21):
    print(random.uniform(2.5, 5.5), end=", ")  # line 3
print()

# Random Numbers Question
"""
Q. What did you see on line 1?
Ans: On running it 20 times in a loop it returns different integers ranging from 5 to 20 including 5 and 20.
Q. What was the smallest number you could have seen, what was the largest?
Ans: Smallest number is 5, Largest number is 20.
Q. What did you see on line 2?
Ans: It will return a random odd integer in the range of 3 to 10 as it will jump 2 numbers everytime. 
Q. What was the smallest number you could have seen, what was the largest?
Ans: The smallest number can be 3 and the largest number can be 9.
Q. Could line 2 have produced a 4?
Ans: Line 2 can't produce a 4, as it starts with 3 and it will gonna jump by 2 numbers.
So it can only produce:- 3,5,7 and 9.
Q. What did you see on line 3?
Ans: It returns a random float number between 2.5 to 5.5.
Q. What was the smallest number you could have seen, what was the largest?
Ans: Smallest number: 2.5, Largest number: 5.5
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
# Random module was already imported so not necessary to import again.
