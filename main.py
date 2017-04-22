import kivy
kivy.require('1.9.0')

import sys
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import BuilderBase, Builder

from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.image import Image
from kivy.uix.button import *
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.audio import SoundLoader # garsam
from kivy.clock import Clock
from functools import partial
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
    cash = 10000
    widget = ResearchScreen(RootWidget)
    connlvl = 1
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")
    income = NumericProperty(0)
    date = 0
    modifier = NumericProperty(1)
    dateStr = StringProperty()
    connStr = StringProperty('connectionScreen')

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
        self.cash += self.income*self.modifier
        self.cashStr = 'Money:' + str(self.cash) + "\u20ac"
        self.date += 1
        self.dateStr = str(Decimal(self.date)/Decimal(24)) + "Days"

    def upgradeConn(self, lvl,cost,devSPD,orderSPD):
        if lvl==2:
            if cost <= self.cash:
                self.cash -= cost
                self.connStr = 'connections2Screen'
        elif lvl==3:
            if cost <= self.cash:
                self.cash -= cost
                self.connStr = 'connections3Screen'
    def ModDisable(self,up,cost):
        if cost <= self.cash:
            widget = ResearchScreen()
            self.cash -= cost
            self.modifier += up
            remove_widget(widget.ids['OP2-1'].ids)

    def getProduct(self, identifier):
        if self.Products[identifier]["cost"] <= self.cash:
            self.cash -= self.Products[identifier]["cost"]
            self.Products[identifier]["quantity"] += 1











if __name__ == '__main__':
    MainApp().run()