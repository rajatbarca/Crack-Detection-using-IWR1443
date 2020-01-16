# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:08:30 2018

@author: DELL
"""
import pandas as pd
import numpy as np

z=pd.read_csv(r'C:\Users\DELL\Desktop\Vel_z Dataset.csv')
ar=np.array(z)
init_disp1=ar[0:1]
init_disp=0
print("Initial displacement",init_disp1)
i=1
while i<len(ar):
    disp=init_disp+(0.5*(ar[i-1]+ar[i]))
    print (disp)
    i+=1
    init_disp=disp