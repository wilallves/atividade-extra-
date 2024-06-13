from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

Window.size = 360, 640

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(1, 179/255, 235/255, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        
        login_label = Label(text='Login', size_hint=(1, None), height=40)
        layout.add_widget(login_label)
        
        self.email_input = TextInput(hint_text='Email', size_hint=(1, None), height=40)
        self.password_input = TextInput(hint_text='Senha', password=True, size_hint=(1, None), height=40)
        
        login_button = Button(text='Login', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        login_button.bind(on_press=self.goto_page_two)  
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        
        register_button = Button(text='Cadastro', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        register_button.bind(on_press=self.goto_register)
        layout.add_widget(register_button)
        
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def goto_register(self, instance):
        self.manager.current = 'register'
    
    def goto_page_two(self, instance):
        self.manager.current = 'page_two'

class PageTwoScreen(Screen):  
    def __init__(self, **kwargs):
        super(PageTwoScreen, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(1, 179/255, 235/255, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        
        email_label = Label(text='E-mail', size_hint=(1, None), height=40)
        layout.add_widget(email_label)
        
        self.email_input = TextInput(hint_text='Insira seu e-mail', size_hint=(1, None), height=40)
        layout.add_widget(self.email_input)
        
        password_label = Label(text='Senha', size_hint=(1, None), height=40)
        layout.add_widget(password_label)
        
        self.password_input = TextInput(hint_text='Insira sua senha', password=True, size_hint=(1, None), height=40)
        layout.add_widget(self.password_input)
        
        enter_button = Button(text='Entrar', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        enter_button.bind(on_press=self.goto_login)
        layout.add_widget(enter_button)
        
        back_button = Button(text='Voltar', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        back_button.bind(on_press=self.goto_login)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def goto_login(self, instance):
        self.manager.current = 'login'

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(1, 179/255, 235/255, 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        
        email_label = Label(text='E-mail', size_hint=(1, None), height=40)
        layout.add_widget(email_label)
        
        self.email_input = TextInput(hint_text='Insira seu e-mail', size_hint=(1, None), height=40)
        layout.add_widget(self.email_input)
        
        password_label = Label(text='Senha', size_hint=(1, None), height=40)
        layout.add_widget(password_label)
        
        self.password_input = TextInput(hint_text='Insira sua senha', password=True, size_hint=(1, None), height=40)
        layout.add_widget(self.password_input)
        
        register_button = Button(text='Cadastrar', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        register_button.bind(on_press=self.register)
        layout.add_widget(register_button)
        
        back_button = Button(text='Voltar', size_hint=(1, None), height=40, background_color=(240/255, 47/255, 189/255, 1))
        back_button.bind(on_press=self.goto_login)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def register(self, instance):
        print("Registrando...")
        print("E-mail:", self.email_input.text)
        print("Senha:", self.password_input.text)

class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(PageTwoScreen(name='page_two'))  
        return sm

if __name__ == '__main__':
    LoginApp().run()
