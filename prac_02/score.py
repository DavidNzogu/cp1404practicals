"""
Program to determine score status
"""
import random


def main():
    """Ask user for score, print result, and also generate a random score result"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score:.2f} -> {random_result}")


def determine_result(score):
    """Determine the results based on the score (does not print)"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
