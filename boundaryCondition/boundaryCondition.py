from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from inDataDict import entryDataDict

from customizedComponents.customizedComponents import *

Builder.load_file("boundaryCondition/boundaryCondition.kv")
class BoundaryConditionLayout(BoxLayout):

    # This method is called after the kv properties have been set
    def on_kv_post(self, base_widget):
        self.currentNumOfEntry = 1
        self.entriesInitialize(numOfEntry=5-1) # The reason of minus 1 is that by default, there is one entry being set up already after .kv file has been posted.

        return super().on_kv_post(base_widget)
    

    """
    etriesInitialize() is used to initialize the bdry entries block inside BoundaryConditionLayout. 
    """
    def entriesInitialize(self, *, numOfEntry):
        
        for i in range(numOfEntry):
            self.addOneMoreEntry()

    
    """
    """
    def addOneMoreEntry(self):

        self.addOneMoreBdryNameEntry()
        self.addOneMoreBdryDetailEntry() 

        self.currentNumOfEntry += 1

        self.ids["nbc-"].text = "{}".format(self.currentNumOfEntry)
    
    
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
        self.ids["bdry_nameLabel-{}".format(self.currentNumOfEntry+1)] = bdry_nameLabel

        seqLabel = BlackLabel()
        seqLabel.halign = "right"
        seqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["bdry_nameSeqLabel-{}".format(self.currentNumOfEntry+1)] = seqLabel

        bdnumTextInput = TextInput()
        bdnumTextInput.multiline = False
        bdnumTextInput.text = ""
        self.ids["bdry_nameBdnumTextInput-{}".format(self.currentNumOfEntry+1)] = bdnumTextInput

        nameTextInput =  TextInput()
        nameTextInput.multiline = False
        bdnumTextInput.text = ""
        self.ids["nameTextInput-{}".format(self.currentNumOfEntry+1)] = nameTextInput


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
        self.ids["bc-{}".format(self.currentNumOfEntry + 1)] = bc_label

        seqLabel = BlackLabel()
        seqLabel.text = "{}".format(self.currentNumOfEntry + 1)
        seqLabel.halign = "right"
        self.ids["bc-seq-{}".format(self.currentNumOfEntry + 1)] = seqLabel

        bc_sc1 = TextInput()
        bc_sc1.multiline = False
        bc_sc1.text = ""
        self.ids["bc-sc1-{}".format(self.currentNumOfEntry + 1)] = bc_sc1

        bc_sc2 = TextInput()
        bc_sc2.multiline = False
        bc_sc2.text = ""
        self.ids["bc-sc2-{}".format(self.currentNumOfEntry + 1)] = bc_sc2

        bc_p1 = TextInput()
        bc_p1.multiline = False
        bc_p1.text = ""
        self.ids["bc-p1-{}".format(self.currentNumOfEntry + 1)] = bc_p1

        bc_p2 = TextInput()
        bc_p2.multiline = False
        bc_p2.text = ""
        self.ids["bc-p2-{}".format(self.currentNumOfEntry + 1)] = bc_p2

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
        if self.currentNumOfEntry > 0 :
            bdry_nameGridLayout = self.ids["bdry_nameGridLayout"]
            bcGridLayout = self.ids["bcGridLayout"]
            
            idToBeDeleted = []
            for (id_key, widget) in self.ids.items():
                if id_key.endswith("-{}".format(self.currentNumOfEntry)):
                    idToBeDeleted.append(id_key)
                    if widget in bdry_nameGridLayout.children:
                        bdry_nameGridLayout.remove_widget(widget)
                    else:
                        bcGridLayout.remove_widget(widget)

            for id_key in idToBeDeleted:
                if id_key in self.ids:
                    self.ids.pop(id_key)

            # print(self.ids)
            
            self.currentNumOfEntry -= 1
            self.ids["nbc-"].text = "{}".format(self.currentNumOfEntry)

            bdry_nameGridLayout = None
            bcGridLayout = None








         

