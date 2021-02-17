# Python program showing
# Graphical representation of
# sin() function
from math import sin
import matplotlib.pyplot as plt

import csv
import random
in_data = []
out_data = []

data = []
data.append(["A","k","w","x","f"])

def fun(A=1,k=1,w=0):
    x = -10

    while x<10:
        in_data.append(x)
        f = k*x+w
        # f = A*sin(k*x+w)
        # f = x*x*A+ x*k +w
        out_data.append(f)
        data.append([A,k,w,x,f])
        x+=1

# i = 10
# while i > 0:
#     fun(1,0.5,0)
#     i-= 1

# param = [[random.randint(-10,10),random.randint(-10,10),random.randint(-10, 10)] for i in range(100)]
param = [[1,1,1] for i in range(100)]
for item in param:
    fun(*item)

csv_file = open('data.csv', 'w')
with csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
    print("Done")

plt.plot(in_data, out_data, color='red')
plt.title("math.sin()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

