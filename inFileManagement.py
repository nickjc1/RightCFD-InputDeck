from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder

from inDataDict import entryDataDict

Builder.load_file("inFileManagementLayout.kv")

class InFileManagementPopupWindow(Popup):

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
    saveDataAndDismissInFileManagementPopupWindow() is used to write the user edited data to local disk.
    The user edited data has been saved inside global dict entryDataDict.
    """
    def saveDataAndDismissInFileManagementPopupWindow(self):
        FileManagement.writeToFile(filePathAndName = self.ids.inPathTextInput.text)
        self.dismiss()
    

    """
    """
    def bindReadDataAndDismissInFileManagementPopupWindowToInFileChooser(self):        
        """
        selection: This is a property of the FileChooserListView. When bind to selection, we are bind{ing directly to the property change itself, meaning the binding will trigger whenever the selection changes.
        we are telling Kivy to call self.readDataAndDismissInFileManagementPopupWindow every time the selection property changes.
        * When to Use selection vs on_selection:
            Use selection when you want to respond to changes in the selection property directly. This is more reliable because it directly observes the property.
        """
        self.ids.inFileChooser.bind(selection=self.readDataAndDismissInFileManagementPopupWindow)


    """
    """
    def readDataAndDismissInFileManagementPopupWindow(self, instance, selection):
        filePath = instance.selection[0]
        FileManagement.readFile(filePathAndName=filePath)
    

    
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


        

