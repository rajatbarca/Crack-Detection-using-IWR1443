import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv(r'C:\Users\DELL\Desktop\Vel_X Dataset.csv')
b=pd.read_csv(r'C:\Users\DELL\Desktop\Vel_y Dataset.csv')
c=pd.read_csv(r'C:\Users\DELL\Desktop\Vel_z Dataset.csv')
plt.plot(a,'r')
plt.plot(b,'g')
plt.plot(c,'b')
plt.title('Velocity in x,y & z axis')
plt.show()