from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.app import App

from inDataDict import entryDataDict

Builder.load_file("inFileManagementLayout.kv")

class InFileManagementPopupWindow(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selectedFilePath = ""

    """
    isDirectoryAndOutputToinPathTextInput() is used in the InFileChooser filter to only show directories in the InFileChooser window
    isDirectoryAndOutputToinPathTextInput() also print out the path of current directory shown on window to the inPathTextInput 
    """
    def isDirectoryAndOutputToInPathTextInput(self, currentDirectory, fileOrDirectoryName):
        if currentDirectory == "/":
            self.ids.inPathTextInput.text = currentDirectory
        else:
            self.ids.inPathTextInput.text = currentDirectory + "/"
        
        return fileOrDirectoryName.endswith("/")

    """
    bind saveDataAndDismissInFileManagementPopupWindow() to the leftButton of InFileManagementPoppopWindow
    """
    def bindSaveDataAndDismissInFileManagementPopupWindowToLeftButton(self):
        self.ids.leftButton.bind(on_press=self.saveDataAndDismissInFileManagementPopupWindow)


    """
    saveDataAndDismissInFileManagementPopupWindow() is used to write the user edited data to local disk.
    The user edited data has been saved inside global dict entryDataDict.
    This method will bind to LeftButton.
    """
    def saveDataAndDismissInFileManagementPopupWindow(self, instance):
        FileManagement.writeToFile(filePathAndName = self.ids.inPathTextInput.text)
        self.dismiss()
    

    """
    """
    def bindGetSelectedFilePathToInFileChooser(self):        
        """
        selection: This is a property of the FileChooserListView. When bind to selection, we are binding directly to the property selection itself, meaning the binding will trigger whenever the selection changes.
        we are telling Kivy to call self.getSelectedFilePath every time the selection property changes.
        * When to Use selection vs on_selection:
            Use selection when you want to respond to changes in the selection property directly. This is more reliable because it directly observes the property.
        """
        self.ids.inFileChooser.bind(selection=self.getSelectedFilePath)


    """
    getSelectedFilePath() is to grab the full path of selected file and save it into property self.selectedFilePath;
    The full path will be wrapped with ""
    """
    def getSelectedFilePath(self, instance, selection):
        if len(selection) > 0:
            self.selectedFilePath = selection[0]
            print(self.selectedFilePath)


    """
    * Bind importSelectedFileDataTo() leftButton of InFileManagementPopupWindow instance
    """
    def bindImportSelectedFileDataToLeftButton(self):
        self.ids.leftButton.bind(on_press=self.importSelectedFileData) 


    """
    * If the filePath is valid (need to modify the code to verify), import the data from that file into entryDataDict
    * Then call self.showDataToInFileDetailsWindow(theWindow=inFileDetailsWindow) to grab the data from entryDataDict to the inFileDetailsWindow.
    """
    def importSelectedFileData(self, instance):
        # local import -- to avoid the circular dependency
        from screens import InFileDetailsScreen
        # print(self.selectedFilePath)
        filePath = self.selectedFilePath

        if True:
            FileManagement.readFile(filePathAndName = filePath)
            print(entryDataDict)

            inFileDetailsWindow = InFileDetailsScreen()
            self.showDataToInFileDetailsWindow(theWindow=inFileDetailsWindow)

            sm = App.get_running_app().root
            sm.add_widget(inFileDetailsWindow)
            inFileDetailsWindow.manager.transition.direction = "right"
            sm.current = "inDetails"

            self.dismiss()

    """
    * Cross compair keys inside entryDataDict and ids from meshAndSimuControlLayoutPannel.ids
    * grab approrate data and put them into widgets of inFileDetailsWindow screen.
    """    
    def showDataToInFileDetailsWindow(self, *, theWindow):
        meshAndSimuControlLayoutPanel = theWindow.ids["meshAndSimuControlLayout"]
        ids = meshAndSimuControlLayoutPanel.ids
        
        for key in entryDataDict:
            # print(key)
            for id in ids:
                # print("    " + id)
                if key == id.split("-")[0] and "-" in id: # split id string to keep the part that is same as the keys in the entryDataDict 
                    if type(entryDataDict[key]) == list: # if the value of the key in the entryDataDict is a list
                        for i in range(len(entryDataDict[key])):
                            ids[key + "-text_{}".format(i)].text = entryDataDict[key][i]
                        break
                    else:
                        if "check" in id: # if the widget of the id is a Checkbox
                            ids[key + "-check_" + entryDataDict[key]].active = True
                            break
                        elif "spinner" in id: # if the widget of the id is a Spinner
                            ids[key + "-spinner"].text = entryDataDict[key]
                            break
                        else: # if the widget of the id is a single TextInput
                            ids[key + "-"].text = entryDataDict[key]
                            break
            # print(len(entryDataDict))

    
class InFileChooser(FileChooserListView):
    pass


class FileManagement:

    TestEntryData = {}

    @classmethod
    def readFile(cls, *, filePathAndName):
        with open(filePathAndName, "r") as file:

            line = file.readline()
            while line != "":
                if not line.startswith("#"):
                    line = line.split("#")[0] # take away all the comment in current line
                    elementsInCurrentLine = line.split() # put all elments of current line into a list named elementsInCurrentLine
                    if len(elementsInCurrentLine) == 2: # If there are only 2 elements in the list
                        entryDataDict[elementsInCurrentLine[0]] = elementsInCurrentLine[1]
                    elif len(elementsInCurrentLine) > 2: # if there are more than 2 elements in the list
                        # check if current key exists
                        # if it does, extend the values of current key with the new values
                        # if it does not, add this new pair to the dict
                        key = elementsInCurrentLine[0] 
                        if key in entryDataDict:
                            entryDataDict[key].extend(elementsInCurrentLine[1:])
                        else:
                            entryDataDict[key] = elementsInCurrentLine[1:]
                    else:
                        pass
                line = file.readline()
            file.close()
    
    @classmethod
    def writeToFile(cls, *, filePathAndName):
        with open(filePathAndName, "w") as file:
            for key in entryDataDict:
                if isinstance(entryDataDict[key], list):
                    str = ""
                    for item in entryDataDict[key]:
                        str  = str + item + " "
                    file.write("{} {}\n".format(key, str))
                else:
                    file.write("{} {}\n".format(key, entryDataDict[key]))


        

