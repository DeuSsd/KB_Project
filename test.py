import keras as k
import random

import matplotlib.pyplot as plt
model = k.models.load_model("model.h5")

from math import sin
data_x = []
data_n = []
data_f = []


A = random.randint(-10,10)
k = random.randint(-10,10)
w = random.randint(-10,10)
A = k = w = 1
i = 10

x = -i

while x <i:
    # f = k * x + w
    f = A * sin(k * x + w)
    predict = model.predict([[A,k,w,x]])
    n1 = predict[0][0]
    data_x.append(x)
    data_f.append(f)
    data_n.append(n1)
    x+=0.5

plt.plot(data_x, data_f, color='red')
plt.plot(data_x, data_n, color='blue')
plt.title("math.sin()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()