class Employee:
    def __init__(self, emp_name, emp_salary, emp_role):
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_role = emp_role

    def display_info(self):
        """Show the employee's current details."""
        print(f"Employee Name : {self.emp_name}")
        print(f"Salary        : ${self.emp_salary}")
        print(f"Job Title     : {self.emp_role}")
        print("-" * 40)

    def give_raise(self, raise_amount):
        """Increase the salary by a given amount and display new salary."""
        self.emp_salary += raise_amount
        print(f"{self.emp_name} has received a raise of ${raise_amount}!")
        print(f"Updated Salary: ${self.emp_salary}")
        print("-" * 40)


def main():
    # Creating Employee objects with unique data
    employees = [
        Employee("Sundar Gurung", 4200.00, "Web Designer"),
        Employee("Manish Jirel", 5500.50, "Team Lead")
    ]

    # Display information for each employee
    print("\n--- Employee Details ---")
    for emp in employees:
        emp.display_info()

    # Give raises to employees
    employees[0].give_raise(800)
    employees[1].give_raise(1200.75)


if __name__ == "__main__":
    main()
