from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Load the corresponding .kv file for layout and styling
Builder.load_file('color.kv')

# Create a custom widget with references to input fields
class MyGridLayout(Widget):
    name = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        color = self.color.text
        print(f"Hello {name}, you like {color}")

        self.name.text = ""
        self.color.text = ""

class ColorApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    ColorApp().run()