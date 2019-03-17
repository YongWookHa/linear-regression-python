import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# hyper-parameters
epoch = 20
lr = 0.001

# read data
data = np.genfromtxt("fire_and_theft.txt", names=('fire', 'theft'), skip_header=1, dtype=np.float)
k = len(data[0]) - 1
m = len(data)
x_values = [list(x)[:-1] for x in data]
y_values = [[x[-1]] for x in data]

print("x_values : ", np.shape(x_values))
print("y_values : ", np.shape(y_values))

# z = w*x + b
w = np.random.rand(1,k+1)
x_original = x_values
x_values = np.transpose([x + [1,] for x in x_values]) # for using bias, we place new column of ones to x_values

cost_log = []

for _ in range(epoch):
    # cost calculating
    z = np.matmul(w, x_values)
    h = z # apply sigmoid later
    temp = 1/m * np.sum(np.subtract(h, y_values))
    e = 1/(2*m) * np.sum(np.square(np.subtract(h, y_values)))
    cost_log.append(e)
    
    # weight updating  
    for i in range(k+1):
        d_e = temp * w[0][i]
        w[0][i] -= lr * d_e
        
plt.figure()
plt.plot(range(epoch), cost_log)
plt.savefig('cost.png')

plt.figure()
plt.scatter(x_original, y_values,  color='black')
plt.plot(x_original, np.transpose(np.matmul(w, x_values)), color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.savefig('graph.png')