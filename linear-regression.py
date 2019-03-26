import numpy as np
import matplotlib.pyplot as plt

# hyper parameters
epoch = 1000 # how many times to repeat
lr = 0.001 # learning rate
train_data_ratio = 0.8 # train data 

#read data
data = np.genfromtxt("pm2.5_normalized.txt", dtype=np.float64, skip_header=1)

data_pivot = int(len(data)*train_data_ratio)
train_data = data[:data_pivot]
test_data = data[data_pivot:]

m = len(train_data) # number of data
k = len(train_data[0]) - 1 # number of dimension on x

x_train = [list(x)[:-1] for x in train_data]
y_train = [x[-1:] for x in train_data]

x_test = [list(x)[:-1] for x in test_data]
y_test = [x[-1:] for x in test_data]

# hypothesis = w1*x1 + w2*x2 + ... + wk*xk + b
w = np.random.rand(k, 1)
b = np.random.random()

cost_log = []
for i in range(epoch):
	pred = np.matmul(x_train, w) + b
	cost =  1/(2*m) * np.sum(np.square(np.subtract(pred, y_train)))
	# cost = (h-y_train)**2.mean()/2

	if i % (epoch//100) == 0:
		print(i//(epoch//100), "%")
		cost_log.append(cost)

	w_gradient = 1/m * np.sum(np.multiply(np.subtract(pred, y_train), x_train))
	b_gradient = 1/m * np.sum(np.subtract(pred, y_train))
	
	# update
	w -= lr * w_gradient
	b -= 2 * lr * b_gradient

# visualize
if k == 1:
	f1 = plt.figure(1)
	plt.title('graph of train data')
	plt.scatter(x_train, y_train)
	pred = np.matmul(x_train, w) + b
	plt.plot(x_train, pred, color='green')
	plt.xticks(())
	plt.yticks(())
	f1.show()

f2 = plt.figure(2)
plt.title('cost')
plt.plot(range(100), cost_log)
f2.show()

# cost for test data
pred = np.matmul(x_test, w) + b
cost =  1/(2*len(test_data)) * np.sum(np.square(np.subtract(pred, y_test)))
print("average cost for test data : ", cost)

input()
