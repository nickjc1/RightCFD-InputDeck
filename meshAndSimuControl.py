from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout

from inDataDict import entryDataDict

Builder.load_file("meshAndSimuControl.kv")
class MeshAndSimuControlLayout(GridLayout):

    """
    * The method to save user selection as well as selection key to entryDataDict
    * This will be bined to on_active method of a CheckBox object
    """
    def checkboxSelected(self, theCheckbox, entryKey, selectedValue):
        entryDataDict[entryKey] = selectedValue
        # print(entryDataDict)
        # print(len(entryDataDict))
    
    """
    * The method to save user selection as well as selection key of a spinner to entryDataDict
    * this will be bined to on_text method of a Spinner object
    """
    def spinnerClicked(self, entryKey, selectedValue):
        entryDataDict[entryKey] = selectedValue
        # print(entryDataDict)
    
    """
    * The method to save user input inside TextInput box to entryDataDict
    * This will be bined to on_text method of a TextInput object
    * Kwarg seqLen: if it is larger than 0, it means a series of textInputs will be wrapped into a list to assgin to a single key in the entryDataDict
    * Kwarg idxOfCurrentTextIpt represents the index for the current editing textInput inside the list of the series fo textInputs
    """
    def typeInsideTextInput(self, key, value, *, seqLen = 1, idxOfCurrentTextIpt = -1):
        if seqLen > 1:
            if key in entryDataDict:
                """
                * For the id that contains 2version, whose value can be either a LIST or a single STRING,
                * when the entry of this id in entryDataDict trys to show on inFileDetails window,
                * first check if this entry is a list:
                *     If it is, re-update this list[indxOfCurrentTextIpt] while initializing the value of this id in inFileDetails window;
                *     If it is not, convert this entry into a list with a length of arg:seqLen and the first item is the arg:value.   
                """
                if type(entryDataDict[key]) == list:
                    entryDataDict[key][idxOfCurrentTextIpt] = value
                else:
                    entryDataDict[key] = [value if i == 0 else "" for i in range(seqLen) ]
            else:
                entryDataDict[key] = ["" for i in range(seqLen)]
                entryDataDict[key][idxOfCurrentTextIpt] = value
        else:
            entryDataDict[key] = value
        print(entryDataDict["steady_monitor"])