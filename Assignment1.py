#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
Task 1:
# 1. Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[1]:


"Hello World"


# 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[2]:


nlist=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        nlist.append(str(i))

print(','.join(nlist))


# 3. Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[3]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


# 4. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r**3

# In[4]:


pi = 3.1415926535897931
r= 6.0  #diameter = 2*radius, Hence radius = diameter/2 i.e, 12/2 = 6 cm
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

Task 2:
# 1. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[5]:


lvalues = input("Input some comma seprated numbers : ")
list = lvalues.split(",")
tuple = tuple(list)
print('List : ',list)


# In[ ]:


2. Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


# In[1]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# 3. Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:
# Input word: AcadGild
# Output: dilGdacA

# In[7]:


rword = input("Input a word to reverse: ")

for char in range(len(rword) - 1, -1, -1):
  print(rword[char], end="")
print("\n")


# 4. Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# 
# Sample Output:
# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens
# 

# In[2]:


print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN, ! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC, \n\t\tand to secure to all its citizens")


# In[ ]:




