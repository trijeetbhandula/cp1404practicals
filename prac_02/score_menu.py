"""
Score Menu
Get a valid score and print score status or stars (*) equivalent to score
"""

MENU_STRING = "(S)tars\n(D)etermine Result\n(Q)uit"


def main():
    """Get score, and display stars or score status"""
    score = get_valid_score()
    print(MENU_STRING)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "S":
            print_stars(score)
        elif choice == "D":
            print(determine_score_status(score))
        else:
            print("Invalid choice")
        print(MENU_STRING)
        choice = input(">>>").upper()
    print("Finished")


def print_stars(score):
    print("*" * int(score))


def get_valid_score():
    """Get a valid score"""
    score = float(input("Enter your score: "))
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
