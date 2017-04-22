import kivy
kivy.require('1.9.0')

import sys
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import BuilderBase, Builder

from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.audio import SoundLoader # garsam
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.label import Label
import time



class RootWidget(FloatLayout):
    pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MainMenu(Screen):
    pass
class MapMenu(Screen):
    pass
class ResearchMenu(Screen):
    pass
class SettingsMenu(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass

Builder.load_file('main.kv')
class MainApp(App):
    cash = 1000
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")


    def build(self):
        Clock.schedule_interval(self.update, 1)
        return RootWidget()
                                            
    def update(self, dt):
        self.cash = self.cash + 1000
        self.cashStr = 'Money:' + str(self.cash) + "\u20ac"


if __name__ == '__main__':
    MainApp().run()