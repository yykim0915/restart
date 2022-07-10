import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib  import font_manager, rc

font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

fruits = ['apple', 'abocado', 'melon', 'kewi', 'wotermelon']
quan= [10,20,30,40,50]

#plt.figure(figsize=(80, 80))  #생략가능
plt.bar(fruits, quan)
plt.plot(fruits, quan, color='orange', marker='o', label='과일수량')
#plt.title('fruits graph')
plt.xlabel('품목이름')
plt.ylabel('금액')
plt.legend(loc='upper right') #범례표시

for k in range(len(quan)):
    value = quan[k]
    print(value)
    plt.text(fruits[k], value+0.7, value, ha='center', va='bottom', size=14)

plt.savefig('./data/graph_fruits.png')
plt.grid(True)
plt.show()
print()
