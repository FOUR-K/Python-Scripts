# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:26:40 2017

@author: naveen84
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) ==1:
        if char == aStr[0]:
            return True
    mid = len(aStr)//2
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid+1:])
