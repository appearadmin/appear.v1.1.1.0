from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.utils import platform
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import time

cred = credentials.Certificate('appear.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
curr_dat = datetime.date.today()
curr_tim = time.time()

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class StudentScreen1(Screen):
    concerns = []
    role = "student"
    fname = []
    yrsc = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.float = Builder.load_file("background.kv")
        self.add_widget(self.float)

        self.float.full_name = Builder.load_file("textfields.kv")
        self.float.yearsec = Builder.load_file("textfields.kv")
        self.float.add_widget(self.float.full_name)
        self.float.add_widget(self.float.yearsec)

        self.float.full_name.hint_text = "Full Name"
        self.float.full_name.pos_hint = {"center_x" : .5, "center_y" : .875}
        self.float.yearsec.hint_text = "Year&Section"
        self.float.yearsec.pos_hint = {"center_x" : .5, "center_y" : .80}

        self.float.grid = GridLayout(cols=2, row_force_default=True, row_default_height=50, pos_hint={"center_x" : .4, "center_y" : .250})
        self.float.add_widget(self.float.grid)

        self.float.grid.checkb1 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb2 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb3 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb4 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb5 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb6 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb7 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb8 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb9 = Builder.load_file("checkbox.kv")

        self.float.grid.cblabel1 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel2 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel3 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel4 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel5 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel6 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel7 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel8 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel9 = Builder.load_file("cblabel.kv")

        self.float.grid.add_widget(self.float.grid.checkb1)
        self.float.grid.add_widget(self.float.grid.cblabel1)
        self.float.grid.add_widget(self.float.grid.checkb2)
        self.float.grid.add_widget(self.float.grid.cblabel2)
        self.float.grid.add_widget(self.float.grid.checkb3)
        self.float.grid.add_widget(self.float.grid.cblabel3)
        self.float.grid.add_widget(self.float.grid.checkb4)
        self.float.grid.add_widget(self.float.grid.cblabel4)
        self.float.grid.add_widget(self.float.grid.checkb5)
        self.float.grid.add_widget(self.float.grid.cblabel5)
        self.float.grid.add_widget(self.float.grid.checkb6)
        self.float.grid.add_widget(self.float.grid.cblabel6)
        self.float.grid.add_widget(self.float.grid.checkb7)
        self.float.grid.add_widget(self.float.grid.cblabel7)
        self.float.grid.add_widget(self.float.grid.checkb8)
        self.float.grid.add_widget(self.float.grid.cblabel8)
        self.float.grid.add_widget(self.float.grid.checkb9)
        self.float.grid.add_widget(self.float.grid.cblabel9)

        self.float.grid.cblabel1.text = "Bathroom Smell"
        self.float.grid.cblabel2.text = "Cleanliness of the CR"
        self.float.grid.cblabel3.text = "Mosquitoes"
        self.float.grid.cblabel4.text = "Smoke"
        self.float.grid.cblabel5.text = "Mud after rain"
        self.float.grid.cblabel6.text = "Scattered Garbage"
        self.float.grid.cblabel7.text = "Lack of running water in restrooms"
        self.float.grid.cblabel8.text = "Broken lights and doors in restroom"
        self.float.grid.cblabel9.text = "Broken Chairs"
        
        self.float.grid.checkb1.bind(active=self.on_checkbox1)
        self.float.grid.checkb2.bind(active=self.on_checkbox2)
        self.float.grid.checkb3.bind(active=self.on_checkbox3)
        self.float.grid.checkb4.bind(active=self.on_checkbox4)
        self.float.grid.checkb5.bind(active=self.on_checkbox5)
        self.float.grid.checkb6.bind(active=self.on_checkbox6)
        self.float.grid.checkb7.bind(active=self.on_checkbox7)
        self.float.grid.checkb8.bind(active=self.on_checkbox8)
        self.float.grid.checkb9.bind(active=self.on_checkbox9)

    def on_checkbox1(self, inst, value):
        if value == True:
            self.concerns.append("1")
        else:
            self.concerns.remove("1")

    def on_checkbox2(self, inst, value):
        if value == True:
            self.concerns.append("2")
        else:
            self.concerns.remove("2")
    
    def on_checkbox3(self, inst, value):
        if value == True:
            self.concerns.append("3")
        else:
            self.concerns.remove("3")
    
    def on_checkbox4(self, inst, value):
        if value == True:
            self.concerns.append("4")
        else:
            self.concerns.remove("4")

    def on_checkbox5(self, inst, value):
        if value == True:
            self.concerns.append("5")
        else:
            self.concerns.remove("5")

    def on_checkbox6(self, inst, value):
        if value == True:
            self.concerns.append("6")
        else:
            self.concerns.remove("6")

    def on_checkbox7(self, inst, value):
        if value == True:
            self.concerns.append("7")
        else:
            self.concerns.remove("7")
    def on_checkbox8(self, inst, value):
        if value == True:
            self.concerns.append("8")
        else:
            self.concerns.remove("8")
    def on_checkbox9(self, inst, value):
        if value == True:
            self.concerns.append("9")
        else:
            self.concerns.remove("9")
    
    def set_var(self, inst):
        self.fname.append(self.float.full_name.text)
        self.yrsc.append(self.float.yearsec.text)

class StudentScreen2(Screen):
    role = "student"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.float = Builder.load_file("background.kv")
        self.add_widget(self.float)

        self.float.grid = GridLayout(cols=2, row_force_default=True, row_default_height=50, pos_hint={"center_x" : .4, "center_y" : .350})
        self.float.add_widget(self.float.grid)

        self.float.grid.checkb10 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb11 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb12 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb13 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb14 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb15 = Builder.load_file("checkbox.kv")

        self.float.grid.cblabel10 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel11 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel12 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel13 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel14 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel15 = Builder.load_file("cblabel.kv")

        self.float.grid.add_widget(self.float.grid.checkb10)
        self.float.grid.add_widget(self.float.grid.cblabel10)
        self.float.grid.add_widget(self.float.grid.checkb11)
        self.float.grid.add_widget(self.float.grid.cblabel11)
        self.float.grid.add_widget(self.float.grid.checkb12)
        self.float.grid.add_widget(self.float.grid.cblabel12)
        self.float.grid.add_widget(self.float.grid.checkb13)
        self.float.grid.add_widget(self.float.grid.cblabel13)
        self.float.grid.add_widget(self.float.grid.checkb14)
        self.float.grid.add_widget(self.float.grid.cblabel14)
        self.float.grid.add_widget(self.float.grid.checkb15)
        self.float.grid.add_widget(self.float.grid.cblabel15)

        self.float.grid.cblabel10.text = "Water Cleanliness"
        self.float.grid.cblabel11.text = "Fallen leaves"
        self.float.grid.cblabel12.text = "Robbers"
        self.float.grid.cblabel13.text = "CR Maintenance"
        self.float.grid.cblabel14.text = "Proper Garbage Disposal"
        self.float.grid.cblabel15.text = "Dirty Hallway and Rooms"

        self.float.grid.checkb10.bind(active=self.on_checkbox10)
        self.float.grid.checkb11.bind(active=self.on_checkbox11)
        self.float.grid.checkb12.bind(active=self.on_checkbox12)
        self.float.grid.checkb13.bind(active=self.on_checkbox13)
        self.float.grid.checkb14.bind(active=self.on_checkbox14)
        self.float.grid.checkb15.bind(active=self.on_checkbox15)

        self.float.other = Builder.load_file("othercomp.kv")
        self.float.add_widget(self.float.other)

    def on_checkbox10(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("10")
        else:
            StudentScreen1.concerns.remove("10")

    def on_checkbox11(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("11")
        else:
            StudentScreen1.concerns.remove("11")

    def on_checkbox12(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("12")
        else:
            StudentScreen1.concerns.remove("12")

    def on_checkbox13(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("13")
        else:
            StudentScreen1.concerns.remove("13")
    
    def on_checkbox14(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("14")
        else:
            StudentScreen1.concerns.remove("14")
    
    def on_checkbox15(self, inst, value):
        if value == True:
            StudentScreen1.concerns.append("15")
        else:
            StudentScreen1.concerns.remove("15")

    def submit(self, inst):
        self.timestamp = str(curr_dat) + str(curr_tim)

        doc_ref = db.collection("users").document(self.timestamp)
        doc_ref.set({"fullname": StudentScreen1.fname[0],
                     "yearsec": StudentScreen1.yrsc[0], 
                     "concerns": StudentScreen1.concerns,
                     "other": self.float.other.text,
                     "role": self.role})

class TeacherScreen1(Screen):
    concerns = []
    role = "teacher"
    fname = []
    yrsc = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.float = Builder.load_file("background.kv")
        self.add_widget(self.float)

        self.float.full_name = Builder.load_file("textfields.kv")
        self.float.yearsec = Builder.load_file("textfields.kv")
        self.float.add_widget(self.float.full_name)
        self.float.add_widget(self.float.yearsec)

        self.float.full_name.hint_text = "Full Name"
        self.float.full_name.pos_hint = {"center_x" : .5, "center_y" : .875}
        self.float.yearsec.hint_text = "Year&Section"
        self.float.yearsec.pos_hint = {"center_x" : .5, "center_y" : .80}

        self.float.grid = GridLayout(cols=2, row_force_default=True, row_default_height=50, pos_hint={"center_x" : .4, "center_y" : .250})
        self.float.add_widget(self.float.grid)

        self.float.grid.checkb1 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb2 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb3 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb4 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb5 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb6 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb7 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb8 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb9 = Builder.load_file("checkbox.kv")

        self.float.grid.cblabel1 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel2 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel3 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel4 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel5 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel6 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel7 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel8 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel9 = Builder.load_file("cblabel.kv")

        self.float.grid.add_widget(self.float.grid.checkb1)
        self.float.grid.add_widget(self.float.grid.cblabel1)
        self.float.grid.add_widget(self.float.grid.checkb2)
        self.float.grid.add_widget(self.float.grid.cblabel2)
        self.float.grid.add_widget(self.float.grid.checkb3)
        self.float.grid.add_widget(self.float.grid.cblabel3)
        self.float.grid.add_widget(self.float.grid.checkb4)
        self.float.grid.add_widget(self.float.grid.cblabel4)
        self.float.grid.add_widget(self.float.grid.checkb5)
        self.float.grid.add_widget(self.float.grid.cblabel5)
        self.float.grid.add_widget(self.float.grid.checkb6)
        self.float.grid.add_widget(self.float.grid.cblabel6)
        self.float.grid.add_widget(self.float.grid.checkb7)
        self.float.grid.add_widget(self.float.grid.cblabel7)
        self.float.grid.add_widget(self.float.grid.checkb8)
        self.float.grid.add_widget(self.float.grid.cblabel8)
        self.float.grid.add_widget(self.float.grid.checkb9)
        self.float.grid.add_widget(self.float.grid.cblabel9)

        self.float.grid.cblabel1.text = "Bathroom Smell"
        self.float.grid.cblabel2.text = "Cleanliness of the CR"
        self.float.grid.cblabel3.text = "Mosquitoes"
        self.float.grid.cblabel4.text = "Smoke"
        self.float.grid.cblabel5.text = "Mud after rain"
        self.float.grid.cblabel6.text = "Scattered Garbage"
        self.float.grid.cblabel7.text = "Lack of running water in restrooms"
        self.float.grid.cblabel8.text = "Broken lights and doors in restroom"
        self.float.grid.cblabel9.text = "Broken Chairs"
        
        self.float.grid.checkb1.bind(active=self.on_checkbox1)
        self.float.grid.checkb2.bind(active=self.on_checkbox2)
        self.float.grid.checkb3.bind(active=self.on_checkbox3)
        self.float.grid.checkb4.bind(active=self.on_checkbox4)
        self.float.grid.checkb5.bind(active=self.on_checkbox5)
        self.float.grid.checkb6.bind(active=self.on_checkbox6)
        self.float.grid.checkb7.bind(active=self.on_checkbox7)
        self.float.grid.checkb8.bind(active=self.on_checkbox8)
        self.float.grid.checkb9.bind(active=self.on_checkbox9)

    def on_checkbox1(self, inst, value):
        if value == True:
            self.concerns.append("1")
        else:
            self.concerns.remove("1")

    def on_checkbox2(self, inst, value):
        if value == True:
            self.concerns.append("2")
        else:
            self.concerns.remove("2")
    
    def on_checkbox3(self, inst, value):
        if value == True:
            self.concerns.append("3")
        else:
            self.concerns.remove("3")
    
    def on_checkbox4(self, inst, value):
        if value == True:
            self.concerns.append("4")
        else:
            self.concerns.remove("4")

    def on_checkbox5(self, inst, value):
        if value == True:
            self.concerns.append("5")
        else:
            self.concerns.remove("5")

    def on_checkbox6(self, inst, value):
        if value == True:
            self.concerns.append("6")
        else:
            self.concerns.remove("6")

    def on_checkbox7(self, inst, value):
        if value == True:
            self.concerns.append("7")
        else:
            self.concerns.remove("7")
    def on_checkbox8(self, inst, value):
        if value == True:
            self.concerns.append("8")
        else:
            self.concerns.remove("8")
    def on_checkbox9(self, inst, value):
        if value == True:
            self.concerns.append("9")
        else:
            self.concerns.remove("9")
    
    def set_var(self, inst):
        self.fname.append(self.float.full_name.text)
        self.yrsc.append(self.float.yearsec.text)

class TeacherScreen2(Screen):
    role = "teacher"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.float = Builder.load_file("background.kv")
        self.add_widget(self.float)

        self.float.grid = GridLayout(cols=2, row_force_default=True, row_default_height=50, pos_hint={"center_x" : .4, "center_y" : .350})
        self.float.add_widget(self.float.grid)

        self.float.grid.checkb10 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb11 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb12 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb13 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb14 = Builder.load_file("checkbox.kv")
        self.float.grid.checkb15 = Builder.load_file("checkbox.kv")

        self.float.grid.cblabel10 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel11 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel12 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel13 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel14 = Builder.load_file("cblabel.kv")
        self.float.grid.cblabel15 = Builder.load_file("cblabel.kv")

        self.float.grid.add_widget(self.float.grid.checkb10)
        self.float.grid.add_widget(self.float.grid.cblabel10)
        self.float.grid.add_widget(self.float.grid.checkb11)
        self.float.grid.add_widget(self.float.grid.cblabel11)
        self.float.grid.add_widget(self.float.grid.checkb12)
        self.float.grid.add_widget(self.float.grid.cblabel12)
        self.float.grid.add_widget(self.float.grid.checkb13)
        self.float.grid.add_widget(self.float.grid.cblabel13)
        self.float.grid.add_widget(self.float.grid.checkb14)
        self.float.grid.add_widget(self.float.grid.cblabel14)
        self.float.grid.add_widget(self.float.grid.checkb15)
        self.float.grid.add_widget(self.float.grid.cblabel15)

        self.float.grid.cblabel10.text = "Water Cleanliness"
        self.float.grid.cblabel11.text = "Fallen leaves"
        self.float.grid.cblabel12.text = "Robberes"
        self.float.grid.cblabel13.text = "CR Maintenance"
        self.float.grid.cblabel14.text = "Proper Garbage Disposal"
        self.float.grid.cblabel15.text = "Dirty Hallway and Rooms"

        self.float.grid.checkb10.bind(active=self.on_checkbox10)
        self.float.grid.checkb11.bind(active=self.on_checkbox11)
        self.float.grid.checkb12.bind(active=self.on_checkbox12)
        self.float.grid.checkb13.bind(active=self.on_checkbox13)
        self.float.grid.checkb14.bind(active=self.on_checkbox14)
        self.float.grid.checkb15.bind(active=self.on_checkbox15)

        self.float.other = Builder.load_file("othercomp.kv")
        self.float.add_widget(self.float.other)

    def on_checkbox10(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("10")
        else:
            TeacherScreen1.concerns.remove("10")

    def on_checkbox11(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("11")
        else:
            TeacherScreen1.concerns.remove("11")

    def on_checkbox12(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("12")
        else:
            TeacherScreen1.concerns.remove("12")

    def on_checkbox13(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("13")
        else:
            TeacherScreen1.concerns.remove("13")
    
    def on_checkbox14(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("14")
        else:
            TeacherScreen1.concerns.remove("14")
    
    def on_checkbox15(self, inst, value):
        if value == True:
            TeacherScreen1.concerns.append("15")
        else:
            TeacherScreen1.concerns.remove("15")

    def submit(self, inst):
        self.timestamp = str(curr_dat) + str(curr_tim)

        doc_ref = db.collection("users").document(self.timestamp)
        doc_ref.set({"fullname": TeacherScreen1.fname[0],
                     "yearsec": TeacherScreen1.yrsc[0], 
                     "concerns": TeacherScreen1.concerns,
                     "other": self.float.other.text,
                     "role": self.role})
        
class LastScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_exit(self):
        appfloat().stop()

class appfloat(MDApp):
    def build(self):
        if(platform == 'android'):
            Window.maximize()
        if(platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (350, 600)
        
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = "Light"

        screen = Builder.load_file("screens.kv")

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(StudentScreen1(name="student1"))
        sm.add_widget(StudentScreen2(name="student2"))
        sm.add_widget(TeacherScreen1(name="teacher1"))
        sm.add_widget(TeacherScreen2(name="teacher2"))
        sm.add_widget(LastScreen(name="last"))

        return screen
        
if __name__ == "__main__":
    appfloat().run()