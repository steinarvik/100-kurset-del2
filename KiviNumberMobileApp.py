from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class AddApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create two text inputs with hints for guidance
        self.num1 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter first number")
        self.num2 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter second number")
        self.result_label = Label(text='Result: ', size_hint=(1, 0.4))

        # Add button with callback for addition
        self.add_button = Button(text='Add', size_hint=(1, 0.2))
        self.add_button.bind(on_press=self.add_numbers)

        # Add widgets to layout
        self.layout.add_widget(self.num1)
        self.layout.add_widget(self.num2)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.result_label)
        return self.layout

    def add_numbers(self, instance):
        # Perform addition with basic input validation
        try:
            result = float(self.num1.text) + float(self.num2.text)
            self.result_label.text = f'Result: {result}'
        except ValueError:
            self.result_label.text = "Please enter valid numbers."


# Run the application
AddApp().run()