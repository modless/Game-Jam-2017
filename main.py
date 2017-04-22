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
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty
from kivy.uix.label import Label
import time

getcontext().prec = 1

class RootWidget(FloatLayout):
    pass

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class MainApp(App):
    cash = 100000
    #widget = ResearchScreen(RootWidget)
    connlvl = 1
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")
    income = NumericProperty(0)
    date = 0
    modifier = NumericProperty(1)
    dateStr = StringProperty()
    connStr = StringProperty('connectionsScreen')
    boolOFF = BooleanProperty(False)
    ##########################
    #   Product Object List  #
    ##########################
    #Product(1000, 0)
    #Shrooms = Product(2000, 15, 0)
    #Heroin = Product(5000, 50, 0)
    #Stomachs = Product(7000, 75, 0)
    Products = DictProperty({
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
    })

    marijuanaString = StringProperty('Marijuana: 0')
    shroomsString = StringProperty('Shrooms: 0')
    heroinString = StringProperty('Heroin: 0')
    stomachsString = StringProperty('Stomachs: 0')
    map_x = 0
    map_y = 0



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
            #widget = ResearchScreen()
            self.cash -= cost
            self.modifier += up
            self.boolOFF = True

    def getProduct(self, identifier):
        if self.Products[identifier]["cost"] <= self.cash:
            self.cash -= self.Products[identifier]["cost"]
            self.Products[identifier]["quantity"] += 1
            self.marijuanaString = 'Marijuana: ' + str(self.Products['Marijuana']['quantity'])
            self.shroomsString = 'Marijuana: ' + str(self.Products['Shrooms']['quantity'])
            self.heroinString = 'Marijuana: ' + str(self.Products['Heroin']['quantity'])
            self.stomachString = 'Marijuana: ' + str(self.Products['Stomachs']['quantity'])











if __name__ == '__main__':
    MainApp().run()