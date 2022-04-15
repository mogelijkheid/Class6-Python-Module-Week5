#!/usr/bin/env python
# coding: utf-8

# In[11]:


class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def deposit(self,d ):
        self.balance = self.balance + d
    
    def withdrawal(self,w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
            
    def bankFees(self):
        self.balance = (95/100)*self.balance
      
    def display(self):
        print("Account Number : {}, Account Name : {} , Account Balance : {}"
              .format (self.accountNumber,self.name, self.balance))
    

