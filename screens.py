'''
author: Chao

screens.py:
    class:
        SolverChooserPopup(Popup) <==> solverChooserPopup.kv/<SolverChooserPopup>
        AppScreenManager(ScreenManager)
        StartUpScreen(Screen) <==> naviWindow.kv/<StartUpScreen>
        InFileDetailsScreen(Screen) <==> inDetails.kv/<InFileDetailsScreen>
'''

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.app import App

from inFileManagement import InFileManagementPopupWindow # The File contains popup window, which is used to  save data to local disk, functionality
from meshAndSimuControl import MeshAndSimuControlLayout

from inDataDict import entryDataDict

Builder.load_file("solverChooserPopup.kv")
class SolverChooserPopup(Popup):

    def gotoInDetails(self):
        sm = App.get_running_app().root
        
        # create inFileDetails screen instance
        # add the instance into the screen manager
        inFileDetailsWindow = InFileDetailsScreen() # need to import class MeshAndSimuControlLayout()
        sm.add_widget(inFileDetailsWindow)
        inFileDetailsWindow.manager.transition.direction = "left" # manager attribute is only assigned to a screen after the sreen is added to the ScreenManager

        sm.current = "inDetails"

        self.dismiss()


class AppScreenManager(ScreenManager):
     def __init__(self, **kwargs):
         super().__init__(**kwargs)


Builder.load_file("naviWindow.kv")
class StartUpScreen(Screen):

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


        # configure the pop up window to meet the import window requirement
        popup.ids.leftButton.text = "Import"
        popup.bindImportSelectedFileDataToLeftButton()

        popup.ids.inFileChooser.filters = [] # The file chooser window will show both file and directory

        # call this method to bind ReadDataAndDismissInFileManagementPopupWindow() to popup window InFileChooser's property selection
        popup.bindGetSelectedFilePathToInFileChooser()

        popup.open()

Builder.load_file("inDetails.kv")
class InFileDetailsScreen(Screen):

    def saveAs(self):
        saveAsLayout = InFileManagementPopupWindow() 
        saveAsLayout.bindSaveDataAndDismissInFileManagementPopupWindowToLeftButton()
        saveAsLayout.open()
    
    def cancel(self):
        entryDataDict.clear()
        sm = App.get_running_app().root
        sm.current = "navi"
        self.manager.transition.direction = "right"

        # dereference the InFileDetailsScreen instance(widget)
        inFileDetailsScreen = None
        for screen in sm.screens:
            if screen.name == "inDetails":
                inFileDetailsScreen = screen
        sm.remove_widget(inFileDetailsScreen)
        inFileDetailsScreen = None

        
        

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