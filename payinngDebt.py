# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:40:31 2017

@author: naveen84
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(12):
    unpaidBalance = balance - (balance*monthlyPaymentRate)
    balance = unpaidBalance * (annualInterestRate/12) + unpaidBalance
print("Remaining balance:",round(balance,2))