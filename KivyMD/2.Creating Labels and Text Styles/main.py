from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello world',halign='center',theme_text_color='Custom',
                        text_color=(255/255.0,70/255.0,79/255.0,1),
                        font_style='Caption')
        icon_label = MDIcon(icon='facebook',
                            halign='center')
        return icon_label


DemoApp().run()