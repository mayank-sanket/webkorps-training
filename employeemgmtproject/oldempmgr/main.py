from employee_mgmt import add_employee, view_employees, update_employee, delete_employee, view_assets
from display import userscreen
from database import connect_db
def main():

    conn = connect_db()

    while True:
        userscreen() 

        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            email = input('Enter your email: ')
            add_employee(name, age, department, salary, email)

            # add_assets()
            

        elif choice == 2:
            print('Presss A if you want to see the last employee, B if you want all the employees')
            
            view_choice = input('Enter A or B: ').lower()
            if view_choice == 'a':
                view_employees(1)
            
            if view_choice == 'b':
                view_employees(1000)
            
            # break

        elif choice == 3:
            emp_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            department = input("Enter new department: ")
            salary = float(input("Enter new salary: "))
            update_employee(emp_id, name, age, department, salary)

        elif choice == 4:
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(emp_id)

        
        elif choice == 5:
            print('Find assets details of the user: ')
            id = input('Enter the ID of the user: ')

            
            view_assets(id)

        elif choice == 6:
            print("Exiting...")

            conn.close()
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()


