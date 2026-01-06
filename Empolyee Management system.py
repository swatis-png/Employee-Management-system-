#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Employe Management System 


# In[1]:


employees={
    101:{'name':'swati',
         'age':'19',
         'department':'google',
         'salary':'250000'}
}
         


# In[31]:


def add_employee():
    emp_id=int(input("Enter Employe ID:"))
    if emp_id in employees:
        print("Employe ID already exists")
        return
    name=input("Enter name:")
    age=int(input("Enter age:"))
    department=input("Enter department:")
    salary=int(input("Enter salary:"))
    employees[emp_id]={
        'name':name,
        'age':age,
        'department':department,
        'salary':salary,
    }
    print("Employe Added Sucessfully ")
    


# In[33]:


add_employee()


# In[101]:


def view_employee():
    if not employees:
        print("No Employees available")
    else:
        print("\nID\tname\tage\tdepartment\tsalary")
        print("-"*40)
    for emp_id, details in employees.items():
        print(emp_id,details['name'],details['age'],details['department'],details['salary'],sep="\t")
    


# In[103]:


view_employee()


# In[105]:


def search_employee():
    emp_id=int(input("Enter Employee ID to search:"))
    if emp_id in employees:
        e=employees[emp_id]
        print("\n Employee found:")
        print("Name:",e['name'])
        print("Age:",e['age'])
        print("Department:",e['department'])
        print("Salary:",e['salary'])
    else:
        print("Employee not found.")
        


# In[109]:


search_employee()


# In[115]:


while True:
    print("\n======Employee Management system =========")
    print("1. Add employee")
    print("2. View employee")
    print("3. Search employee")
    print("4. Exit")
    choice =input("Enter your choice(1-4):")
    if choice=="1":
        add_employee()
    elif choice=="2":
        view_employee()
    elif choice=="3":
        search_employee()
    elif choice=="4":
        print("Thank you for using EMS")
        break 
    else:
        print("Invalid choice!Please enter 1,2,3 or4")
        


# In[ ]:




