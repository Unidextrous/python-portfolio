from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty  # Used to link UI elements from .kv file


# Define the main widget class that connects to the .kv layout
class MyGridLayout(Widget):
    # These are linked to the TextInput widgets in the .kv file
    name = ObjectProperty(None)
    color = ObjectProperty(None)

    # Called when the Submit button is pressed
    def press(self):
        # Get text from input fields
        name = self.name.text
        color = self.color.text

        # Print a message to the console
        print(f"Hello {name}, you like {color}")

        self.name.text = ""
        self.color.text = ""

class designApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    designApp().run()