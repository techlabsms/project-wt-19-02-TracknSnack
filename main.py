from kivy.app import App
from menus.kivy_control import *
from kivy.uix.screenmanager import Screen, ScreenManager
from  kivy.clock import Clock
from kivy.core.window import Window
#Window.clearcolor = (1, 1, 1, 1)




class ScreenManagement(ScreenManager):
    def __init__(self):
        super().__init__()
        self.add_widget(Intro())
        self.add_widget(InputProcessingMenu())
        self.add_widget(InputMenu())
        self.add_widget(Loading())
        self.current = 'intro'
        Clock.schedule_once(self.go_input, 10)

    def go_input(self,_):
        self.current = 'input'


class TracknSnack(App):
    def build(self):

        return ScreenManagement()


if __name__ == '__main__':
    TracknSnack().run()
