from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from inDataDict import entryDataDict

from customizedComponents.customizedComponents import *

Builder.load_file("lineoutInterior/lineoutInterior.kv")
class LineoutInteriorLayout(BoxLayout):

    """
    This method is called after the kv properties have been set
    """
    def on_kv_post(self, base_widget):
        self.currentNumOfEntry = 1

        if "nlineout_interior" not in entryDataDict: # in case if we import data from .txt file, so that below lines won't wipe out the data that has been read.
            entryDataDict["nlineout_interior"] = 1
            entryDataDict["lineout_interior"] = ["1", "", "", "", "", "", ""]

        # print(entryDataDict)

        return super().on_kv_post(base_widget)
    

    """
    etriesInitialize() is used to initialize the bdry entries block inside BoundaryConditionLayout. 
    """
    def entriesInitialize(self, *, numOfEntry):
        for i in range(numOfEntry):
            self.addOneMoreEntry(isNewEntry=False)
            self.currentNumOfEntry == 1

    
    """
    """
    def addOneMoreEntry(self, *, isNewEntry):
        self.addOneMoreBdryNameEntry()

        self.currentNumOfEntry += 1

        self.ids["nlineout_interior-"].text = "{}".format(self.currentNumOfEntry)
        entryDataDict["nlineout_interior"] = self.currentNumOfEntry

        newLineoutBdryEntrySubList = ["{}".format(self.currentNumOfEntry), "", "", "", "", "", ""]

        if isNewEntry: # if It is to create a new empty entry for user to type in, set to True; If it is to set up certain number of entries for import data, set to False
            entryDataDict["lineout_interior"].extend(newLineoutBdryEntrySubList)
            
        # print(self.ids.keys())
        print(entryDataDict)
    
    
    """
    """
    def addOneMoreBdryNameEntry(self):
        lineout_interiorLabel = BlackLabel()
        lineout_interiorLabel.text = "lineout_interior"
        self.ids["lineout_interior-{}1".format(self.currentNumOfEntry+1)] = lineout_interiorLabel

        lineInterSeqLabel = BlackLabel()
        lineInterSeqLabel.halign = "right"
        lineInterSeqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["lineInterSeq-{}2".format(self.currentNumOfEntry+1)] = lineInterSeqLabel

        lineInterSXTextInput = TextInput()
        lineInterSXTextInput.multiline = False
        lineInterSXTextInput.text = ""
        lineInterSXTextInput.id = "lineInterSX-text-{}3".format(self.currentNumOfEntry+1) 
        self.ids[lineInterSXTextInput.id] = lineInterSXTextInput
        lineInterSXTextInput.bind(text=self.typeInsideTextInput)

        lineInterSYTextInput =  TextInput()
        lineInterSYTextInput.multiline = False
        lineInterSYTextInput.text = ""
        lineInterSYTextInput.id = "lineInterSY-text-{}4".format(self.currentNumOfEntry+1)
        self.ids[lineInterSYTextInput.id] = lineInterSYTextInput
        lineInterSYTextInput.bind(text=self.typeInsideTextInput)

        lineInterSZTextInput =  TextInput()
        lineInterSZTextInput.multiline = False
        lineInterSZTextInput.text = ""
        lineInterSZTextInput.id = "lineInterSZ-text-{}5".format(self.currentNumOfEntry+1)
        self.ids[lineInterSZTextInput.id] = lineInterSZTextInput
        lineInterSZTextInput.bind(text=self.typeInsideTextInput)

        lineInterEXTextInput = TextInput()
        lineInterEXTextInput.multiline = False
        lineInterEXTextInput.text = ""
        lineInterEXTextInput.id = "lineInterEX-text-{}6".format(self.currentNumOfEntry+1) 
        self.ids[lineInterEXTextInput.id] = lineInterEXTextInput
        lineInterEXTextInput.bind(text=self.typeInsideTextInput)

        lineInterEYTextInput =  TextInput()
        lineInterEYTextInput.multiline = False
        lineInterEYTextInput.text = ""
        lineInterEYTextInput.id = "lineInterEY-text-{}7".format(self.currentNumOfEntry+1)
        self.ids[lineInterEYTextInput.id] = lineInterEYTextInput
        lineInterEYTextInput.bind(text=self.typeInsideTextInput)

        lineInterEZTextInput =  TextInput()
        lineInterEZTextInput.multiline = False
        lineInterEZTextInput.text = ""
        lineInterEZTextInput.id = "lineInterEZ-text-{}8".format(self.currentNumOfEntry+1)
        self.ids[lineInterEZTextInput.id] = lineInterEZTextInput
        lineInterEZTextInput.bind(text=self.typeInsideTextInput)

        theLayout = self.ids["lineoutInteriorGridLayout"]
        theLayout.add_widget(lineout_interiorLabel)
        theLayout.add_widget(lineInterSeqLabel)
        theLayout.add_widget(lineInterSXTextInput)
        theLayout.add_widget(lineInterSYTextInput) 
        theLayout.add_widget(lineInterSZTextInput)
        theLayout.add_widget(lineInterEXTextInput) 
        theLayout.add_widget(lineInterEYTextInput)
        theLayout.add_widget(lineInterEZTextInput)

        theLayout = None


    """
    """    
    def deleteOneBdryEntry(self): 
        if self.currentNumOfEntry > 1 :
            lineoutInteriorGridLayout = self.ids["lineoutInteriorGridLayout"]
            
             
            idToBeDeleted = []# temporary list that is used to store the ids that are goint to be removed.

            # Get suffixes of the ids of the last line which is going to be deleted.
            suffixes = ["{}{}".format(self.currentNumOfEntry, i) for i in range(1, 9)]
            # print(suffixes)

            # remove the widgets of last line of entries from the layout
            for (id_key, widget) in self.ids.items():
                if any(id_key.endswith("-{}".format(i)) for i in suffixes):
                    idToBeDeleted.append(id_key)
                    lineoutInteriorGridLayout.remove_widget(widget)
                    
            
            # remove the ids relating to the removed widgets from self.ids dictionary
            for id_key in idToBeDeleted:
                if id_key in self.ids:
                    self.ids.pop(id_key)

            # remove last line of entries from the entryDataDict     
            for i in range(0, 7):
                entryDataDict["lineout_interior"].pop(-1)

            # print(entryDataDict)
            # print(self.ids.keys())
            
            self.currentNumOfEntry -= 1
            self.ids["nlineout_interior-"].text = "{}".format(self.currentNumOfEntry)




    def typeInsideTextInput(self, instance, value, *, idFromKv=""):

        # if the id is assigned in the .kv file, the instance.id won't exist. Thus the id needs to be pass here directly through idFromKv parameter
        if(idFromKv == ""):
            id = instance.id
        else:
            id = idFromKv
        
        # print(id)

        idInfos = id.split("-")
        idNum = int(idInfos[-1])
        if (idInfos[0].startswith("lineInter")):
            index = (idNum//10 - 1)*8 + (idNum%10) - (idNum//10)- 1
            # print("index is {}".format(index))
            entryDataDict["lineout_interior"][index] = value

        print(entryDataDict)









         

