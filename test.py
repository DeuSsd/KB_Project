import keras as k
model = k.models.load_model("model.h5")

test = [10,0,0]#k w x
#f = k*x+w
f = test[0]*test[2]+test[1]
predict = model.predict([test])
print(f,predict[0][0])