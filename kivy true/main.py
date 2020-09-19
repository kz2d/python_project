from kivy.app import App
from main2 import Main
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.vector import Vector
from kivy.config import Config
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 300)

    

class PongApp(App):
    def build(self):
        game = Main()
        return game


if __name__ == '__main__':
    PongApp().run()