import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os
import random
import time

#Gotta have this, cuz why not?
current_dir = os.path.dirname(os.path.realpath(__file__))

class HomeScreen(Screen):
    pass

class PlayScreen(Screen):
    import google_streetview.api
    params = [{'size':'600x300',
               'location':'46.414382,10.012988',
               'heading':'151.78',
               'pitch':'-0.76',
               'key':'dev_test'}]
    result=google_streetview.api.results(params)
    def say_hi(self):
        print("wow")
    pass

class Instructions(Screen):
    pass

class HighScore(Screen):
    pass

# This is the main GeoGuessr App/Frame, launched via gg, to contains navigation to sub frames.
class GeoGuessr(App):

    def build(self):
        # return GeoGuessry Main Page.
        global sm 
        sm = ScreenManager()
        Builder.load_file("widgets/homescreen.kv")
        Builder.load_file("widgets/playscreen.kv")
        Builder.load_file("widgets/highscore.kv")
        Builder.load_file("widgets/instructions.kv")
        sm.add_widget(HomeScreen(name="menu"))
        sm.add_widget(PlayScreen(name="playscreen"))
        sm.add_widget(Instructions(name="instructions"))
        sm.add_widget(HighScore(name="highscore"))
        return sm


if __name__ == '__main__':
    gg = GeoGuessr()
    gg.run()
