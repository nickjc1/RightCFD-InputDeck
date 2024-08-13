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

from inDataDict import entryDataDict # The File contains global variable entryDataDict
from inFileManagement import InFileManagementPopupWindow # The File contains popup window, which is used to  save data to local disk, functionality


Builder.load_file("main.kv")
class AppScreenManager(ScreenManager):
     def __init__(self, **kwargs):
         super().__init__(**kwargs)

class FirstScreen(Screen):
    def createNewInFile(self):
        popup = SolverChooserPopup()
        popup.open()
    
    def importExistingInFile(self):
        popup = InFileManagementPopupWindow()

        # A widget can only be removed from its parent widget.
        # So in order to remove inPathTextInput, we need to find out its parent widget.
        # Then remove the textinput from its parent
        inPathTextInputParent = popup.ids.inPathTextInput.parent
        inPathTextInputParent.remove_widget(popup.ids.inPathTextInput)

        popup.ids.leftButton.text = "Import"
        popup.ids.inFileChooser.filters = []

        popup.open()

class SecondScreen(Screen):
    def saveAs(self):
        # self.manager.current = "navi"
        # self.manager.transition.direction = "right"
        saveAsLayout = InFileManagementPopupWindow()
        saveAsLayout.open()

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

    """
    * The method to save user selection as well as selection key to entryDataDict
    * This will be bined to on_active method of a CheckBox object
    """
    def checkboxSelected(self, theCheckbox, entryKey, selectedValue):
        entryDataDict[entryKey] = selectedValue
        print(entryDataDict)
        print(len(entryDataDict))
    
    """
    * The method to save user selection as well as selection key of a spinner to entryDataDict
    * this will be bined to on_text method of a Spinner object
    """
    def spinnerClicked(self, entryKey, selectedValue):
        entryDataDict[entryKey] = selectedValue
        print(entryDataDict)
    
    """
    * The method to save user input inside TextInput box to entryDataDict
    * This will be bined to on_text method of a TextInput object
    * Kwarg seqLen: if it is larger than 0, it means a series of textInputs will be wrapped into a list to assgin to a single key in the entryDataDict
    * Kwarg idxOfCurrentTextIpt represents the index for the current editing textInput inside the list of the series fo textInputs
    """
    def typeInsideTextInput(self, key, value, *, seqLen = 0, idxOfCurrentTextIpt = -1):
        if seqLen > 0:
            if key in entryDataDict:
                listOfValues = entryDataDict[key]
                listOfValues[idxOfCurrentTextIpt] = value
            else:
                entryDataDict[key] = ["" for i in range(seqLen)]
                entryDataDict[key][idxOfCurrentTextIpt] = value
        else:
            entryDataDict[key] = value
        print(entryDataDict)


class InputDeckApp(App):
    def build(self):
        
        Window.clearcolor = (252/255.0, 251/255.0, 244/255.0, 1)

        sm = AppScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())

        return sm


if __name__ == "__main__":
    InputDeckApp().run()