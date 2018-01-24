# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:53:53 2017

@author: naveen84
"""

s = "azcbobobegghakl"
count = 0
n = 0
while n< len(s)-2:
    if s[n]=='b' and s[n+1]=='o' and s[n+2] =='b':
        count += 1
    n += 1
print(count)