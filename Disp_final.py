# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:52:53 2018

@author: DELL
"""
import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv(r'C:\Users\DELL\Desktop\MPU_z Dataset.csv')
b=pd.read_csv(r'C:\Users\DELL\Desktop\Vel_z Dataset.csv')
c=pd.read_csv(r'C:\Users\DELL\Desktop\Disp_z Dataset.csv')
plt.plot(a,'r')
plt.plot(b,'g')
plt.plot(c,'b')
plt.title('Blue=disp, green=vel and red=accl for z-axis')
plt.show()