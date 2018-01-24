# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:40:31 2017

@author: naveen84
"""

balance = 320000
annualInterestRate = 0.2
monthlyPayment =0
monthlyLower = balance/12.0
monthlyUpper = (balance*((1+annualInterestRate/12.0)**12))/12
#print(monthlyPayment,monthlyUpper,monthlyLower)
testBalance = balance
while round(testBalance,2) != 0.00:
    monthlyPayment = (monthlyLower + monthlyUpper)/2
    testBalance = balance
    for i in range(12):
        unpaidBalance = testBalance - monthlyPayment
        testBalance = unpaidBalance * (annualInterestRate/12) + unpaidBalance
    
    if testBalance > 0:
        monthlyLower = monthlyPayment
    elif testBalance < 0:
        monthlyUpper = monthlyPayment
    #print(monthlyPayment,monthlyUpper,monthlyLower)

print("Lowest payment:",round((monthlyPayment),2))