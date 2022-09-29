"""
Program to determine score status
"""

from random import randint


def main():
    """Get users score and print result"""
    score = get_valid_score()
    print(f"Score: {score}, Result: {determine_score_status(score)}")
    # Using a random integer for score
    print("Using a random score between 0 to 100, the result will be: ")
    score = randint(0, 100)
    print(f"Score: {score}, Result: {determine_score_status(score)}")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_score_status(score):
    """To determine the status of score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
