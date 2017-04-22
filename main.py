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
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label
import time

class RootWidget(FloatLayout):
    pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class MainApp(App):
    cash = 100000
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")
    income = NumericProperty(0)

    ##########################
    #   Product Object List  #
    ##########################
    #Product(1000, 0)
    #Shrooms = Product(2000, 15, 0)
    #Heroin = Product(5000, 50, 0)
    #Stomachs = Product(7000, 75, 0)
    Products = {
        "Marijuana": {
            "cost": 1000,
            "quantity": 0,
        },
        "Shrooms": {
            "cost": 2000,
            "quantity": 0
        },
        "Heroin": {
            "cost": 5000,
            "quantity": 0
        },
        "Stomachs": {
            "cost": 7000,
            "quantity": 0
        }
    }



    def build(self):
        Clock.schedule_interval(self.update, 1)
        return RootWidget()
                                            
    def update(self, dt):
        self.cash += self.income
        self.cashStr = 'Money:' + str(self.cash) + "\u20ac"

    def getProduct(self, identifier):
        if self.Products[identifier]["cost"] <= self.cash:
            self.cash -= self.Products[identifier]["cost"]
            self.Products[identifier]["quantity"] += 1











if __name__ == '__main__':
    MainApp().run()