#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name={self.name}\nAge={self.age}")
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name,age)
        #super()=Person
        self.section=section
    def display(self):
        print(f"Name={self.name}\nAge={self.age}\nSection={self.section}")
        

P1=Person("walter", "25")
P1.display()

S1=Student("Pinkman", "17", "Chemistry")
S1.display()


# In[ ]:





# In[ ]:




