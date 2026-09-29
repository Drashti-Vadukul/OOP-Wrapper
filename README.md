# 🏢 OOP Wrapper – Employee Management System

A Python-based console application developed to demonstrate and practice fundamental **Object-Oriented Programming (OOP)** concepts through a simple Employee Management System.

---

## 👩‍💻 Author

**Drashti Vadukul**

BCA Student | Learning Python, AI, ML & Data Science

---

## 📌 Project Overview

The **OOP Wrapper – Employee Management System** is a Python-based console application designed to demonstrate the practical implementation of **Object-Oriented Programming (OOP)** concepts.

The project represents different types of people and employees using Python classes. Users can create different objects such as:

- 👤 Person
- 👨‍💼 Employee
- 👩‍💼 Manager
- 👨‍💻 Developer

The application provides a simple **menu-driven interface** through which users can:

- Create objects
- Store multiple objects
- Display object information
- Work with different types of employees

The main purpose of this project is to understand how multiple classes can be connected using **inheritance**, how data can be protected using **encapsulation**, and how child classes can modify inherited behavior using **method overriding**.

---

# 🎯 Project Objectives

The main objective of this project is to understand and implement fundamental **Object-Oriented Programming concepts using Python**.

The project focuses on:

- Creating classes and objects
- Creating constructors
- Implementing encapsulation
- Using private attributes
- Creating getter methods
- Implementing inheritance
- Implementing multi-level inheritance
- Implementing method overriding
- Using the `super()` function
- Managing multiple objects using a list
- Taking user input
- Creating a menu-driven application
- Displaying object-specific information

This project provides a practical example of how different OOP concepts can be combined to create a small real-world application.

---

# 💡 Project Description

The **Employee Management System** represents different types of people and employees using separate Python classes.

The basic class is the `Person` class.

The `Employee` class inherits from `Person` and adds employee-specific information such as:

- Employee ID
- Salary

The `Manager` and `Developer` classes further inherit from the `Employee` class.

A `Manager` contains additional information such as:

- Department

A `Developer` contains additional information such as:

- Programming Language

This creates a clear class hierarchy and demonstrates how properties and methods can be reused through inheritance.

---

# 🏗️ Class Hierarchy

The class hierarchy of the project is:

```text
                         Person
                           |
                           |
                        Employee
                       /        \
                      /          \
                     /            \
                Manager        Developer
```

Another representation:

```text
Person
  |
  └── Employee
        |
        ├── Manager
        |
        └── Developer
```

---

# 📚 Classes Used in the Project

The project contains four main classes:

1. `Person`
2. `Employee`
3. `Manager`
4. `Developer`

---

## 1️⃣ Person Class

The `Person` class is the **base class** of the project.

It stores basic information about a person and provides common functionality that can be reused by child classes.

### Attributes

The `Person` class contains:

- `Name`
- `Age`

### Responsibilities

- Store basic personal information
- Provide common methods for displaying person details
- Act as the parent class for `Employee`

---

## 2️⃣ Employee Class

The `Employee` class inherits from the `Person` class.

It extends the functionality of `Person` by adding employee-specific information.

### Inheritance

```text
Person
   ↓
Employee
```

### Additional Attributes

The `Employee` class contains:

- Employee ID
- Salary

### Responsibilities

- Store employee information
- Reuse properties and methods from `Person`
- Add employee-specific details
- Demonstrate inheritance

---

## 3️⃣ Manager Class

The `Manager` class inherits from the `Employee` class.

It represents an employee who works as a manager.

### Inheritance

```text
Person
   ↓
Employee
   ↓
Manager
```

### Additional Attribute

The `Manager` class contains:

- Department

### Responsibilities

- Reuse information from `Person`
- Reuse employee information from `Employee`
- Add manager-specific information
- Demonstrate multi-level inheritance
- Override inherited methods when required

---

## 4️⃣ Developer Class

The `Developer` class also inherits from the `Employee` class.

It represents an employee who works as a developer.

### Inheritance

```text
Person
   ↓
Employee
   ↓
Developer
```

### Additional Attribute

The `Developer` class contains:

- Programming Language

### Responsibilities

- Reuse information from `Person`
- Reuse employee information from `Employee`
- Add developer-specific information
- Demonstrate hierarchical inheritance
- Override inherited methods when required

---

# 🔄 Inheritance

Inheritance is one of the main OOP concepts demonstrated in this project.

The project uses both **multi-level inheritance** and **hierarchical inheritance**.

### Multi-Level Inheritance

Multi-level inheritance is demonstrated through:

```text
Person
   ↓
Employee
   ↓
Manager
```

and:

```text
Person
   ↓
Employee
   ↓
Developer
```

Here:

- `Employee` inherits from `Person`
- `Manager` inherits from `Employee`
- `Developer` inherits from `Employee`

This allows child classes to reuse functionality from their parent classes.

---

# 🌳 Hierarchical Inheritance

The project also demonstrates **hierarchical inheritance**.

Both `Manager` and `Developer` inherit from the same parent class, `Employee`.

```text
              Employee
              /       \
             /         \
        Manager      Developer
```

This allows both classes to share common employee functionality while maintaining their own specialized information.

---

# 🔐 Encapsulation

The project demonstrates **encapsulation** by protecting data using private attributes.

Private attributes are represented using double underscores:

```python
self.__name
self.__age
self.__salary
```

These attributes cannot be accessed directly from outside the class in the normal way.

Instead, getter methods can be used to access the required information.

Example:

```python
def get_salary(self):
    return self.__salary
```

### Benefits of Encapsulation

- Protects internal data
- Controls access to attributes
- Improves data security
- Keeps class implementation organized
- Follows OOP best practices

---

# 🔁 Method Overriding

The project demonstrates **method overriding**.

A child class can provide its own implementation of a method that already exists in its parent class.

For example:

```text
Person
  └── display()

Employee
  └── display()

Manager
  └── display()

Developer
  └── display()
```

Each class can customize the `display()` method according to its own requirements.

This demonstrates **runtime polymorphism** and allows different objects to behave differently while using the same method name.

---

# 🧩 Use of `super()`

The project uses the Python `super()` function to reuse functionality from parent classes.

For example:

```python
super().__init__(name, age)
```

The `super()` function allows a child class to call the constructor or methods of its parent class.

### Example Concept

```text
Manager
   ↓
Employee
   ↓
Person
```

When creating a `Manager` object, `super()` can be used to initialize the inherited employee and person information without rewriting the same code.

### Benefits of `super()`

- Avoids duplicate code
- Reuses parent class functionality
- Makes inheritance easier to manage
- Improves code maintainability

---

# 📋 Object Management

The application manages multiple employee objects using a **Python list**.

Objects created through the menu can be stored in a list and later displayed.

Conceptually:

```python
employees = []
```

Objects can then be added to the list:

```python
employees.append(employee)
```

This allows the application to manage multiple objects during program execution.

---

# 🖥️ Menu-Driven Application

The project uses a **menu-driven console interface**.

The user can interact with the application through different menu options.

A typical flow is:

```text
========================================
       EMPLOYEE MANAGEMENT SYSTEM
========================================

1. Create Person
2. Create Employee
3. Create Manager
4. Create Developer
5. Display Details
6. Exit

Enter your choice:
```

The user selects an option and provides the required information.

The program then creates the appropriate object and stores it for later use.

---

# 🔄 Program Flow

The basic working flow of the application is:

```text
Start
  |
  ↓
Display Menu
  |
  ↓
Take User Choice
  |
  ├── Create Person
  |
  ├── Create Employee
  |
  ├── Create Manager
  |
  ├── Create Developer
  |
  ├── Display Objects
  |
  └── Exit
  |
  ↓
Store Objects
  |
  ↓
Display Information
  |
  ↓
Continue / Exit
```

---

# 🧠 OOP Concepts Demonstrated

| OOP Concept | Implementation in Project |
|---|---|
| Class | `Person`, `Employee`, `Manager`, `Developer` |
| Object | Objects created from each class |
| Constructor | `__init__()` |
| Encapsulation | Private attributes |
| Getter | Methods used to access private data |
| Inheritance | Child classes inherit from parent classes |
| Multi-Level Inheritance | `Person → Employee → Manager/Developer` |
| Hierarchical Inheritance | `Employee → Manager` and `Employee → Developer` |
| Method Overriding | Child classes redefine `display()` |
| Polymorphism | Same method name with different implementations |
| `super()` | Reuse parent class constructor/methods |
| List | Stores multiple employee objects |
| User Input | Accepts information through console |
| Menu-Driven Program | Allows user interaction through options |

---

# 📊 Class Relationship Overview

| Class | Inherits From | Main Information |
|---|---|---|
| `Person` | None | Name, Age |
| `Employee` | `Person` | Employee ID, Salary |
| `Manager` | `Employee` | Department |
| `Developer` | `Employee` | Programming Language |

---

# 🛠️ Technologies Used

- **Python 3**
- Object-Oriented Programming
- Python Classes & Objects
- Inheritance
- Encapsulation
- Polymorphism
- Console / Terminal Interface

---
---

# 🎓 Learning Outcomes

By completing this project, the following concepts can be understood more clearly:

- How classes and objects work in Python
- How constructors initialize object data
- How private attributes provide data protection
- How getter methods provide controlled access
- How inheritance promotes code reuse
- How multi-level inheritance works
- How hierarchical inheritance works
- How method overriding changes inherited behavior
- How `super()` connects child and parent classes
- How polymorphism works in Python
- How multiple objects can be stored and managed
- How OOP concepts can be applied to a real-world problem

---

# 🚀 Future Improvements

The project can be extended with additional features such as:

- 🔍 Search employee by ID
- ✏️ Update employee information
- 🗑️ Delete employee records
- 💾 Save employee data to a file
- 📂 Load employee data when the application starts
- 🗄️ Connect the application to a database
- 🔐 Add user authentication
- 📊 Add employee statistics
- 🖥️ Create a graphical user interface (GUI)
- 🌐 Convert the project into a web application

---

# 📌 Conclusion

The **OOP Wrapper – Employee Management System** is a practical Python project created to understand and demonstrate important **Object-Oriented Programming concepts**.

Through the `Person`, `Employee`, `Manager`, and `Developer` classes, the project demonstrates how classes can be connected using inheritance, how data can be protected using encapsulation, how child classes can override parent methods, and how `super()` can be used to reuse parent functionality.

The menu-driven interface also provides practical experience with **user input, object creation, list-based object management, and console-based application development**.

Overall, this project serves as a foundation for understanding how OOP principles can be applied to build structured and maintainable Python applications.

---

## ⭐ Key Concepts at a Glance

```text
                 OBJECT-ORIENTED PROGRAMMING
                              |
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    Encapsulation         Inheritance          Polymorphism
        │                     │                     │
 Private Attributes      Person → Employee      Method Overriding
 Getter Methods          Employee → Manager     display()
                         Employee → Developer
                              │
                           super()
```

---

## 👩‍💻 Author

**Drashti Vadukul**

BCA Student | Learning Python, AI, ML & Data Science

---

