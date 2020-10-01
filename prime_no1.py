# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:26:02 2020
@author: Narendra Sharma
"""
#

# Program to Calucalte prime and print its table
#  Assumption Input Variable would be Integer
no=int(input("Please inter an Integer to Check if its prime :"))
## Divide by 2 to know till which no we want to move for division.
div=int(no/2)
## Bolean True False Taken to Check if the 
prime= False
## Here we are dividing the no from no/2 
# if the no is divisible we simple exit setting prime to false.
for i in range(2,(div+1)):
    #print(no%i)
    if no%i==0: 
        prime= False
        break
    else : prime=True
           
# If prime is True then Just Print its table
if prime:
    print(f"{no} is a Prime No and its table below")
    for i in range(1,11):
        print(f" {no} * {i} = {no * i }")
else:
    print(f"{no} is a Not a Prime No")