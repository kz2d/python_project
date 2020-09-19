from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout 

Builder.load_string("""
<Button@Button>:
    background_color:[0,0,0,1]
<Main>:
    test:test
    StackLayout:
        Label:
            id:test
            halign: 'left'
            valign: 'middle'
            size_hint:2,0.25
            markup: True
            text:'kkk[u]555[/u]f'
            text_size:(self.width,self.height)
            font_size:'30sp'

        Label:
            halign: 'right'
            valign: 'middle'
            size_hint:1,0.05
            text:"kkk"
            text_size:(self.width,self.height)
            font_size:'30sp'

        GridLayout:
            size_hint:1,0.3
            cols:6
            Button:
                text:"8"
            Button:
                text:"9"
            Button:
                text:"DEL"
            Button:
                text:"AC"
            Button:
                text:"4"
            Button:
                text:"5"
            Button:
                text:"6"
            Button:
                text:":"
            Button:
                text:"1"
            Button:
                text:"2"
            Button:
                text:"3"
            Button:
                text:"+"
            Button:
                text:"-"
            Button:
                text:"0"
            Button:
                text:"."
            Button:
                text:""
            Button:
                text:"Ans"
            Button:
                text:"="

        GridLayout:
            size_hint:1,0.4
            rows:4
            Button:
                text:"7"
            Button:
                text:"8"
            Button:
                text:"9"
            Button:
                text:"DEL"
            Button:
                text:"AC"
            Button:
                text:"4"
            Button:
                text:"5"
            Button:
                text:"6"
            Button:
                text:""
            Button:
                text:":"
            Button:
                text:"1"
            Button:
                text:"2"
            Button:
                text:"3"
            Button:
                text:"+"
            Button:
                text:"-"
            Button:
                text:"0"
            Button:
                text:"."
            Button:
                text:""
            Button:
                text:"Ans"
            Button:
                text:"="
""")

class Main(BoxLayout):
    def __init__(self):
        super(Main, self).__init__()
        self.test.text='77\n[size=20]------[/size]+55556565656565656565656565\n77'