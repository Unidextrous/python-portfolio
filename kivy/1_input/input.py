import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add top_grid to original GridLayout
        self.add_widget(self.top_grid)

        # Create submit button
        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name.text
        color = self.color.text
        self.add_widget(Label(text=f"Hello {name}, you like {color}"))

        self.name.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()