#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:52:20 2021

@author: juliehembeck
"""

rollNumber = [47, 64, 69, 37, 76, 83, 45, 95, 97, 46]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}


numberList = list(sampleDict.values())

NewList = list((set(rollNumber) & set(numberList)))

print(NewList)

