#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class School:
    students= []
    def __init__(self,capacity):
        self.capacity=capacity
        
    def add_student(self,student):
        if len(self.students)<self.capacity:
            self.students.append(student)
        else:
            print(f'You can not register {student.name} as capacity is full')
            
    def print_students(self):
        for i in self.students:
            print(i)
        
class Student:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return f'name is {self.name} age is {self.age} and gender is {self.gender}'

school1=School(2)
student_1=Student('Johan',34, 'male')
student_2=Student('Heaven', 31, 'female')
student_3=Student('Pearl', 21, 'female')

school1.add_student(student_1)
school1.add_student(student_2)

school1.print_students()
school1.add_student(student_3)

print(school1.__dict__)
print(student_1.__dict__)
print(student_2.__dict__)
print(student_3.__dict__)



        


# In[ ]:





# In[ ]:




