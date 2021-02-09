
# import numpy as np
#
# input_data = np.array([0.3, 0.7, 0.9])
# output_data = np.array([0.5, 0.9, 1.0])
#
# model = k.Sequential()
#
# model.add(k.layers.Dense(units = 1, activation="linear"))
# model.compile(loss ="mse",optimizer="sgd")
# fit_results = model.fit(x=input_data,y=output_data, epochs= 100)
#
# predicted = model.predict(([0.5]))
# print(predicted)
#

import keras as k
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

n = 1
sum = 100
d = 6
while sum > 0.5:

    data_frame = pd.read_csv("data.csv")
    # data_frame = data_frame[:d*400]

    columns = data_frame.shape[0]


    from sklearn.utils import shuffle

    data_frame = shuffle(data_frame)

    input_names = ["k","w","x"]
    # input_names = ["x"]

    output_names = ["f"]




    def dataframe_to_dict(df):
        result = dict()
        for column in df.columns:
            values = df[column]
            result[column] = values
        return result


    def make_supervised(df):
        raw_in_data = df[input_names]
        raw_out_data = df[output_names]
        return  {"in": dataframe_to_dict(raw_in_data),
                 "out": dataframe_to_dict(raw_out_data)}

    def encode(data):
        vectors = []
        for data_name, data_values in data.items():
            vectors.append(list(data_values))

        formatted = []

        for vector_raw in list(zip(*vectors)):
            formatted.append(list(vector_raw))

        return formatted



    supervised = make_supervised(data_frame)
    in_data = np.array(encode(supervised["in"]))
    out_data = np.array(encode(supervised["out"]))

    print(round(columns*0.8))

    train_x = in_data[:round(columns*0.8)]
    train_y = out_data[:round(columns*0.8)]

    test_x = in_data[round(columns*0.8):]
    test_y = out_data[round(columns*0.8):]

    model = k.Sequential()
    print("==========",3,n,n,1,"====")
    model.add(k.layers.Dense(units = 3, activation = None))
    model.add(k.layers.Dense(units = n, activation= "relu"))
    model.add(k.layers.Dense(units = n, activation= "relu"))
    model.add(k.layers.Dense(units = 1, activation = None))


    opt = k.optimizers.Adam(learning_rate=0.01)
    model.compile(loss='MSE', optimizer=opt, metrics="accuracy")

    epochs = 100
    early_stopping_patience = 10
    # Add early stopping
    early_stopping = k.callbacks.EarlyStopping(
        monitor="val_loss", patience=early_stopping_patience, restore_best_weights=True
    )


    callback = k.callbacks.EarlyStopping(
        monitor='loss', patience=3, restore_best_weights=True, min_delta= 0.01
    )


    fit_results = model.fit(
        x=train_x,
        y=train_y,
        epochs= epochs,
        validation_split=0.2,
        callbacks=[early_stopping,callback],
    )
    model.save("model.h5")


    model = k.models.load_model("model.h5")
    # plt.title("train/validation")
    # plt.plot(fit_results.history["accuracy"],label = "Train")
    # plt.plot(fit_results.history["val_accuracy"], label = "Validation")
    # plt.legend()
    # plt.show()
    predict = model.predict(test_x)


    sum = 0
    for item in range(len(predict)):
        el1 =   abs(predict[item][0])
        el2 = abs((test_x[item][-1]))
        delta = abs( el1 - el2)
        sum += delta
        # print(delta)

    print()
    eps = sum/len(predict)
    print(sum,eps )
    n+=1
#
#
# plt.title("loss/validation")
# plt.plot(fit_results.history["loss"],label = "Train")
# plt.plot(fit_results.history["val_loss"], label = "Validation")
# plt.legend()
# plt.show()