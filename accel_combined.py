import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv(r'C:\Users\DELL\Desktop\MPU_x Dataset.csv')
b=pd.read_csv(r'C:\Users\DELL\Desktop\MPU_y Dataset.csv')
c=pd.read_csv(r'C:\Users\DELL\Desktop\MPU_z Dataset.csv')
plt.plot(a,'r')
plt.plot(b,'g')
plt.plot(c,'b')
plt.title('Acceleration in x,y & z axis')
plt.show()