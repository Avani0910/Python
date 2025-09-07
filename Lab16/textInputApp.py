from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a TextInput widget for user input
        self.text_input = TextInput(hint_text="Type something here", font_size=24, multiline=False)

        # Create a Label to display the typed text
        self.display_label = Label(text="Your text will appear here", font_size=24, halign='center')

        # Create a Button that will update the label with the text input
        submit_button = Button(text="Display Text", font_size=24, size_hint=(1, 0.3))
        submit_button.bind(on_press=self.display_text)

        # Add widgets to the layout
        layout.add_widget(self.text_input)
        layout.add_widget(submit_button)
        layout.add_widget(self.display_label)

        return layout

    def display_text(self, instance):
        # Update the label with the text from the TextInput
        self.display_label.text = self.text_input.text

if __name__ == "__main__":
    TextInputApp().run()
