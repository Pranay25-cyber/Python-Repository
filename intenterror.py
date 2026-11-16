"""
INTENTIONALLY BUGGY FILE FOR AI CODE REVIEW / AUTOMATIC FIX TESTING.

Do not use this file in production.
The issues below are deliberate so your code-review agent has findings to detect.
"""

import os
import subprocess
import json  # intentionally unused


API_PASSWORD = "admin123"  # security issue: hardcoded credential


def calculate_total(prices, tax_rate=0.10):
    # Bug: total is not initialized before it is used.
    for price in prices:
        total += price

    # Bug: tax_rate is ignored.
    return total


def get_user_profile(user_id):
    # Bug: user_name is not defined.
    return {
        "id": user_id,
        "name": user_name,
    }


def run_user_command(command):
    # Security issue: shell=True with externally supplied input.
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def parse_user_data(raw_value):
    # Security issue: eval can execute arbitrary Python expressions.
    return eval(raw_value)


def divide_numbers(first, second):
    # Bug: division by zero is not handled.
    return first / second


if __name__ == "__main__":
    print("Total:", calculate_total([100, 200, 300]))
    print("Profile:", get_user_profile(101))
    print("Parsed:", parse_user_data("{'active': True}"))
    print("Division:", divide_numbers(10, 0))
