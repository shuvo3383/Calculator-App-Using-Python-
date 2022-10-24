import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
Builder.load_file('calc.kv')


class Demo(GridLayout):
   def btn_press(self,btn):
       self.ids.screen1.text






class CheckBox_App(App):
    def build(self):
        return Demo()


root = CheckBox_App()
root.run()