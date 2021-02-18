#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:52:50 2021

@author: juliehembeck
"""

#function counts the number of vowels in the word input

def count_vowels(x):
     vowels = 0
     for i in range(len(x)):
        # print(x[i])
         if x[i] == 'a' or x[i] == 'e' or x[i] == 'i'or x[i] == 'o'or x[i] == 'u':
             vowels += 1
     return vowels
         
print(count_vowels('supercalifragilisticexpialidocious'))