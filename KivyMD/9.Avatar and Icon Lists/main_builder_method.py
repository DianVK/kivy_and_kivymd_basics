from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container

"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(20):
            items = OneLineAvatarListItem(
                ImageLeftWidget(
                    source="full_image.png"
                ),
                text="Single-line item with avatar")
            self.root.ids.container.add_widget(items)

DemoApp().run()
