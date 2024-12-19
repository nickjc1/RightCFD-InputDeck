from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from inDataDict import entryDataDict

from customizedComponents.customizedComponents import *

Builder.load_file("lineoutBdry/lineoutBdry.kv")
class LineoutBdryLayout(BoxLayout):

    """
    This method is called after the kv properties have been set
    """
    def on_kv_post(self, base_widget):
        self.currentNumOfEntry = 1

        if "nlineout_bdry" not in entryDataDict: # in case if we import data from .txt file, so that below lines won't wipe out the data that has been read.
            entryDataDict["nlineout_bdry"] = 1
            entryDataDict["lineout_bdry"] = ["1", "", "", ""]

        print(entryDataDict)

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

        self.ids["nlineout_bdry-"].text = "{}".format(self.currentNumOfEntry)
        entryDataDict["nlineout_bdry"] = self.currentNumOfEntry

        newLineoutBdryEntrySubList = ["{}".format(self.currentNumOfEntry), "", "", ""]

        if isNewEntry: # if It is to create a new empty entry for user to type in, set to True; If it is to set up certain number of entries for import data, set to False
            entryDataDict["lineout_bdry"].extend(newLineoutBdryEntrySubList)
            
        # print(self.ids.keys())
        # print(entryDataDict)
    
    
    """
    """
    def addOneMoreBdryNameEntry(self):
        lineout_bdryLabel = BlackLabel()
        lineout_bdryLabel.text = "lineout_bdry"
        self.ids["lineout_bdry-{}1".format(self.currentNumOfEntry+1)] = lineout_bdryLabel

        lineoutSeqLabel = BlackLabel()
        lineoutSeqLabel.halign = "right"
        lineoutSeqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["lineoutSeq-{}2".format(self.currentNumOfEntry+1)] = lineoutSeqLabel

        lineoutBdnumTextInput = TextInput()
        lineoutBdnumTextInput.multiline = False
        lineoutBdnumTextInput.text = ""
        lineoutBdnumTextInput.id = "lineoutBdnum-text-{}3".format(self.currentNumOfEntry+1) 
        self.ids[lineoutBdnumTextInput.id] = lineoutBdnumTextInput
        lineoutBdnumTextInput.bind(text=self.typeInsideTextInput)

        lineoutDirectionTextInput =  TextInput()
        lineoutDirectionTextInput.multiline = False
        lineoutDirectionTextInput.text = ""
        lineoutDirectionTextInput.id = "lineoutDirection-text-{}4".format(self.currentNumOfEntry+1)
        self.ids[lineoutDirectionTextInput.id] = lineoutDirectionTextInput
        lineoutDirectionTextInput.bind(text=self.typeInsideTextInput)

        lineoutPositionTextInput =  TextInput()
        lineoutPositionTextInput.multiline = False
        lineoutPositionTextInput.text = ""
        lineoutPositionTextInput.id = "lineoutPosition-text-{}5".format(self.currentNumOfEntry+1)
        self.ids[lineoutPositionTextInput.id] = lineoutPositionTextInput
        lineoutPositionTextInput.bind(text=self.typeInsideTextInput)


        theLayout = self.ids["lineoutBdryGridLayout"]
        theLayout.add_widget(lineout_bdryLabel)
        theLayout.add_widget(lineoutSeqLabel)
        theLayout.add_widget(lineoutBdnumTextInput)
        theLayout.add_widget(lineoutDirectionTextInput) 
        theLayout.add_widget(lineoutPositionTextInput)

        theLayout = None


    """
    """    
    def deleteOneBdryEntry(self): 
        if self.currentNumOfEntry > 1 :
            lineoutBdryGridLayout = self.ids["lineoutBdryGridLayout"]
            
             
            idToBeDeleted = []# temporary list that is used to store the ids that are goint to be removed.

            # Get suffixes of the ids of the last line which is going to be deleted.
            suffixes = ["{}{}".format(self.currentNumOfEntry, i) for i in range(1, 6)]
            # print(suffixes)

            # remove the widgets of last line of entries from the layout
            for (id_key, widget) in self.ids.items():
                if any(id_key.endswith("-{}".format(i)) for i in suffixes):
                    idToBeDeleted.append(id_key)
                    lineoutBdryGridLayout.remove_widget(widget)
                    
            
            # remove the ids relating to the removed widgets from self.ids dictionary
            for id_key in idToBeDeleted:
                if id_key in self.ids:
                    self.ids.pop(id_key)

            # remove last line of entries from the entryDataDict     
            for i in range(0, 4):
                entryDataDict["lineout_bdry"].pop(-1)

            # print(entryDataDict)
            # print(self.ids.keys())
            
            self.currentNumOfEntry -= 1
            self.ids["nlineout_bdry-"].text = "{}".format(self.currentNumOfEntry)




    def typeInsideTextInput(self, instance, value, *, idFromKv=""):

        # if the id is assigned in the .kv file, the instance.id won't exist. Thus the id needs to be pass here directly through idFromKv parameter
        if(idFromKv == ""):
            id = instance.id
        else:
            id = idFromKv
        
        # print(id)

        idInfos = id.split("-")
        idNum = int(idInfos[-1])
        if (idInfos[0].startswith("lineout")):
            index = (idNum//10 - 1)*5 + (idNum%10) - (idNum//10)- 1
            # print("index is {}".format(index))
            entryDataDict["lineout_bdry"][index] = value

        print(entryDataDict)









         

