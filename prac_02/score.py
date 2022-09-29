"""
Program to determine score status
"""


def main():
    """Get users score and print result"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))


def determine_score_status(score):
    """To determine the status of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
