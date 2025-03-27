"""
Kivy GUI program to convert miles to kilometres.
Handles invalid inputs and auto-updates output on text change or button press.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = "Your Name"

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """App for converting miles to kilometres."""
    result_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy GUI from .kv file."""
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        """Convert miles to km and update the label."""
        self.result_text = str(self.convert_to_km(text))

    def handle_increment(self, text, change):
        """Increase or decrease the value in the input box and update result."""
        try:
            value = int(text)
        except ValueError:
            value = 0
        value += change
        self.root.ids.input_miles.text = str(value)
        self.result_text = str(self.convert_to_km(str(value)))

    def convert_to_km(self, miles_text):
        """Convert miles to kilometres, safely."""
        try:
            miles = float(miles_text)
            return round(miles * MILES_TO_KM, 5)
        except ValueError:
            return 0.0

MilesConverterApp().run()
