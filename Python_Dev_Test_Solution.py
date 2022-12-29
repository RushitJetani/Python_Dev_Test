#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1. Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. 
#Square each element of the list in one by one fashion and print them. 
#After the end of the iteration, print - "The sequence has ended".
A=[1,2,3,4,5,6]
for i in A:
     print(i*i)
print("The sequence has ended")


# In[2]:


"""Question 2. If choice of user = 2, print the pattern - > 

* * * * *
 * * * *
  * * *
   * *
    *                       
   _ _
  _ _ _
 _ _ _ _
_ _ _ _ _

If choice of user = 1, print the pattern - > 

* * * * *
 * * * *
  * * *
   * *
    * 

If choice of the user = any_other_choice_other_than_1_and_2, print the message - >

'Invalid Input'
"""

a=input('Enter Your Choice: ')

if a == '2':
    rows = 5
    i = 0
    while i <= rows - 1:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1:
            print('*', end=' ')
            k += 1
        print()
        i += 1

    i = rows - 2
    while i >= 0:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1:
            print('_', end=' ')
            k += 1
        print('')
        i -= 1
    
elif a == '1':
    rows = 5
    i = 0
    while i <= rows - 1:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1:
            print('*', end=' ')
            k += 1
        print()
        i += 1

else:
    print('Invalid Input')


# In[3]:


#Question 3. Create a tuple t_1 = (1, 4, 9, 16, 25, 36). Square each element of the tuple using tuple comprehension 
#and store the result in a variable known as t_modified. Find element at index position 4 of the tuple t_modified. 
#Now slice the modified tuple in such a way that the sliced  tuple includes only elements from index position 1 to 3 
#and store this sliced tuple in a variable known as t_sliced. 

t_1=(1, 4, 9, 16, 25, 36)
print('t_1:', t_1)
t_modified=tuple(x**2 for x in t_1)
print('t_modified:', t_modified)
print('Element at index position 4 of t_modified:',t_modified[4])
t_sliced=t_modified[1:4]
print('t_sliced:',t_sliced)


# In[4]:


#Question 4. Show by raising an error how tuples are immutable and also define what exactly immutability is in your own words.
tuple=(10, 20, 30, 40)
tuple[1]=100

'''
Tuple is immutable:
As the tuple is immutable, we cannot change the elements after they are created; they are fixed once created.
'''


# In[5]:


'''Question 5. 
Create a frozenset named frozen_set_1 containing the elements: 'A', 'B', 'C' and 'D' and combine it using union 
with a frozenset named frozen_set_2 containing elements 'A', 2, 'C' and 4. The final combined frozenset must be 
named frozenset_union. Now find the common elements in frozen_set_1 and frozen_set_2 and store the result in 
a variable named frozenset_common. Lastly, in a new forzenset named forzenset_difference store the elements of 
frozen_set_1 which are not in frozen_set_2 and in a new frozenset named frozenset_distinct store the elements 
which are unique to frozen_set_1 and frozen_set_2.'''

a=('A', 'B', 'C', 'D')
frozen_set_1 = frozenset(a)
print('frozen_set_1:',frozen_set_1)
b=('A', 2, 'C', 4)
frozen_set_2 = frozenset(b)
print('frozen_set_2:',frozen_set_2)
frozenset_union= frozen_set_1.union(frozen_set_2)
print('frozenset_union:',frozenset_union)
frozenset_common= frozen_set_1.intersection(frozen_set_2)
print('frozenset_common:',frozenset_common)
frozenset_difference= frozen_set_1.difference(frozen_set_2)
print('frozenset_difference:',frozenset_difference)
frozenset_distinct= frozen_set_1.symmetric_difference(frozen_set_2)
print('frozenset_distinct:',frozenset_distinct)


# In[6]:


'''Question 6. 
Write a python program to remove items in a list containing the character 'a' or 'A'. Use lambda function for it. 
For this program pass in as argument the list: list_a = ["car", "place", "tree", "under", "grass", "price"] 
to the lambda function named remove_items_containing_a_or_A.'''

list_a = ["car", "place", "tree", "under", "grass", "price"]
remove_items_containing_a_or_A = list(filter(lambda x: ((x.find('a') or x.find('A')) == -1), list_a))
print(remove_items_containing_a_or_A)


# In[7]:


#Question 7: 
#Create a custom exception class which can handle "IndexError" as well as "ValueError" such that it can display 
#its own custom error message when we use index which is not valid in a list. Take list as list_a = [1, 2, 3, 4, 5].

try:  
    list_a = [1, 2, 3, 4, 5]  
    a=int(input('Enter the index='))
    print(list_a[a])
except LookupError:  
    print ('The index ' + str(a) + ' is incorrect and index should lie between -5 and 4.')
except ValueError:
    print ('Use an Integer value as the input.')

