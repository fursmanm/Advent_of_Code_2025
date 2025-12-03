# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 11:47:37 2025

@author: Fursman
"""

def max_twelve_digit_in_bank(bank: str) -> int:

    digits = [int(d) for d in bank]
    stack = []
    to_remove = len(digits) - 12

    for d in digits:
        # remove smaller digits from the stack if needed
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # Take exactly 12 digits
    result_digits = stack[:12]
    # Convert to integer
    result = int("".join(str(d) for d in result_digits))
    return result


def total_from_file(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        for line in f:
            bank = line.strip()
            if bank:
                total += max_twelve_digit_in_bank(bank)
    return total

if __name__ == "__main__":
    filename = r"C:\Users\...\Batteries.txt"
    result = total_from_file(filename)
    print("Total output joltage:", result)
