"""
CP1404/CP5632 Practical - Dynamic Labels Example
Creates Label widgets dynamically from a list of names.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app that displays a list of names using dynamic Label widgets."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Model: list of names
        self.names = ["Ada Lovelace", "Alan Turing", "Grace Hopper", "Linus Torvalds", "Guido van Rossum"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add a Label widget for each name."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
