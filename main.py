# apparently kivy isn't compatible with python 3.10. It'd be nice if the documentation simply stated
# that in no uncertain terms 
# I'm following the video https://youtu.be/l8Imtec4ReQ
# which is "only" 5 hours 41 minutes long
# courtesy of freeCodeCamp
# video resources
# https://codewithjonathan.net/courses.html
# embed layouts: 39:30 min in
# anchorlayout - 41:13 mark

# i just skipped 'page layout' and pretty much all the rest of it. 
# I couldn't really follow it anyway
# so i'm jumping to widgets - 1:09 or so


from kivy.app import App 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    #no ___init necessary
    # event on clock called via kv file
    count = 1
    my_text = StringProperty("1")
    def on_button_click(self):
        print("Button Clicked")
        self.count += 1
        self.my_text = str(self.count)
        

        """
        self.count = self.count + 1
        print(f"Button Clicked {self.count}")
        #self.my_text =  self.count
        
        Button.text=f"was clicked {self.count}"
        """
        

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


class MainWidget(Widget):
    pass
"""
class TheLabApp(App):
    pass


TheLabApp().run()

