from employee_manager import EmployeeManager


def main():
    manager = EmployeeManager()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        
        choice = int(input(input("Enter choice: ")))

        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            email = input('Enter email: ')
            manager.add_employee(name, age, department, salary, email)

        elif choice == 2:

            manager.view_employees()
            

        elif choice == 3:
            emp_id = int(input("Enter Employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            department = input("Enter new department: ")
            salary = float(input("Enter new salary: "))
            email = input("Enter the new email: ")
            manager.update_employee(emp_id, name, age, department, salary, email)

        elif choice == 4:
            emp_id = int(input("Enter Employee ID to delete: "))
            manager.delete_employee(emp_id)

        elif choice == 5:
            manager.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
