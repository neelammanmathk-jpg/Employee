# employee.py
# Program to accept employee information and return a formatted string (with default values)

import sys

def get_employee_details(
        name="John Doe",
        emp_id="E1001",
        department="IT",
        salary=50000):
    """Return a formatted employee details string with defaults."""
    return (
        f"Employee Name: {name},"
        f"Employee ID: {emp_id},"
        f"Department: {department},"
        f"Salary: {float(salary):.2f}"
    )


if __name__ == "__main__":
    # Simply print the default formatted string
    print(get_employee_details())
