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
from kivy.uix.modalview import ModalView
from kivy.uix.gridlayout import GridLayout
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
    cashlog = []
    cashlog.append('Hello\n')
    #widget = ResearchScreen(RootWidget)
    connlvl = 1
    cashStr = StringProperty("'Money:' + str(self.cash) + '\u20ac'")
    income = NumericProperty(0)
    date = 0
    modifier = NumericProperty(1)
    dateStr = StringProperty()
    connStr = StringProperty('connectionsScreen')
    boolOFF = BooleanProperty(False)
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
        "Cocaine": {
            "cost": 2500,
            "quantity": 0
        },
        "LSD": {
            "cost": 3000,
            "quantity": 0
        },
        "Ecstasy": {
            "cost": 3500,
            "quantity": 0
        },
        "Ketamine": {
            "cost": 6000,
            "quantity": 0
        },
        "Amphetamine": {
            "cost": 7000,
            "quantity": 0
        },
        "Crack": {
            "cost": 1500,
            "quantity": 0
        },
        "Stomachs": {
            "cost": 7000,
            "quantity": 0
        },
        "Kidneys": {
            "cost": 26000,
            "quantity": 0
        },
        "Hearts": {
            "cost": 14000,
            "quantity": 0
        },
        "Livers": {
            "cost": 10000,
            "quantity": 0
        },
        "Spleens": {
            "cost": 6000,
            "quantity": 0
        },
        "Small Intestines": {
            "cost": 26000,
            "quantity": 0
        },
        "Skulls with Teeth": {
            "cost": 5000,
            "quantity": 0
        },
        "Pairs of Eyeballs": {
            "cost": 4000,
            "quantity": 0
        },
        "Shoulders": {
            "cost": 3000,
            "quantity": 0
        }
    })

    marijuanaString = StringProperty('Marijuana: 0')
    shroomsString = StringProperty('Shrooms: 0')
    heroinString = StringProperty('Heroin: 0')
    cocaineString = StringProperty('Cocaine: 0')
    LSDString = StringProperty('LSD: 0')
    ecstasyString = StringProperty('Ecstasy: 0')
    ketamineString = StringProperty('Ketamine: 0')
    amphetamineString = StringProperty('Amphetamine: 0')
    crackString = StringProperty('Crack: 0')
    stomachsString = StringProperty('Stomachs: 0')
    kidneysString = StringProperty('Kidneys: 0')
    heartsString = StringProperty('Hearts: 0')
    liversString = StringProperty('Livers: 0')
    spleensString = StringProperty('Spleens: 0')
    smallIntestinesString = StringProperty('Small Intestines: 0')
    skullsWithTeethString = StringProperty('Skulls with Teeth: 0')
    pairsOfEyeballsString = StringProperty('Pairs of Eyeballs: 0')
    shouldersString = StringProperty('Shoulders: 0')

    map_x = 0
    map_y = 0



    cashlogSTR = StringProperty('cashlogSTR: 0')
    def build(self):
        Clock.schedule_interval(self.update, 1)
        return RootWidget()

    def update(self, dt):
        self.cash += self.income*self.modifier
        self.cashStr = 'Money:' + str(self.cash) + "\u20ac"
        self.date += 1
        self.dateStr = str(Decimal(self.date)/Decimal(24)) + "Days"
        self.cashlogSTR = self.getstringfromarray(self.cashlog)
    def getstringfromarray(self, array):
        return ''.join(array)
    def upgradeConn(self, lvl,cost,devSPD,orderSPD):
        if lvl==2:
            if cost <= self.cash:
                self.cash -= cost
                self.connStr = 'connections2Screen'
                self.cashlog.append(self.dateStr + ": minus " + str(cost) + " euros\n")
                print(''.join(self.cashlog))
        elif lvl==3:
            if cost <= self.cash:
                self.cash -= cost
                self.connStr = 'connections3Screen'
                self.cashlog.append(self.dateStr + ": minus " + str(cost) + " euros\n")
    def ModDisable(self,up,cost):
        if cost <= self.cash:
            self.cash -= cost
            self.modifier += up
            self.boolOFF = True
            self.cashlog.append(self.dateStr + ": minus " + str(cost) + " euros\n")

    def getProduct(self, identifier):
        if self.Products[identifier]["cost"] <= self.cash:
            self.cash -= self.Products[identifier]["cost"]
            self.Products[identifier]["quantity"] += 1
            self.marijuanaString = 'Marijuana: ' + str(self.Products['Marijuana']['quantity'])
            self.shroomsString = 'Shrooms: ' + str(self.Products['Shrooms']['quantity'])
            self.cocaineString = 'Cocaine: ' + str(self.Products['Cocaine']['quantity'])
            self.LSDString = 'LSD: ' + str(self.Products['LSD']['quantity'])
            self.ecstasyString = 'Ecstasy: ' + str(self.Products['Ecstasy']['quantity'])
            self.ketamineString = 'Ketamine: ' + str(self.Products['Ketamine']['quantity'])
            self.amphetamineString = 'Amphetamine: ' + str(self.Products['Amphetamine']['quantity'])
            self.crackString = 'Crack: ' + str(self.Products['Crack']['quantity'])
            self.heroinString = 'Heroin: ' + str(self.Products['Heroin']['quantity'])
            self.stomachsString = 'Stomachs: ' + str(self.Products['Stomachs']['quantity'])
            self.kidneysString = 'Kidneys: ' + str(self.Products['Kidneys']['quantity'])
            self.heartsString = 'Hearts: ' + str(self.Products['Hearts']['quantity'])
            self.liversString = 'Livers: ' + str(self.Products['Livers']['quantity'])
            self.spleensString = 'Spleens: ' + str(self.Products['Spleens']['quantity'])
            self.smallIntestinesString = 'Small Intestines: ' + str(self.Products['Small Intestines']['quantity'])
            self.skullsWithTeethString = 'Skulls with Teeth: ' + str(self.Products['Skulls with Teeth']['quantity'])
            self.pairsOfEyeballsString = 'Pairs of Eyeballs: ' + str(self.Products['Pairs of Eyeballs']['quantity'])
            self.shouldersString = 'Shoulders: ' + str(self.Products['Shoulders']['quantity'])











if __name__ == '__main__':
    MainApp().run()