from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.counter = 0  # Initialize counter

        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a label to display the counter
        self.label = Label(text=f"Counter: {self.counter}", font_size=40, halign='center')

        # Create a button that increments the counter
        button = Button(text="Increment", font_size=30, size_hint=(1, 0.3))
        button.bind(on_press=self.increment_counter)

        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"

if __name__ == "__main__":
    CounterApp().run()
