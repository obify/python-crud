import sqlite3

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}"


class EmployeeManager:
    def __init__(self, db_name='employees.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_employee(self, emp_id, name):
        try:
            self.cursor.execute('INSERT INTO employees (id, name) VALUES (?, ?)', (emp_id, name))
            self.conn.commit()
            print(f"Employee {name} added successfully.")
        except sqlite3.IntegrityError:
            print("Employee ID already exists.")

    def read_employee(self, emp_id=None):
        if emp_id:
            self.cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
            row = self.cursor.fetchone()
            if row:
                employee = Employee(*row)
                print(employee)
            else:
                print("Employee not found.")
        else:
            self.cursor.execute('SELECT * FROM employees')
            rows = self.cursor.fetchall()
            if rows:
                for row in rows:
                    print(Employee(*row))
            else:
                print("No employees found.")

    def update_employee(self, emp_id, name):
        self.cursor.execute('UPDATE employees SET name = ? WHERE id = ?', (name, emp_id))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Employee {emp_id} updated.")
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Employee {emp_id} deleted.")
        else:
            print("Employee not found.")

    def close(self):
        self.conn.close()


def menu():
    manager = EmployeeManager()
    try:
        while True:
            print("\n--- Employee Management (SQLite) ---")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. View Employee by ID")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                emp_id = input("Enter ID: ")
                name = input("Enter Name: ")
                manager.create_employee(emp_id, name)

            elif choice == '2':
                manager.read_employee()

            elif choice == '3':
                emp_id = input("Enter Employee ID: ")
                manager.read_employee(emp_id)

            elif choice == '4':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter New Name: ")
                manager.update_employee(emp_id, name)

            elif choice == '5':
                emp_id = input("Enter Employee ID: ")
                manager.delete_employee(emp_id)

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")
    finally:
        manager.close()


if __name__ == "__main__":
    menu()
