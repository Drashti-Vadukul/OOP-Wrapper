
# Class Person

class Person:

    def __init__(self,name, age):
        self.__name = name
        self.__age =age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def display(self):
        print("Person Details")
        print("")
        print("Name=",self.__name)
        print("Age=",self.__age)

# Employee Class

class Employee(Person):
    def __init__(self,name ,age ,employee_id ,salary):
        super().__init__(name,age)
        self.__employee_id = employee_id
        self.__salary = salary
      

    def display(self):
        print("Employee Details")
        print("")
        print("Name =", self.get_name())
        print("Age =", self.get_age())
        print("Employee_id", self.__employee_id)
        print("Salary =",self.__salary)
        

# Manager class

class Manager(Employee):
    def __init__(self, name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.__department = department

    def display(self):
        print("Manager Details")
        print("")
        super().display()
        print("Department:",self.__department)

#Developer Class 

class Developer(Employee):
    def __init__(self, name,age,employee_id,salary,language):
        super().__init__(name,age,employee_id,salary)
        self.__language = language

    def display(self):
        print("Developer Details")
        print("")
        super().display()
        print("Language:",self.__language)


object = []
p_obj = None
e_obj = None
m_obj = None
d_obj = None




print("\n---- Python OOP Project: Employee Management System ----")
print("")
print("Choose an Operation :")

while True :

    print("\n1. create a Person")
    print("2. create an Employee")
    print("3. Create Manager")
    print("4. Create Developer")
    print("5. Show Details")
    print("6. Exit ")

   

    choice = int(input("\nEnter Your Choice :"))
    
   


    if choice == 1:

        name = input("\nEnter your Name :")
        age = input("Enter Your Age :")

        p = Person(name ,age)
        p_obj = p
        object.append(p)

        print("\n Person Created with name :",p.get_name(),"and Age :",p.get_age())

    elif choice == 2:

        name = input("\nEnter your Name :")
        age = input("Enter Your Age :")
        employee_id = input("Enter Employee ID :")
        salary = float( input("Enter Salary :"))

        e = Employee(name, age, employee_id, salary)
        e_obj = e
        object.append(e)

        print("Employee Created with name",name,", age:",age,", ID:",employee_id,", and Salary:",salary)

    elif choice == 3:
         
         name = input("\nEnter your Name :")
         age = input("Enter Your Age :")
         employee_id = input("Enter Employee ID :")
         salary = float(input("Enter Salary :"))
         department = input("Enter Department :")

         m = Manager(name, age, employee_id, salary, department)
         m_obj = m
         object.append(m)

         print("Manager Created with name ",name,", age:",age,", ID:",employee_id,", Salary:",salary ,", and Department :",department)


    elif choice == 4:

        name = input("\nEnter your Name :")
        age = input("Enter Your Age :")
        employee_id = input("Enter Employee ID :")
        salary = float(input("Enter Salary :"))
        language = input("Enter Language :")

        d = Developer(name, age, employee_id, salary, language)
        d_obj = d
        object.append(d)
        
        print("Developer Created with name ",name,", age:",age,", ID:",employee_id,", Salary:",salary ,", and Programming Language :",language)


    elif choice == 5:

        print("")
        print("\nChoose Details to show")
        print("")
        print("1. Person Details")
        print("2. Employee Details")
        print("3. Manager Details")
        print("4. Developer Details")

        print("")

        choice = int(input("Enter Your Choice :"))

        if choice == 1:
            if p_obj is not None:
                p_obj.display()
            else:
                print("Not Found Person Details !!")

        elif choice == 2:
            if e_obj is not None:
                e_obj.display()
            else:
                print("Not Found Employee Details !!")

        elif choice == 3:
            if m_obj is not None:
                m_obj.display()
            else:
                print("Not Found Manager Details  !!")

        elif choice == 4:
            if d_obj is not None:
                d_obj.display()
            else:
                print("Not Found Developer Details !!")
        else:
            print("Invalid Choice !!")

    elif choice == 6:
        print("Exiting the system.All resources have been freed.")
        print("Goodbye")
        break
    else:
        print("Invalid Choice !!")

    print("\n--- Choose another operation ---")