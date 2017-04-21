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
from kivy.core.audio import SoundLoader # garsam
from kivy.uix.screenmanager import ScreenManager, Screen # ekranam

map = Image(source='map.png')

cliclSound = SoundLoader.load('Untitled 2.wav') # uzloadinam click garsa
screenMng = ScreenManager() # screen manageris

screenMng.add_widget(MapScreen(name='mapScreen'))
screenMng.add_widget(StationsScreen(name='stationsScreen'))

class MapScreen(Screen):
    pass
class StationsScreen(Screen):
    pass


class RootWidget(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()