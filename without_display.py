import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# hyper parameters
epoch = 1000 # how many times to repeat
lr = 0.005 # learning rate

#read data
data = np.genfromtxt("fire_and_theft.txt", names=('fire','theft'), dtype=np.float64, skip_header=1)

m = len(data) # number of data
k = len(data[0]) - 1 # number of attributes on x

x_values = [list(x)[:-1] for x in data]
y_values = [[x[-1]] for x in data]

# hypothesis = w1*x1 + w2*x2 + ... + wk*xk + b
w = np.random.rand(1, k)
b = np.random.random()

cost_log = []
for _ in range(epoch):
	pred = np.matmul(x_values, w) + b
	cost =  1/(2*m) * np.sum(np.square(np.subtract(pred, y_values)))
	# cost = (h-y_values)**2.mean()/2
	cost_log.append(cost)

	w_gradient = 1/m * np.sum(np.multiply(np.subtract(pred, y_values), x_values))
	b_gradient = 1/m * np.sum(np.subtract(pred, y_values))
	
	# update
	w -= lr * w_gradient
	b -= 2 * lr * b_gradient

result = np.matmul(x_values, w) + b

plt.figure()
plt.title('graph')
plt.scatter(x_values, y_values)
plt.plot(x_values, result, color='green')
plt.savefig('graph.png')

plt.figure()
plt.title('cost')
plt.plot(range(epoch), cost_log)
plt.savefig('cost.png')

input()
