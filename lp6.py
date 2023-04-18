import matplotlib.pyplot as plt
import numpy as np

ultData = [153,153,150,146,140,131,117,97,85,80,78,75,73,70,68,66,64,62,60,58,56,54,52]
x = list()
for i in range(0, len(ultData)):
    x.append(i * 3)


plt.plot(x, ultData)
plt.title('Distance vs Time')



plt.ylabel('Distance (cm)')
plt.xlabel('Time (s)')
plt.show()

