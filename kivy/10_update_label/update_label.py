from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('update_label.kv')

class MyLayout(Widget):
    def press(self):
        # Create variables for our widgets
        name = self.ids.name_input.text

        # Update the label
        self.ids.name_label.text = name

class UpdateLayoutApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    UpdateLayoutApp().run()