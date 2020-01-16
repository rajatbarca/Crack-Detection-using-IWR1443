import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv(r'C:\Users\DELL\Desktop\Disp_X Dataset.csv')
b=pd.read_csv(r'C:\Users\DELL\Desktop\Disp_y Dataset.csv')
c=pd.read_csv(r'C:\Users\DELL\Desktop\Disp_z Dataset.csv')
plt.plot(a,'r')
plt.plot(b,'g')
plt.plot(c,'b')
plt.title('Displacement in x,y & z axis')
plt.show()