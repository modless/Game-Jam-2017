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
from decimal import getcontext, Decimal
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label
import time

getcontext().prec = 1

class RootWidget(FloatLayout):
    pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Builder.load_file('main.kv')
class MainApp(App):
    cash = 1000
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")
    income = NumericProperty(0)
    date = 0
    dateStr = StringProperty()


    def build(self):
        Clock.schedule_interval(self.update, 1)
        return RootWidget()
                                            
    def update(self, dt):
        self.cash += self.income
        self.cashStr = 'Money:' + str(self.cash) + "\u20ac"
        self.date += 1
        self.dateStr = str(Decimal(self.date)/Decimal(24)) + "Days"


    def incomeUp(self, cost, up):
        if cost <= self.cash:
            self.cash -= cost
            self.income += up



if __name__ == '__main__':
    MainApp().run()