from customtkinter import *
from PIL import Image
import webbrowser

from login import Login
from home import Home

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

    # Cerrar la ventana de inicio de sesión y abrir la ventana del home del juego
    def close(self, response):
        self.app.destroy()
        home = Home()
        home.runHome(response)

    # Función para iniciar sesión
    def login(self, data):
        login = Login()
        response = login.login(data)
        
        if not response:
            self.errorLabel.configure(
                text="Usuario o contraseña incorrectos",
                text_color=self.COLOR_INVALIDO
            )
            self.username.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
            self.password.configure(
                placeholder_text_color=self.COLOR_TEXTO_INVALIDO,
                border_color=self.COLOR_INVALIDO
            )
        else:
            self.errorLabel.configure(
                text="",
            )
            self.username.configure(
                placeholder_text_color=self.COLOR_VALIDO,
                border_color=self.COLOR_VALIDO
            )
            self.password.configure(
                placeholder_text_color=self.COLOR_VALIDO,
                border_color=self.COLOR_VALIDO
            )

            self.close(response)
        

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
        elif data["password"] == "" or len(data["password"]) < 6:
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
        frameOne = CTkFrame(self.app, width=300, height=600, fg_color=self.COLOR_BARRA_SUPERIOR)
        frameOne.place(x=0, y=0)

        logoImage = CTkImage(
            light_image=Image.open("./assets/images/LogoNegro.png"),
            dark_image=Image.open("./assets/images/LogoBlanco.png"),
            size=(200, 100)
        )

        logoLabel = CTkLabel(
            frameOne,
            image=logoImage,
            text="",
        )

        logoLabel.place(x=50, y=50)

        # Agregar contenido a los marcos
        titleLogin = CTkLabel(
            frameOne,
            text="Iniciar sesión",
            font=("./assets/fonts/DIN Black.ttf", 25),
        )
        titleLogin.place(x=75, y=180)

         # Agregar contenido a los marcos
        self.errorLabel = CTkLabel(
            frameOne,
            text="",
            font=("./assets/fonts/DIN Black.ttf", 14),
        )
        self.errorLabel.place(x=25, y=210)

        self.username = CTkEntry(
            frameOne,
            font=("./assets/fonts/DIN.ttf", 18),
            placeholder_text="Usuario",
            width=250,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR
        )
        self.username.place(x=25, y=240)
        
        self.password = CTkEntry(
            frameOne,
            font=("./assets/fonts/DIN.ttf", 18),
            placeholder_text="Contraseña",
            show="*",
            width=250,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR
        )
        self.password.place(x=25, y=290)

        googleIcon = CTkImage(
            light_image=Image.open("./assets/images/google.png"),
            dark_image=Image.open("./assets/images/google.png"),
            size=(25, 25)
        )

        buttonLoginGoogle = CTkButton(
            frameOne,
            cursor="hand2",
            text="",
            font=("./assets/fonts/DIN.ttf", 18),
            width=250,
            height=40,
            border_color=self.COLOR_BARRA_SUPERIOR,
            fg_color='#fff',
            text_color=self.COLOR_BARRA_SUPERIOR,
            image=googleIcon,
            compound="left",
            hover_color=self.COLOR_MENU_LATERAL,
            command=self.loginWithGoogle
        )

        buttonLoginGoogle.place(x=25, y=340)

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
        self.checkbox.place(x=25, y=390)

        loginIcon = CTkImage(
            light_image=Image.open("./assets/images/loginIconLight.png"),
            dark_image=Image.open("./assets/images/loginIconDark.png"),
            size=(30, 30)
        )

        buttonLogin = CTkButton(
            frameOne,
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

        buttonLogin.place(x=(400/2)-75, y=450)

        # Agregar contenido a los marcos
        self.registerLink = CTkLabel(
            frameOne,
            text="¿No tienes una cuenta? Regístrate",
            font=("./assets/fonts/DIN Black.ttf", 14),
            cursor="hand2",
        )
        self.registerLink.place(x=40, y=560)


    # Crear el segundo marco (derecha)
    def rightFrame(self):
        frameTwo = CTkFrame(self.app,width=500, height=600)
        frameTwo.place(x=300, y=0)

        imageBgRight = CTkImage(
            light_image=Image.open("./assets/images/bgRight.png"),
            dark_image=Image.open("./assets/images/bgRight.png"),
            size=(500, 600)
        )

        logoLabel = CTkLabel(
            frameTwo,
            image=imageBgRight,
            text="",
        )

        logoLabel.place(x=-0, y=0)
    
    # Mostrar la ventana de inicio de sesión
    def showLogin(self):
        self.leftFrame()
        self.rightFrame()
        self.events()

if __name__ == "__main__":
    main = Main()
    main.showLogin()
    main.app.mainloop()