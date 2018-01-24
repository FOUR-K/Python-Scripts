# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:53:12 2017

@author: naveen84
"""

s = 'abcbcd'
maximum = 0
current_max =0
start =0
current_start =0
for i in range(len(s)):
    if i==0:
        current_start = i
        current_maximum = 1
    else:
        if s[i-1] <=s[i]:
            current_maximum +=1
        else:
            current_start = i
            current_maximum =1
    if maximum < current_maximum:
        start = current_start
        maximum = current_maximum
print("Longest substring in alphabetical order is: "+s[start:start+maximum])