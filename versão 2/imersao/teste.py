import numpy as np  
import matplotlib.pyplot as plt 

a = [1,2,3]
b = [3,4,6]

plt.scatter(a,b, c='blue', marker='o', label='PLS')
plt.xlabel('Mass Seed')
plt.ylabel('Wood Density')
plt.title('Mass Seed vs. Wood Density')
plt.legend()
plt.grid()
plt.show()