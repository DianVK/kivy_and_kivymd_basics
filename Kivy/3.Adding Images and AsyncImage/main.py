from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class MainApp(App):
    def build(self):
        # img = Image(source='cute.png')
        img = AsyncImage(source='https://www.pngmart.com/files/13/Cute-Rilakkuma-PNG-Photos.png')
        return img


MainApp().run()