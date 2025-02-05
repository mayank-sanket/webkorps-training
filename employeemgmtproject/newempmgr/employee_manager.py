from database import Database
import os


class EmployeeManager:
    def __init__(self):
        self.db = Database()

    def add_employee(self, name, age, department, salary, email):
        query = "insert into employees (name, age, department, salary, email) values (%s, %s, %s, %s, %s);"
        self.db.cursor.execute(query, (name, age, department, salary, email))
        self.db.commit()
        print("Employee added successfully.")

    def view_employees(self):
        # self.db.cursor.execute("select * from employees")
       
        # employees = self.db.cursor.fetchall()
        # print("\nID | Name | Age | Department | Salary | Email")
        # for emp in employees:  
                # print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4] } | {emp[5]}")


         self.db.cursor.execute("select name, department, age from employees")
         row = self.db.cursor.fetchall()
         data = list(row)
        #  print(data)
         clear_data = [dict(row) for row in data]
         print(clear_data)

         if clear_data[1].get('name') == 'Mayank Sanket':
            print('Mayank found at 1st index')

            try:
                file = open('names.txt', 'w')
                file.write('Mayank Sanket')
                file.close()
            except Exception as e:
                print('Error while loading data')
            finally:
                print('File Saved!')
       
         
        #  self.db.cursor.execute('select name, department, email from employees')

        #  rw = self.db.cursor.fetchone()
        #  print(rw['name'], rw['department'], rw['email'])

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
