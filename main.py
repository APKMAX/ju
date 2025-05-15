from kivy.app import App
from kivy.uix.label import Label

class HolaMundoApp(App):
    def build(self):
        return Label(text="¡Hola mundo desde Kivy!")

if __name__ == "__main__":
    HolaMundoApp().run()