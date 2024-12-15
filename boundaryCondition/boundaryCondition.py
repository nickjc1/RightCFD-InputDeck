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
        # self.entriesInitialize(numOfEntry=self.currentNumOfEntry)

        return super().on_kv_post(base_widget)
    

    """
    bdry_nameEtriesInitialize() is used to initialize the bdry_name entries block inside BoundaryConditionLayout. 
    """
    def entriesInitialize(self, *, numOfEntry):
        
        for i in range(numOfEntry):
            bdry_nameLabel = BlackLabel()
            bdry_nameLabel.text = "bdry_name"

            seqLabel = BlackLabel()
            seqLabel.halign = "right"
            seqLabel.text = "{}".format(i+1)
            self.ids["bdry_nameSeqLabel{}".format(i+1)] = seqLabel

            bdnumTextInput = TextInput()
            bdnumTextInput.multiline = False
            bdnumTextInput.text = ""
            self.ids["bdry_nameBdnumTextInput{}".format(i+1)] = bdnumTextInput

            nameTextInput =  TextInput()
            nameTextInput.multiline = False
            bdnumTextInput.text = ""
            self.ids["nameTextInput{}".format(i+1)] = nameTextInput


            # create a pointer that points to the GridLayout object inside self.
            theLayout = self.ids["bdry_nameGridLayout"]

            theLayout.add_widget(bdry_nameLabel)
            theLayout.add_widget(seqLabel)
            theLayout.add_widget(bdnumTextInput)
            theLayout.add_widget(nameTextInput)

        # print(self.ids)

    def addOneMoreEntry(self):
        bdry_nameLabel = BlackLabel()
        bdry_nameLabel.text = "bdry_name"

        seqLabel = BlackLabel()
        seqLabel.halign = "right"
        seqLabel.text = "{}".format(self.currentNumOfEntry+1)
        self.ids["bdry_nameSeqLabel{}".format(self.currentNumOfEntry+1)] = seqLabel

        bdnumTextInput = TextInput()
        bdnumTextInput.multiline = False
        bdnumTextInput.text = ""
        self.ids["bdry_nameBdnumTextInput{}".format(self.currentNumOfEntry+1)] = bdnumTextInput

        nameTextInput =  TextInput()
        nameTextInput.multiline = False
        bdnumTextInput.text = ""
        self.ids["nameTextInput{}".format(self.currentNumOfEntry+1)] = nameTextInput


        # create a pointer that points to the GridLayout object inside self.
        theLayout = self.ids["bdry_nameGridLayout"]

        theLayout.add_widget(bdry_nameLabel)
        theLayout.add_widget(seqLabel)
        theLayout.add_widget(bdnumTextInput)
        theLayout.add_widget(nameTextInput) 

        print(theLayout.height)
        # self.height = self.minimum_height
        # print(self.height)
        # self.ids["bdry_nameGridLayout"].height = self.ids["bdry_nameGridLayout"].minimum_height
        # self.parent.do_layout()

        # currentScroll_y = self.parent.scroll_y


        
        self.currentNumOfEntry += 1
            
    




         

