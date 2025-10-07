"""
Program to determine score status
"""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """get a valid score, then process menu options until quit."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive"""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):
    """Determine the results based on the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score"""
    print("*" * int(score))


main()
