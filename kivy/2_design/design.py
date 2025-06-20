from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        color = self.color.text
        print(f"Hello {name}, you like {color}")

        self.name.text = ""
        self.color.text = ""

class designApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    designApp().run()