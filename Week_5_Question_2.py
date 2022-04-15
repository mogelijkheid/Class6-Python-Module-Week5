#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        self.area=self.length * self.width
        return self.area
    def perimeter(self):
        self.perimeter=2 * self.length + 2 * self.width
        return  self.perimeter
    def display(self):
        print("length :{}, width: {}, area :{} and perimeter:{}".format(self.length,self.width,self.area,self.perimeter))
    
class Parallelepipede(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length, width)
        #super()=Rectangle
        self.height=height
    def volume(self):
        self.volume=self.length * self.width * self.height
        return self.volume
    def display(self):
        print("volume: {}".format(self.volume))


# In[ ]:




