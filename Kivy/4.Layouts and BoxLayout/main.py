from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=20,padding=80)
        img = Image(source='cute.png')
        button = Button(text='Login',size_hint=(None,None),width=100,height=50,pos_hint={'center_x': 0.5})
        layout.add_widget(img)
        layout.add_widget(button)

        return layout


MainApp().run()