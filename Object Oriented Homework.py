#!/usr/bin/env python
# coding: utf-8

# In[19]:


#create a class Line that holds methods to calculate the slope and the distance between two points of a line

class Line():
    
    #constructor
    def __init__(self,cord1,cord2):
        self.x1,self.y1=cord1
        self.x2,self.y2=cord2
        
    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
        
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)
        
c1=(5,8)
c2=(6,10)
point1=Line(c1,c2)
point1.slope()
point1.distance()


    


# In[ ]:





# In[11]:


#create a class Cylinder and calculate the surface area and volme of it
class Cylinder():
    def __init__(self,radius,height):
        self.r=radius
        self.ht=height
    
    def surface_area(self):
        return (2*3.14*self.r*self.ht)
    
    def volume(self):
        return (3.14*pow(self.r,2)*self.ht)
    
c1=Cylinder(3,4)
c1.surface_area()


# In[12]:


c1.volume()


# In[31]:


#create a class Account that performs withdrawl and deposit functions

class Account():
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    def withdrawl(self):
        withdrawl_amt=int(input('Enter the amount to be withdrawed'))
        if self.balance>withdrawl_amt:
            print('Proceed with the withdrawl process')
            self.balance=self.balance-withdrawl_amt
            print(f'balance left after withdrawl: :{self.balance} ') 
    
    def deposit(self):
        deposit_amt=int(input('Enter the amt to be deposited'))
        print("Deposit Process Initiated!! ")
        self.balance=self.balance+deposit_amt
        print(f'Total balance after deposit is :{self.balance} ')
        
    def __str__(self):
        return f"Owner:{self.owner} \nBalance:{self.balance}"
a1=Account('Preeti',60000)


# In[34]:


print(a1)


# In[33]:


a1.deposit()


# In[35]:


a1.withdrawl()


# In[ ]:




