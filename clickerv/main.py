from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        buttons = [
            ("Screen 1", "screen1"),
            ("Screen 2", "screen2"),
            ("Screen 3", "screen3"),
            ("Screen 4", "screen4"),
            ("Exit", "exit")  # Додана кнопка "Exit"
        ]
        for text, screen_name in buttons:
            button = Button(text=text)
            if screen_name == "exit":  # Перевірка для кнопки Exit
                button.bind(on_press=self.exit_app)
            else:
                button.bind(on_press=lambda instance, screen_name=screen_name: self.switch_screen(screen_name))
            layout.add_widget(button)
        self.add_widget(layout)

    def switch_screen(self, screen_name):
        self.manager.current = screen_name

    def exit_app(self, instance):  # Метод для завершення роботи програми
        App.get_running_app().stop()


class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        return_button = Button(text="Return to Main")
        return_button.bind(on_press=self.return_to_main)
        label = Label(text="Widget 1")
        text_input = TextInput(hint_text="Enter something")
        layout.add_widget(return_button)
        layout.add_widget(label)
        layout.add_widget(text_input)
        self.add_widget(layout)

    def return_to_main(self, instance):
        self.manager.current = 'main'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        return_button = Button(text="Return to Main")
        return_button.bind(on_press=self.return_to_main)
        label = Label(text="Widget 2")
        text_input = TextInput(hint_text="Enter something")
        layout.add_widget(return_button)
        layout.add_widget(label)
        layout.add_widget(text_input)
        self.add_widget(layout)

    def return_to_main(self, instance):
        self.manager.current = 'main'


class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        return_button = Button(text="Return to Main")
        return_button.bind(on_press=self.return_to_main)
        label = Label(text="Widget 3")
        text_input = TextInput(hint_text="Enter something")
        layout.add_widget(return_button)
        layout.add_widget(label)
        layout.add_widget(text_input)
        self.add_widget(layout)

    def return_to_main(self, instance):
        self.manager.current = 'main'


class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        return_button = Button(text="Return to Main")
        return_button.bind(on_press=self.return_to_main)
        label = Label(text="Widget 4")
        text_input = TextInput(hint_text="Enter something")
        layout.add_widget(return_button)
        layout.add_widget(label)
        layout.add_widget(text_input)
        self.add_widget(layout)

    def return_to_main(self, instance):
        self.manager.current = 'main'


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        return sm


if __name__ == '__main__':
    TestApp().run()
