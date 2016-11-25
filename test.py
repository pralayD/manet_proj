from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

x2 = [2,4]
y2 = [7,8]

plt.plot(x,y,label = 'First line')
plt.plot(x2,y2, label = 'Second line')

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show() 