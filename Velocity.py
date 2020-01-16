# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:18:13 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
y=pd.read_csv(r'C:\Users\DELL\Desktop\Good.csv')
arr=np.array(y)
print(arr)
init_accel=arr[0:1]
init_vel=0
print("Initial acceleration",init_accel)
i=1
while i<len(arr):
    vel=init_vel+(0.5*(arr[i-1]+arr[i]))
    print (vel)
    i+=1
    init_vel=vel

