from kivy.config import Config

# Set the desired window size
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '750')

# Disable window resizing
Config.set('graphics', 'resizable', False)


from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.factory import Factory
from kivy.uix.popup import Popup


# Window.minimum_width, Window.minimum_height = Window.size
# Window.maximum_width, Window.maximum_height = Window.size
# Window.resizable = False

Builder.load_file("main.kv")
class AppScreenManager(ScreenManager):
     def __init__(self, **kwargs):
         super().__init__(**kwargs)

class FirstScreen(Screen):
    def gotoInDetails(self):
        popup = SolverChooserPopup()
        popup.open()

class SecondScreen(Screen):
    def back2Navi(self):
        self.manager.current = "navi"
        self.manager.transition.direction = "right"

    def on_enter(self, *args):
        Clock.schedule_once(self.expand_first_panel)

    def expand_first_panel(self, dt):
        # Debug: Print the children to understand the order
        # for i in range(len(self.ids.acco.children)):
        #     print(self.ids.acco.children[i])
    
        # Expand the first panel (last in the children list due to reverse order)
        self.ids.panelOne.collapse = False

    def checkboxClick(self, thecheckBox, isActive):
        print(isActive)

Builder.load_file("solverChoose.kv")
class SolverChooserPopup(Popup):
    def gotoInDetails(self):
        App.get_running_app().root.current = "inDetails"
        self.dismiss()

Builder.load_file("meshAndSimuControl.kv")
class MeshAndSimuControlLayout(GridLayout):
    def checkboxSelected(self, theCheckbox, selectedValue):
        print("{} on {}".format(theCheckbox.active, selectedValue))
    
    def spinnerClicked(self, selectedValue):
        print("{}".format(selectedValue))


class InputDeckApp(App):
    def build(self):
        
        Window.clearcolor = (252/255.0, 251/255.0, 244/255.0, 1)

        sm = AppScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())

        return sm


if __name__ == "__main__":
    InputDeckApp().run()