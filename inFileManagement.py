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
    

    
class InFileChooser(FileChooserListView):
    pass


class FileManagement:

    entryData = {}

    @classmethod
    def readFile(cls, *, filePathAndName):
        with open(filePathAndName, "r") as file:

            line = file.readline()
            while line != "":
                if not line.startswith("#"):
                    line = line.split("#")[0] # take away all the comment in current line
                    elementsInCurrentLine = line.split() # put all elments of current line into a list named elementsInCurrentLine
                    if len(elementsInCurrentLine) == 2: # If there are only 2 elements in the list
                        cls.entryData[elementsInCurrentLine[0]] = elementsInCurrentLine[1]
                    elif len(elementsInCurrentLine) > 2: # if there are more than 2 elements in the list
                        # check if current key exists
                        # if it does, extend the values of current key with the new values
                        # if it does not, add this new pair to the dict
                        key = elementsInCurrentLine[0] 
                        if key in cls.entryData:
                            cls.entryData[key].extend(elementsInCurrentLine[1:])
                        else:
                            cls.entryData[key] = elementsInCurrentLine[1:]
                    else:
                        pass
                line = file.readline()
            file.close()
        
        for key in cls.entryData:
            print(key, cls.entryData[key])
    
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


        

