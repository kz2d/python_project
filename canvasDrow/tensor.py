from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.config import Config
import numpy as np

g=28
g1=28

main=np.zeros((100,g,g1))
print(main.shape)
i=0

Config.set('graphics', 'height',g*20)
Config.set('graphics', 'width', g1*20+80)

a=20
b=20

class MyPaintWidget(Widget):

    def __init__(self, **kwargs):
        super(MyPaintWidget,self).__init__(**kwargs)
        with self.canvas:
            pass

    def on_touch_down(self, touch):
        global a, b, main,g,g1
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
        global a, b, main,g,g1,i
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(pos=(a*s,s1*b), size=(a, b))
            main[i,g1-1-s1,s]=1
            if(s1!=0):
                v=main[i,g1-s1,s]
                v+=0.2
                if(v>1):
                    v=1
                main[i,g1-s1,s]=v
                Color(v,v,0)
                Rectangle ( pos = (a * s , (s1-1) * b) , size = (a , b) )
            if (s1!=(g1-1)):
                v = main[i,g1 -2 - s1 , s]
                v += 0.2
                if (v > 1):
                    v = 1
                main[i,g1-2 - s1 , s] = v
                Color ( v , v , 0 )
                Rectangle ( pos = (a * s ,(s1 + 1) * b) , size = (a , b) )
            if (s!=0):
                v = main[i,g1 - 1 - s1 , s-1]
                v += 0.2
                if (v > 1):
                    v = 1
                main[i,g1 - 1 - s1 , s-1] = v
                Color ( v , v , 0 )
                Rectangle ( pos = ( a * (s-1) , (s1) * b) , size = (a , b) )
            if (s!=(g-1)):
                v = main[i,g1 - 1 - s1 , s+1]
                v += 0.2
                if (v > 1):
                    v = 1
                main[i,g1 - 1 - s1 , s+1] = v
                Color ( v , v , 0 )
                Rectangle ( pos = (a * (s+1) , (s1) * b) , size = (a , b) )

class MyPaintApp(App):

    def build(self):
        pin=BoxLayout()
        self.painter = MyPaintWidget(size_hint=(0.875,1))
        clearbtn = Button(text='Clear', size_hint=(0.125,1))
        clearbtn.bind(on_release=self.clear)
        
        pin.add_widget(self.painter)
        pin.add_widget(clearbtn)
        return pin

    def clear(self, obj):
        global main, g, g1, i
        self.painter.canvas.clear()
        i+=1
        if(i==100):
            np.save('my_mnist',main)

if __name__ == '__main__':
    MyPaintApp().run()