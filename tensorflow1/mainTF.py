import tensorflow as tf
import tensorflow.keras as keras
import os
import numpy as np

a=np.load('my_mnist_1.1.npy')
mnist=keras.datasets.mnist

(train, label_train),(test, label_test)=mnist.load_data()
train,test=train[:14000]/255,test[:2000]/255
label_train,label_test=label_train[:14000],label_test[:2000]
train,test=np.concatenate((train,a[:1400])),np.concatenate((test,a[1400:1600]))
label_train,label_test=np.concatenate((label_train,(np.zeros((1400))+10))),np.concatenate((label_test,(np.zeros((200))+10)))
print(train.shape, test.shape, label_train.shape, label_test.shape)

def build():
    model=keras.models.Sequential([
        keras.layers.Flatten(input_shape = (28,28)),
        keras.layers.Dense(128, activation = 'relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense ( 20 , activation = 'relu' ) ,
        keras.layers.Dense(11, activation = 'softmax')
    ])

    model.compile(optimizer = 'adam',
                  loss='sparse_categorical_crossentropy',
                  metrics = ['accuracy'],
                  )
    return model

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname ( checkpoint_path )

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint ( filepath = checkpoint_path ,
                                                   save_weights_only = True ,
                                                   verbose = 1 ,)

model=build()
model.fit(train,label_train, epochs =30, callbacks = [cp_callback])
print(model.evaluate(test, label_test))
# model=build()
# print(model.evaluate(test, label_test))
# model.load_weights(checkpoint_path)
#
# print(model.evaluate(test, label_test))
























# a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# a[0]=np.load('my_mnist.npy')
# print(a[0].shape)
#
# for i in range(1,4):
#     a[i]=np.zeros((100,28,28))
#     for d in range(100):
#         a[i][d]=np.rot90(a[i-1][d])
#
# for i in range(4,8):
#     a[i] = np.zeros ( (100 , 28 , 28) )
#     for d in range ( 100 ):
#         a[i][d]=np.flipud(a[i-4][d])
#
# for i in range(8,16):
#     a[i] = np.zeros ( (100 , 28 , 28) )
#     for d in range ( 100 ):
#         a[i][d]=a[i][d]*(-1)+1
#
# f=a[0]
# for i in range(1,16):
#     print(a[i].shape)
#     f=np.concatenate((f,a[i]), axis = 0)
#
# print(f.shape)
# np.save('my_mnist_1.1',f)