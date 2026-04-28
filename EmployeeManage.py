import os
import ast
from matplotlib.pylab import rint 

FILENAME = "employees.txt"

class Employee:
    def __init__(self, name, idNumber, department, title):
        self.name = name 
        self.idNumber = idNumber
        self.department = department
        self.title = title
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.idNumber}, Department: {self.department}, Title: {self.title}"
    
    def update(self, name=None, department=None, title=None):
        if name is not None:
            self.name = name
        if department is not None:
            self.department = department
        if title is not None:
            self.title = title

emp1 = Employee("Susan Meyers", 47800, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39120, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81744, "Manufacturing", "Engineer")

emp_dict = {}

if (os.path.exists(FILENAME)):
    with open(FILENAME, "r") as f:
        for line in f:
            emp = ast.literal_eval(line.strip())
            emp_dict[emp["idNumber"]] = emp
 
else:
    for emp in [emp1, emp2, emp3]:
        emp_dict[emp.idNumber] = vars(emp)
    f = open(FILENAME, "w")
    for emp in emp_dict.values():
        f.write(str(emp) + "\n")
    f.close()


def main():

    while True:
        print("\nEmployee Management Menu")
        print("1. Look up employee")
        print("2. Add employee")
        print("3. Update employee")
        print("4. Delete employee")
        print("5. Quit")

        choice = input("Enter choice: ")
        
        if choice == "1":
            emp_id = int(input("Enter ID: "))
            with open(FILENAME, "r") as f:
                for line in f:
                    if str(emp_id) in line:
                        print("Employee with ID " + str(emp_id) + " found: " + line.strip())
                        break
                else:
                    print("Employee with ID " + str(emp_id) + " not found.")

        elif choice == "2":
            name = input("Name: ")
            emp_id = int(input("ID: "))
            dept = input("Department: ")
            title = input("Job Title: ")

            new_emp = Employee(name, emp_id, dept, title)
            emp_dict[new_emp.idNumber] = vars(new_emp)
            f = open(FILENAME, "a")
            f.write(str(emp_dict[new_emp.idNumber]) + "\n")
            f.close()
            print("Employee added.")

        elif choice == "3":
            emp_id = int(input("Enter ID to update: "))
            if emp_id in emp_dict:
                name = input("New Name: ")
                dept = input("New Department: ")
                title = input("New Job Title: ")

                emp_dict[emp_id].update(name=name, department=dept, title=title)
                
                with open(FILENAME, "w") as f:
                    for emp in emp_dict.values():
                        f.write(str(emp) + "\n")
                
                print("Employee updated.")
                print(emp_dict[emp_id])
            else:
                print("Employee not found.")

        elif choice == "4":
            emp_id = int(input("Enter ID to delete: "))
            if emp_id in emp_dict:
                del emp_dict[emp_id]

                with open(FILENAME, "w") as f:
                    for emp in emp_dict.values():
                        f.write(str(emp) + "\n")

                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == "5":
            #save_data(employees)
            print("Data saved. Exiting program.")
            break

        elif choice == "6":
            print(emp_dict.values())       

        else:
            print("Invalid choice.")


main()