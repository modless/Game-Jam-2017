import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.graphics.svg import Svg
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

sound = SoundLoader.load('Untitled 2.wav')

class RootWidget(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()