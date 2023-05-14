
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import*
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window



class Mainlayout(GridLayout):

    
    #take input text in this variable
    update_text=StringProperty("")
    name=StringProperty("")
    
    def button_click(self):
        name=self.ids.name_input.text
        line_dirrect=self.ids.read_text.text
        line=line_dirrect.lower()
        #specific words which will be matched with line(Textinput)
        symptm_1="inappropriate laughing and giggling"
        symptm_2="no sensitivity of pain"
        symptm_3="not able to make eye contact properly"
        symptm_4="no proper response to sound"
        symptm_5="may not have a wish for cuddling"
        symptm_6="not able to express their gestures"
        symptm_7="no interaction with others"
        symptm_8="inappropriate objects attachment"
        symptm_9="want to live alone"
        symptm_10="echo words"
        if symptm_1 in line or symptm_2 in line or symptm_3 in line or symptm_4 in line or symptm_5 in line or symptm_6 in line or symptm_7 in line or symptm_8 in line or symptm_9 in line or symptm_10 in line:
            
            self.update_text=(f"Unfortunately, your child {name.title()} has Autism")
                
        else:
            self.update_text=(f"Your child {name.title()} is normal")

    def clear_text(self):

        #self.ids.answer.text=""
        self.update_text=""
        self.ids.read_text.text=""
        self.ids.name_input.text=""
        self.ids.age_input.text=""
        self.ids.gender_input.text=""
        self.ids.region_input.text=""

        def on_keyboard(self, instance, keycode, scancode, codepoint, modifier):
            if keycode == 40:  # Enter key
                self.on_submit(None)

    def update_window(self, focus):
        if focus:
            Window.softinput_mode = 'pan'
        else:
            Window.softinput_mode = 'resize'

        

class Autisom(App):
    def build(se1f):
        
        return Mainlayout()


Autisom().run()

