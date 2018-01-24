# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:07:39 2018

@author: naveen84
"""

#!/bin/python3

import sys

def initialize(s):
    # This function is called once before all queries.
    arr = [1]
    for i in range(1,len(s)//2+1):
        arr.append((i*arr[i-1])%1000000007)
    
    c_count = [] 
    string = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        c_count.append(count(string[i],s))
        

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.

if __name__ == "__main__":
    s = input().strip()
    initialize(s)
    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answerQuery(l, r)
        print(result)
