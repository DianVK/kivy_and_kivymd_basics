from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

KV = '''
<MyOneLineIconListItem>:
    text: root.text
    IconLeftWidget:
        icon: "trash-can-outline"
        on_release: root.schedule_trash() 

MDBoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: 'Press icon to delete'
        halign: 'center'
        size_hint_y: None
        height: dp(24)
    ScrollView:

        MDList:
            id: container
'''


class MyOneLineIconListItem(OneLineIconListItem):
    text = StringProperty()

    def schedule_trash(self):  # adds a delay to allow the animation to complete.
        Clock.schedule_once(self.trash, .5)

    def trash(self, dt):
        app = MDApp.get_running_app()
        app.root.ids.container.remove_widget(self)


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(MyOneLineIconListItem(text=f"Single-line item {i}"))


Test().run()