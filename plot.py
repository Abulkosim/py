from matplotlib import pyplot as plt

x = [0, 1, 3]
y = [0, 1, 9]

plt.plot(x, y, color='blue', marker='o')

x1 = [0, 1, 3]
y1 = [-1, 1, 1]

plt.plot(x1, y1, color='red', marker='o')
plt.title('test')

plt.xlabel('x')

plt.ylabel('y')

plt.show()