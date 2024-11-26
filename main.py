from customtkinter import *
from PIL import Image
import webbrowser

from login import Login

class Main:
    def __init__(self):
        # URL de la API
        self.webUrl = "http://localhost:3000"

        # Crear la ventana principal
        self.app = CTk()
        self.app.title("Iniciar sesión")
        self.app.geometry("800x600")
        set_appearance_mode("Dark")
        self.app.resizable(False, False)

        # Colors tkinter
        self.COLOR_BARRA_SUPERIOR = "#1f2329"
        self.COLOR_MENU_LATERAL = "#2a3138"
        self.COLOR_CUERPO_PRINCIPAL = "#f1faff"
        self.COLOR_MENU_CURSOR_ENCIMA = "#266b9b"
        self.WHITE = "#ffffff"
        self.BLACK = "#000000";

        # Color de los inputs validos e inválidos
        self.COLOR_VALIDO = "#1565c0"
        self.COLOR_INVALIDO = "#e53935"
        self.COLOR_TEXTO_INVALIDO = "#ef5350"
    
        # Datos de usuario
        self.username = ""
        self.password = ""
        self.checkbox = None
        self.registerLink = None

    def login(self, data):
        login = Login()
        login.login(data)

    # Función para validar datos del formulario
    def dataValidation(self):        
        data = {
            "username": self.username.get(),
            "password": self.password.get(),
            "checkbox": self.checkbox.get()
        }

        if(data["username"] == "" and data["password"] == ""):
            self.username.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
            self.password.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
            return
        elif data["username"] == "":
            self.username.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
            return
        elif data["password"] == "":
            self.password.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
            return
        elif data["username"] != "" and data["password"] != "":
            self.username.configure(
                placeholder_text_color=self.COLOR_VALIDO,
                border_color=self.COLOR_VALIDO
            )
            self.password.configure(
                placeholder_text_color=self.COLOR_VALIDO,
                border_color=self.COLOR_VALIDO
            )

        self.login(data)
        

    # Abrir el navegador con la URL de registro
    def openRegister(self, event=None):
        webbrowser.open(f'{self.webUrl}/singup')
    

    # Enviar formulario con la tecla Enter
    def eventSendForm(self, event=None):
        self.dataValidation()
    

    # Función para iniciar sesión con Google
    def loginWithGoogle(self):
        # Aquí puedes agregar la lógica para iniciar sesión con Google
        # Por ejemplo, abrir una URL de autenticación de Google
        webbrowser.open(f'{self.webUrl}/auth/google')
    
    # Cambiar color del enlace de registro al entrar el cursor
    def on_enter(self, event):
        self.registerLink.configure(text_color=self.COLOR_VALIDO)

    # Cambiar color del enlace de registro al salir el cursor
    def on_leave(self, event):
        self.registerLink.configure(text_color=self.WHITE)


    # Eventos de la aplicación
    def events(self):
        # Vincular el evento click al botón de inicio de sesión        
        self.password.bind("<Return>", self.eventSendForm)

        # Vincular el evento click al enlace de registro
        self.registerLink.bind("<Button-1>", self.openRegister)

        self.registerLink.bind("<Enter>", self.on_enter)
        self.registerLink.bind("<Leave>", self.on_leave)



    # Crear el primer marco (izquierda)
    def leftFrame(self):
        frame_1 = CTkFrame(self.app, width=400, height=600, fg_color=self.COLOR_BARRA_SUPERIOR)
        frame_1.place(x=0, y=0)

        logoImage = CTkImage(
            light_image=Image.open("./assets/images/LogoNegro.png"),
            dark_image=Image.open("./assets/images/LogoBlanco.png"),
            size=(200, 100)
        )

        logoLabel = CTkLabel(
            frame_1,
            image=logoImage,
            text="",
        )

        logoLabel.place(x=100, y=50)

        # Agregar contenido a los marcos
        titleLogin = CTkLabel(
            frame_1,
            text="Iniciar sesión",
            font=("./assets/fonts/DIN Black.ttf", 25),
        )
        titleLogin.place(x=120, y=200)

        self.username = CTkEntry(
            frame_1,
            font=("./assets/fonts/DIN.ttf", 18),
            placeholder_text="Usuario",
            width=300,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR
        )
        self.username.place(x=50, y=240)
        
        self.password = CTkEntry(
            frame_1,
            font=("./assets/fonts/DIN.ttf", 18),
            placeholder_text="Contraseña",
            show="*",
            width=300,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR
        )
        self.password.place(x=50, y=290)

        googleIcon = CTkImage(
            light_image=Image.open("./assets/images/google.png"),
            dark_image=Image.open("./assets/images/google.png"),
            size=(25, 25)
        )

        buttonLoginGoogle = CTkButton(
            frame_1,
            cursor="hand2",
            text="",
            font=("./assets/fonts/DIN.ttf", 18),
            width=300,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR,
            fg_color='#fff',
            text_color=self.COLOR_BARRA_SUPERIOR,
            image=googleIcon,
            compound="left",
            hover_color=self.COLOR_MENU_LATERAL,
            command=self.loginWithGoogle
        )

        buttonLoginGoogle.place(x=50, y=340)

        # Crear un CheckBox
        self.checkbox = CTkCheckBox(
            self.app,
            text="Permanecer conectado",
            font=("Arial", 12),
            corner_radius=5,
            border_width=3,
            bg_color=self.COLOR_BARRA_SUPERIOR,
            border_color=self.COLOR_MENU_LATERAL
        )
        self.checkbox.place(x=50, y=390)

        loginIcon = CTkImage(
            light_image=Image.open("./assets/images/loginIconLight.png"),
            dark_image=Image.open("./assets/images/loginIconDark.png"),
            size=(25, 25)
        )

        buttonLogin = CTkButton(
            frame_1,
            cursor="hand2",
            text="",
            font=("./assets/fonts/DIN.ttf", 18),
            width=50,
            height=50,
            border_color=self.COLOR_BARRA_SUPERIOR,
            corner_radius=10,
            image=loginIcon,
            fg_color=self.COLOR_MENU_LATERAL,
            hover_color=self.COLOR_MENU_CURSOR_ENCIMA,
            command=self.dataValidation
        )

        buttonLogin.place(x=(400/2)-25, y=450)

        # Agregar contenido a los marcos
        self.registerLink = CTkLabel(
            frame_1,
            text="¿No tienes una cuenta? Regístrate",
            font=("./assets/fonts/DIN Black.ttf", 14),
            cursor="hand2",
        )
        self.registerLink.place(x=80, y=560)
    
    # Crear el segundo marco (derecha)
    def rightFrame(self):
        frameTwo = CTkFrame(self.app,width=400, height=600)
        frameTwo.place(x=400, y=0)

        imageBg = CTkImage(
            light_image=Image.open("./assets/images/bg.png"),
            dark_image=Image.open("./assets/images/bg.png"),
            size=(1366, 720)
        )

        logoLabel = CTkLabel(
            frameTwo,
            image=imageBg,
            text="",
        )

        logoLabel.place(x=-700, y=0)
    

    def showLogin(self):
        self.leftFrame()
        self.rightFrame()
        self.events()


main = Main()
main.showLogin()
main.app.mainloop()