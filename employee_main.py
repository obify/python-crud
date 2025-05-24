from Employee import Employee
from EmployeeOperation import EmployeeOperation

if __name__ == "__main__":
    emp = Employee(1, "John Doe")
    emp_op = EmployeeOperation()
    emp_op.add_employee(emp)
    emp_op.list_employees()
