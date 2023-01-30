# apparently kivy isn't compatible with python 3.10. It'd be nice if the documentation simply stated
# that in no uncertain terms 
# I'm following the video https://youtu.be/l8Imtec4ReQ
# which is "only" 5 hours 41 minutes long
# courtesy of freeCodeCamp

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class BoxLayoutExample(BoxLayout):
    # pass
    # instead of using kivy file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # unlike in kivy file must use = here
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

