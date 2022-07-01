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


# This is the main GeoGuessr App/Frame, launched via gg, to contains navigation to sub frames.
class GeoGuessr(App):

    def build(self):
        # return GeoGuessry Main Page.
        global sm 
        sm = ScreenManager()
        Builder.load_file("widgets/homescreen.kv")
        sm.add_widget(HomeScreen(name="menu"))
        #sm.add_widget(Builder.load_file("widgets/playscreen.kv"))
        #sm.add_wdget(Builder.load_file("widgets/highscore.kv"))
        return sm


if __name__ == '__main__':
    gg = GeoGuessr()
    gg.run()
