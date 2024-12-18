from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from inDataDict import entryDataDict

from customizedComponents.customizedComponents import *

Builder.load_file("boundaryCondition/boundaryCondition.kv")
class BoundaryConditionLayout(BoxLayout):

    """
    This method is called after the kv properties have been set
    """
    def on_kv_post(self, base_widget):
        self.currentNumOfEntry = 1

        if "nbc" not in entryDataDict: # in case if we import data from .txt file, so that below lines won't wipe out the data that has been read.
            entryDataDict["nbc"] = 1
            entryDataDict["bdry_name"] = ["1", "", ""]
            entryDataDict["bc"] = ["1", "", "", "", ""]

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
        self.addOneMoreBdryDetailEntry() 

        self.currentNumOfEntry += 1

        self.ids["nbc-"].text = "{}".format(self.currentNumOfEntry)
        entryDataDict["nbc"] = self.currentNumOfEntry

        newBdryNameEntrySubList = ["{}".format(self.currentNumOfEntry), "", ""]
        newBdryDetailEntrySubList = ["{}".format(self.currentNumOfEntry), "", "", "", ""]

        if isNewEntry: # if It is to create a new empty entry for user to type in, set to True; If it is to set up certain number of entries for import data, set to False
            entryDataDict["bdry_name"].extend(newBdryNameEntrySubList)
            entryDataDict["bc"].extend(newBdryDetailEntrySubList)
            
        # print(self.ids.keys())
        # print(entryDataDict)
    
    
    """
    """
    def addOneMoreBdryNameEntry(self):
        # create a pointer that points to the GridLayout object inside self.
        # self.height = self.minimum_height
        # print(self.height)
        # self.ids["bdry_nameGridLayout"].height = self.ids["bdry_nameGridLayout"].minimum_height
        # self.parent.do_layout()

        # currentScroll_y = self.parent.scroll_y
        bdry_nameLabel = BlackLabel()
        bdry_nameLabel.text = "bdry_name"
        self.ids["bdry_name-{}1".format(self.currentNumOfEntry+1)] = bdry_nameLabel

        seqLabel = BlackLabel()
        seqLabel.halign = "right"
        seqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["bdseq-{}2".format(self.currentNumOfEntry+1)] = seqLabel

        bdnumTextInput = TextInput()
        bdnumTextInput.multiline = False
        bdnumTextInput.text = ""
        bdnumTextInput.id = "bdnum-text-{}3".format(self.currentNumOfEntry+1) 
        self.ids[bdnumTextInput.id] = bdnumTextInput
        bdnumTextInput.bind(text=self.typeInsideTextInput)

        nameTextInput =  TextInput()
        nameTextInput.multiline = False
        nameTextInput.text = ""
        nameTextInput.id = "bdname-text-{}4".format(self.currentNumOfEntry+1)
        self.ids[nameTextInput.id] = nameTextInput
        nameTextInput.bind(text=self.typeInsideTextInput)


        theLayout = self.ids["bdry_nameGridLayout"]
        theLayout.add_widget(bdry_nameLabel)
        theLayout.add_widget(seqLabel)
        theLayout.add_widget(bdnumTextInput)
        theLayout.add_widget(nameTextInput) 

        theLayout = None


    """
    """
    def addOneMoreBdryDetailEntry(self):
        bc_label = BlackLabel()
        bc_label.text = "bc"
        self.ids["bc-{}1".format(self.currentNumOfEntry + 1)] = bc_label

        seqLabel = BlackLabel()
        seqLabel.text = "{}".format(self.currentNumOfEntry + 1)
        seqLabel.halign = "right"
        self.ids["bc_seq-{}2".format(self.currentNumOfEntry + 1)] = seqLabel

        bc_sc1 = TextInput()
        bc_sc1.multiline = False
        bc_sc1.text = ""
        bc_sc1.id = "bc_sc-text-{}3".format(self.currentNumOfEntry + 1)
        self.ids[bc_sc1.id] = bc_sc1
        bc_sc1.bind(text=self.typeInsideTextInput)

        bc_sc2 = TextInput()
        bc_sc2.multiline = False
        bc_sc2.text = ""
        bc_sc2.id = "bc_sc-text-{}4".format(self.currentNumOfEntry + 1)
        self.ids[bc_sc2.id] = bc_sc2
        bc_sc2.bind(text=self.typeInsideTextInput)

        bc_p1 = TextInput()
        bc_p1.multiline = False
        bc_p1.text = ""
        bc_p1.id = "bc_p-text-{}5".format(self.currentNumOfEntry + 1)
        self.ids[bc_p1.id] = bc_p1
        bc_p1.bind(text=self.typeInsideTextInput)

        bc_p2 = TextInput()
        bc_p2.multiline = False
        bc_p2.text = ""
        bc_p2.id = "bc_p-text-{}6".format(self.currentNumOfEntry + 1)
        self.ids[bc_p2.id] = bc_p2
        bc_p2.bind(text=self.typeInsideTextInput)

        theLayout = self.ids["bcGridLayout"]
        theLayout.add_widget(bc_label)
        theLayout.add_widget(seqLabel)
        theLayout.add_widget(bc_sc1)
        theLayout.add_widget(bc_sc2)
        theLayout.add_widget(bc_p1)
        theLayout.add_widget(bc_p2)

        theLayout = None


    """
    """    
    def deleteOneBdryEntry(self): 
        if self.currentNumOfEntry > 1 :
            bdry_nameGridLayout = self.ids["bdry_nameGridLayout"]
            bcGridLayout = self.ids["bcGridLayout"]
            
             
            idToBeDeleted = []# temporary list that is used to store the ids that are goint to be removed.

            # Get suffixes of the ids of the last line which is going to be deleted.
            suffixes = ["{}{}".format(self.currentNumOfEntry, i) for i in range(1, 7)]
            # print(suffixes)

            # remove the widgets of last line of entries from the layout
            for (id_key, widget) in self.ids.items():
                if any(id_key.endswith("-{}".format(i)) for i in suffixes):
                    idToBeDeleted.append(id_key)
                    if widget in bdry_nameGridLayout.children:
                        bdry_nameGridLayout.remove_widget(widget)
                    else:
                        bcGridLayout.remove_widget(widget)
            
            # remove the ids relating to the removed widgets from self.ids dictionary
            for id_key in idToBeDeleted:
                if id_key in self.ids:
                    self.ids.pop(id_key)

            # remove last line of entries from the entryDataDict     
            for i in range(0, 3):
                entryDataDict["bdry_name"].pop(-1)
            for i in range(0, 5):
                entryDataDict["bc"].pop(-1)

            # print(entryDataDict)
            # print(self.ids.keys())
            
            self.currentNumOfEntry -= 1
            self.ids["nbc-"].text = "{}".format(self.currentNumOfEntry)

            bdry_nameGridLayout = None
            bcGridLayout = None




    def typeInsideTextInput(self, instance, value, *, idFromKv=""):

        # if the id is assigned in the .kv file, the instance.id won't exist. Thus the id needs to be pass here directly through idFromKv parameter
        if(idFromKv == ""):
            id = instance.id
        else:
            id = idFromKv
        
        # print(id)

        idInfos = id.split("-")
        idNum = int(idInfos[-1])
        if (idInfos[0].startswith("bd")):
            index = (idNum//10 - 1)*4 + (idNum%10) - (idNum//10)- 1
            # print("index is {}".format(index))
            entryDataDict["bdry_name"][index] = value
        elif (idInfos[0].startswith("bc")):
            index = (idNum//10 - 1)*6 + (idNum%10) - (idNum//10)- 1
            entryDataDict["bc"][index] = value

        print(entryDataDict)









         

