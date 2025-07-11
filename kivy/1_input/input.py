import kivy
from kivy.app import App
from kivy.uix.label import Label            # For text display
from kivy.uix.gridlayout import GridLayout  # For organizing widgets in rows/columns
from kivy.uix.textinput import TextInput    # For user text input
from kivy.uix.button import Button          # For interactive buttons

# Define the main layout using a GridLayout
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
    
    # Define the event handler for the button
    def press(self, instance):
        name = self.name.text
        color = self.color.text

        # Display a message with the entered info
        self.add_widget(Label(text=f"Hello {name}, you like {color}"))

        # Clear the input fields
        self.name.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()