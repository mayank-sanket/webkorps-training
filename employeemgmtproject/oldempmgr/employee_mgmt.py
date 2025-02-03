from database import connect_db
# def add_assets():
    
   

#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()
        
#         cursor.execute("insert into assets default values")
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Assets added successfully!")

# ------------------------------------------------------------------------- 
def add_employee(name, age, department, salary, email):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "insert into employees (name, age, department, salary, email) values (%s, %s, %s, %s, %s)" 
        cursor.execute(query, (name, age, department, salary, email))
        conn.commit()
        cursor.close()

        # conn.close()
        print("Employee added successfully!")
    
def view_employees(limit):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = f"select * from employees order by id desc limit {limit}"
        cursor.execute(query)
        employees = cursor.fetchall()
        cursor.close()
        # conn.close()

       
        
        if employees:
            print("\nID | Name | Age | Department | Salary | Email")
            print("-" * 40)
            for emp in employees:  
                print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4] } | {emp[5]}")
        else:
            print("No employees found.")



def update_employee(emp_id, name, age, department, salary, email):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "update employees set name=%s, age=%s, department=%s, salary=%s, email = %s where id=%s"
        cursor.execute(query, (name, age, department, salary, email, emp_id ))
        conn.commit()
        cursor.close()
        # conn.close()
        print("Employee updated successfully!")


def delete_employee(emp_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("delete from employees where id = %s", (emp_id,))  
        conn.commit()
        cursor.close()
        # conn.close()
        print("Employee deleted successfully!")
        



def view_assets(id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()


        query = "select * from assets where id = %s"
        cursor.execute(query, (id,))
        assets = cursor.fetchall()
        cursor.close()
        # conn.close()

       
        
        if assets:
            print("\n ID | Laptop | Charger | Mouse | Keyboard")
            print("-" * 40)
            for asset in assets:  
                print(f"{asset[0]} | {asset[1]} | {asset[2]} | {asset[3]} | {asset[4] } ")
        else:
            print("No assets found.")

