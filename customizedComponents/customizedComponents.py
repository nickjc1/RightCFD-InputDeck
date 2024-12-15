from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import SpinnerOption

from kivy.lang.builder import Builder


Builder.load_file("./customizedComponents/customizedComponents.kv")

class MyButton(Button):
    pass

class BlackLabel(Label):
    pass

class CustomizedSpinnerOption(SpinnerOption):
    pass