from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from inDataDict import entryDataDict

from customizedComponents.customizedComponents import *

Builder.load_file("boundaryCondition/linearDbc.kv")
class LinearDbcLayout(BoxLayout):

    """
    This method is called after the kv properties have been set
    """
    def on_kv_post(self, base_widget):
        self.currentNumOfEntry = 1

        if "nlinearDbc" not in entryDataDict: # in case if we import data from .txt file, so that below lines won't wipe out the data that has been read.
            entryDataDict["nlinearDbc"] = 1
            entryDataDict["linear_Dbc"] = ["1", "", "", "", ""]

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

        self.ids["nlinearDbc-"].text = "{}".format(self.currentNumOfEntry)
        entryDataDict["nlinearDbc"] = self.currentNumOfEntry

        newLinearDbcEntrySubList = ["{}".format(self.currentNumOfEntry), "", "", "", ""]

        if isNewEntry: # if It is to create a new empty entry for user to type in, set to True; If it is to set up certain number of entries for import data, set to False
            entryDataDict["linear_Dbc"].extend(newLinearDbcEntrySubList)
            
        # print(self.ids.keys())
        # print(entryDataDict)
    
    
    """
    """
    def addOneMoreBdryNameEntry(self):
        linear_DbcLabel = BlackLabel()
        linear_DbcLabel.text = "linear_Dbc"
        self.ids["linear_Dbc-{}1".format(self.currentNumOfEntry+1)] = linear_DbcLabel

        linSeqLabel = BlackLabel()
        linSeqLabel.halign = "right"
        linSeqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["linSeq-{}2".format(self.currentNumOfEntry+1)] = linSeqLabel

        linBdnumTextInput = TextInput()
        linBdnumTextInput.multiline = False
        linBdnumTextInput.text = ""
        linBdnumTextInput.id = "linBdnum-text-{}3".format(self.currentNumOfEntry+1) 
        self.ids[linBdnumTextInput.id] = linBdnumTextInput
        linBdnumTextInput.bind(text=self.typeInsideTextInput)

        linDirTextInput =  TextInput()
        linDirTextInput.multiline = False
        linDirTextInput.text = ""
        linDirTextInput.id = "linDir-text-{}4".format(self.currentNumOfEntry+1)
        self.ids[linDirTextInput.id] = linDirTextInput
        linDirTextInput.bind(text=self.typeInsideTextInput)

        linKTextInput =  TextInput()
        linKTextInput.multiline = False
        linKTextInput.text = ""
        linKTextInput.id = "linK-text-{}5".format(self.currentNumOfEntry+1)
        self.ids[linKTextInput.id] = linKTextInput
        linKTextInput.bind(text=self.typeInsideTextInput)

        linBTextInput =  TextInput()
        linBTextInput.multiline = False
        linBTextInput.text = ""
        linBTextInput.id = "linB-text-{}6".format(self.currentNumOfEntry+1)
        self.ids[linBTextInput.id] = linBTextInput
        linBTextInput.bind(text=self.typeInsideTextInput)

        theLayout = self.ids["linear_DbcGridLayout"]
        theLayout.add_widget(linear_DbcLabel)
        theLayout.add_widget(linSeqLabel)
        theLayout.add_widget(linBdnumTextInput)
        theLayout.add_widget(linDirTextInput) 
        theLayout.add_widget(linKTextInput)
        theLayout.add_widget(linBTextInput)

        theLayout = None


    """
    """    
    def deleteOneBdryEntry(self): 
        if self.currentNumOfEntry > 1 :
            linear_DbcGridLayout = self.ids["linear_DbcGridLayout"]
            
             
            idToBeDeleted = []# temporary list that is used to store the ids that are goint to be removed.

            # Get suffixes of the ids of the last line which is going to be deleted.
            suffixes = ["{}{}".format(self.currentNumOfEntry, i) for i in range(1, 7)]
            # print(suffixes)

            # remove the widgets of last line of entries from the layout
            for (id_key, widget) in self.ids.items():
                if any(id_key.endswith("-{}".format(i)) for i in suffixes):
                    idToBeDeleted.append(id_key)
                    linear_DbcGridLayout.remove_widget(widget)
                    
            
            # remove the ids relating to the removed widgets from self.ids dictionary
            for id_key in idToBeDeleted:
                if id_key in self.ids:
                    self.ids.pop(id_key)

            # remove last line of entries from the entryDataDict     
            for i in range(0, 5):
                entryDataDict["linear_Dbc"].pop(-1)

            # print(entryDataDict)
            # print(self.ids.keys())
            
            self.currentNumOfEntry -= 1
            self.ids["nlinearDbc-"].text = "{}".format(self.currentNumOfEntry)




    def typeInsideTextInput(self, instance, value, *, idFromKv=""):

        # if the id is assigned in the .kv file, the instance.id won't exist. Thus the id needs to be pass here directly through idFromKv parameter
        if(idFromKv == ""):
            id = instance.id
        else:
            id = idFromKv
        
        # print(id)

        idInfos = id.split("-")
        idNum = int(idInfos[-1])
        if (idInfos[0].startswith("lin")):
            index = (idNum//10 - 1)*6 + (idNum%10) - (idNum//10)- 1
            # print("index is {}".format(index))
            entryDataDict["linear_Dbc"][index] = value

        # print(entryDataDict)









         

