from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder

from inDataDict import entryDataDict

Builder.load_file("inFileManagementLayout.kv")

class InFileManagementPopupWindow(Popup):

    """
    isDirectory() is used in the InFileChooser filter to only show directories in the InFileChooser window
    isDirectory() also print out the path of current directory shown on window to the inPath textInput 
    """
    def isDirectoryAndOutputToInPath(self, currentDirectory, fileOrDirectoryName):
        if currentDirectory == "/":
            self.ids.inPath.text = currentDirectory
        else:
            self.ids.inPath.text = currentDirectory + "/"
        
        return fileOrDirectoryName.endswith("/")


    """
    """
    def saveDataAndDismissInFileManagementPopupWindow(self):
        with open(self.ids.inPath.text, "w") as file:
            for key in entryDataDict:
                if isinstance(entryDataDict[key], list):
                    str = ""
                    for item in entryDataDict[key]:
                        str  = str + item + " "
                    file.write("{} {}\n".format(key, str))
                else:
                    file.writelines("{} {}\n".format(key, entryDataDict[key]))
            self.dismiss()

class InFileChooser(FileChooserListView):
    pass
