# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:50:57 2017

@author: naveen84
"""
from math import *
def polysum(n,s):
    """
    Input: n, a positive integer
           s, a positive int or float
    returns float upto 4 decimal places
    """
    def polyArea(n,s):
        """
        returns area of polygon
        """
        return (0.25*n*s**2)/(tan(pi/n))
    def polyPerimeter(n,s):
        """
        returns perimeter of polygon
        """
        return n*s
    return round((polyArea(n,s) + polyPerimeter(n,s)**2),4)
