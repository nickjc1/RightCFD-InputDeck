from kivy.config import Config
# Set the desired window size
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '750')
# Disable window resizing
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.core.window import Window

from screens import AppScreenManager, StartUpScreen 

startUpScreen= StartUpScreen()

class InputDeckApp(App):
    def build(self):
        
        Window.clearcolor = (252/255.0, 251/255.0, 244/255.0, 1)

        sm = AppScreenManager()

        sm.add_widget(startUpScreen)

        return sm


if __name__ == "__main__":
    InputDeckApp().run()