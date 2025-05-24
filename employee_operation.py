class EmployeeOperation:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.get_name()} added successfully.")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print("List of Employees:")
        for employee in self.employees:
            print(f"ID: {employee.get_id()}, Name: {employee.get_name()}")
