"""
Intentional test file for an AI Code Review Agent.

This file contains deliberate bugs and security issues.
Use it only in a disposable test repository. Do not use these patterns
in production code.
"""

import os
import sqlite3
from pathlib import Path

# Deliberately hard-coded secret for secret-scanning tests.
DATABASE_PASSWORD = "test_password_123"


def get_user_profile(user_id):
    """Fetch a user profile (intentionally contains SQL injection risk)."""
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    # BUG: user_id is interpolated directly into SQL.
    query = f"SELECT id, username, email FROM users WHERE id = {user_id}"
    cursor.execute(query)

    profile = cursor.fetchone()
    connection.close()
    return profile


def read_config(config_path):
    """Read a config file (intentionally lacks error handling)."""
    # BUG: file may not exist; exception is not handled.
    with open(config_path, "r") as config_file:
        return config_file.read()


def calculate_average(values):
    """Calculate average (intentionally fails for an empty list)."""
    # BUG: ZeroDivisionError when values is empty.
    return sum(values) / len(values)


def save_report(report_text, output_path):
    """Save report (intentionally uses an unsafe path)."""
    # BUG: user-controlled paths may overwrite unintended files.
    path = Path(output_path)
    path.write_text(report_text, encoding="utf-8")


def run_command(command):
    """Run a command (intentionally unsafe)."""
    # BUG: shell=True with untrusted input can allow command injection.
    return os.system(command)


def main():
    print("Profile:", get_user_profile("1 OR 1=1"))
    print("Average:", calculate_average([]))
    print("Config:", read_config("missing-config.txt"))
    print("Command status:", run_command("echo test"))


if __name__ == "__main__":
    main()
