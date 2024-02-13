import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.label = Label(text = "Color here")

        layout.add_widget(self.label)
        layout.add_widget(Button(text = "red", on_press=self.on_click, background_color="#FF0000"))
        layout.add_widget(Button(text = "orange", on_press=self.on_click, background_color="#FF6347"))
        layout.add_widget(Button(text = "yellow", on_press=self.on_click, background_color="#FFFF00"))
        layout.add_widget(Button(text = "green", on_press=self.on_click, background_color="#00FF00"))
        layout.add_widget(Button(text = "cyan", on_press=self.on_click, background_color="#00FFFF"))
        layout.add_widget(Button(text = "dodger blue", on_press=self.on_click, background_color="#1E90FF"))
        layout.add_widget(Button(text = "fuchsia", on_press=self.on_click, background_color="#FF00FF"))

        return layout

    def on_click(self, sender):
        self.label.text = sender.text


if __name__ == "__main__":
    app = MainApp()
    app.run()