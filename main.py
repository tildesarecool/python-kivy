# apparently kivy isn't compatible with python 3.10. It'd be nice if the documentation simply stated
# that in no uncertain terms 
# I'm following the video https://youtu.be/l8Imtec4ReQ
# which is "only" 5 hours 41 minutes long
# courtesy of freeCodeCamp
# video resources
# https://codewithjonathan.net/courses.html
# embed layouts: 39:30 min in
# anchorlayout - 41:13 mark




from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class BoxLayoutExample(BoxLayout):
    pass
    # instead of using kivy file
    # did below as example of laying out UI in py file
    # then switched back to kv file

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # unlike in kivy file must use = here
        
        self.orientation = "vertical"
        # note: buttons don't respond to layout info like 'dp' properties, only widgets do (see kv file)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

