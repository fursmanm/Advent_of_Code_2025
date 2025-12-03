# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 10:11:47 2025

@author: Fursman
"""

def max_two_digit_in_bank(bank: str) -> int:

    digits = [int(d) for d in bank]
    n = len(digits)
    voltage = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            value = digits[i] * 10 + digits[j]
            if value > voltage:
                voltage = value

    return voltage


def total_from_file(filename: str) -> int:
    total = 0
    with open(filename, "r") as f:
        for line in f:
            bank = line.strip()
            if bank:
                total += max_two_digit_in_bank(bank)
    return total

if __name__ == "__main__":
    filename = r"C:\Users\...\Batteries.txt"
    result = total_from_file(filename)
    print("Total output joltage:", result)
