#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
list=[]
for n in range (1500,2700):
    if (n%7==0) and (n%5==0):
        list.append(str(n))
print(list)


# In[3]:


#2

opreation=input("Enter the degree you want to convert from : ")


last_char =opreation[-1]


#to check if the user write letter C OR F at end of degree that he or her want to converted from
if last_char !='C'and last_char !='F':
    print("please enter the degree in this way 50F , 50C,""30F""....etc")


if last_char=='C':
    print("degree in fahrenheit : ",1.8*int(''.join(filter(str.isdigit, opreation)))+32)
  
    
if last_char=='F':
        print("degree in  celsius : ",1.8*int(''.join(filter(str.isdigit, opreation)))+32)


 


# In[4]:


#3
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[5]:


#4
def reverse(string):
	string = "".join(reversed(string))
	return string

word=input("Enter a word: ")

print("The reversed string is : ")
print(reverse(word))


# In[8]:


#5

def find_max(n1,n2,n3):
    max=0
    if n1>max:
        max=n1
    if n2>max:
        max=n2
    if n3>max:
        max=n3
    return max




print("The largest number is : ",find_max(5,-3,-12))


# In[10]:


#6

def sum_of_list(list):
  total = 0
  for value in list:
    total = total + value
  return total

my_list = [1,3,5,2,4]
print (("The sum of the list is: "), sum_of_list(my_list))


# In[11]:


#7

for i in range(6):
     if (i == 3 or i==6):
           continue
     print(i)


# In[12]:


#8
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(fact(n))


# In[13]:


#9
def unique_list(numbers):
   return list(set(numbers))


num=[1,3,5,2,1,1,3,4,2]
print(unique_list(num))


# In[ ]:


#10
addition = lambda a: a+15
print(addition(25))
multiply=lambda a,b:a*b
print(multiply(3,4))

