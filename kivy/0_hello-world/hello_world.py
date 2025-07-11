# Import the core Kivy framework

import kivy
from kivy.app import App            # App is the base class for Kivy applications
from kivy.uix.label import Label    # Label is a simple UI widget for displaying text

# Define the main application class
class MyApp(App):
    def build(self):
        # The build() method returns the root widget of the UI
        # Here, we return a Label widget with custom text and font size
        return Label(text="Hello, World!", font_size=72)

# Standard Python boilerplate to run the app
if __name__ == "__main__":
    MyApp().run()   # Launch the application loop