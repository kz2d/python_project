from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.config import Config
import numpy as np

import tensorflow as tf
import tensorflow.keras as keras
import os

a=np.load('my_mnist_1.1.npy')
mnist=keras.datasets.mnist

(train, label_train),(test, label_test)=mnist.load_data()
train,test=train[:14000]/255,test[:2000]/255
label_train,label_test=label_train[:14000],label_test[:2000]
train,test=np.concatenate((train,a[:1400])),np.concatenate((test,a[1400:1600]))
label_train,label_test=np.concatenate((label_train,(np.zeros((1400))+10))),np.concatenate((label_test,(np.zeros((200))+10)))

def build():
    model=keras.models.Sequential([
        keras.layers.Flatten(input_shape = (28,28)),
        keras.layers.Dense(128, activation = 'relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense ( 20 , activation = 'relu' ),
        keras.layers.Dense(11, activation = 'softmax')
    ])

    model.compile(optimizer = 'adam',
                  loss='sparse_categorical_crossentropy',
                  metrics = ['accuracy'])
    return model

# checkpoint_path='training_1\cp.ckpt'
# checkpoint_dir = os.path.dirname ( checkpoint_path )
model=build()
model.fit(train,label_train, epochs =10)#epoch=5


g=28
g1=28
main=np.zeros((g,g1))
print(np.expand_dims(main,0).shape)

Config.set('graphics', 'height',20*g)
Config.set('graphics', 'width', 20*g1+80)



a=20
b=20


class MyPaintWidget(Widget):

    def __init__(self, **kwargs):
        super(MyPaintWidget,self).__init__(**kwargs)
        with self.canvas:
            pass

    def on_touch_down(self, touch):
        global a, b, main,g,g1
        print(touch.x,touch.y)
        s=int(touch.x/a)
        s1=int(touch.y/b)
        self.Draw(s,s1)


    def on_touch_move(self, touch):
        global a, b, main,g,g1
        
        s=int(touch.x/a)
        s1=int(touch.y/b)
        if(s>(g-1)):
            return
        self.Draw(s,s1)

    def Draw(self,s,s1):
        global a, b, main,g,g1
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(pos=(a*s, s1*b), size=(a, b))
            main[g1-1-s1,s]=1
            if(s1!=0):
                v=main[g1-s1,s]
                v+=0.2
                if(v>1):
                    v=1
                main[g1-s1,s]=v
                Color(v,v,0)
                Rectangle ( pos = ( a * s ,(s1-1) * b) , size = (a , b) )
            if (s1!=(g1-1)):
                v = main[g1 -2 - s1 , s]
                v += 0.2
                if (v > 1):
                    v = 1
                main[g1-2 - s1 , s] = v
                Color ( v , v , 0 )
                Rectangle ( pos = ( a * s , (s1 + 1) * b) , size = (a , b) )
            if (s!=0):
                v = main[g1 - 1 - s1 , s-1]
                v += 0.2
                if (v > 1):
                    v = 1
                main[g1 - 1 - s1 , s-1] = v
                Color ( v , v , 0 )
                Rectangle ( pos = ( a * (s-1) , (s1) * b) , size = (a , b) )
            if (s!=(g-1)):
                v = main[g1 - 1 - s1 , s+1]
                v += 0.2
                if (v > 1):
                    v = 1
                main[g1 - 1 - s1 , s+1] = v
                Color ( v , v , 0 )
                Rectangle ( pos = (a * (s+1) ,(s1) * b) , size = (a , b) )
            gg=model.predict(np.expand_dims(main,0))
            print(np.argmax(gg[0]))

class MyPaintApp(App):

    def build(self):
        pin=BoxLayout()
        self.painter = MyPaintWidget(size_hint=(0.875,1))
        clearbtn = Button(text='Clear', size_hint=(0.125,1))
        clearbtn.bind(on_release=self.clear_canvas)
        
        pin.add_widget(self.painter)
        pin.add_widget(clearbtn)
        return pin

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        global main, g, g1
        main=np.zeros((g,g1))


if __name__ == '__main__':
    MyPaintApp().run()