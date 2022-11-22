"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to km."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field or press UP/DOWN"
        return self.root

    def handle_calculate(self):
        """To handle calculation and output result."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str("%.3f" % result)

    def handle_increment(self, change):
        """To handle up/down button press and update new value."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """To get a valid input from text entry widget."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
