from database import Database


class EmployeeManager:
    def __init__(self):
        self.db = Database()

    def add_employee(self, name, age, department, salary, email):
        query = "insert into employees (name, age, department, salary, email) values (%s, %s, %s, %s, %s);"
        self.db.cursor.execute(query, (name, age, department, salary, email))
        self.db.commit()
        print("Employee added successfully.")

    def view_employees(self):
        self.db.cursor.execute("select * from employees")
        employees = self.db.cursor.fetchall()
        print("\nID | Name | Age | Department | Salary | Email")
        for emp in employees:  
                print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4] } | {emp[5]}")

    def update_employee(self, emp_id, name, age, department, salary, email):
        query = "update employees set name=%s, age=%s, department=%s, salary=%s , email = %s where id=%s;"
        self.db.cursor.execute(query, (name, age, department, salary, emp_id, email))
        self.db.commit()
        print("Employee updated successfully.")

    def delete_employee(self, emp_id):
        query = "delete from employees where id=%s;"
        self.db.cursor.execute(query, (emp_id,))
        self.db.commit()
        print("Employee deleted successfully.")

    def close(self):
        self.db.close()
