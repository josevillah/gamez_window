from customtkinter import *

class Login:
    def __init__(self):
        self.app = CTk()
        self.app.title("Iniciar sesión")
        self.app.geometry("800x600")
        set_appearance_mode("dark")

        # Colors tkinter
        self.COLOR_BARRA_SUPERIOR = "#1f2329"
        self.COLOR_MENU_LATERAL = "#2a3138"
        self.COLOR_CUERPO_PRINCIPAL = "#f1faff"
        self.COLOR_MENU_CURSOR_ENCIMA = "#2f88c5"
        self.WHITE = "#ffffff"


    def showLogin(self):
        # Crear el primer marco (izquierda)
        frame_1 = CTkFrame(self.app)
        frame_1.grid(row=0, column=0, sticky="nsew")

        # Crear el segundo marco (derecha)
        frame_2 = CTkFrame(self.app)
        frame_2.grid(row=0, column=1, sticky="nsew")

        # Configurar la grid para que las columnas tengan un tamaño proporcional
        self.app.grid_columnconfigure(0, weight=1)  # Columna 0 (izquierda)
        self.app.grid_columnconfigure(1, weight=2)  # Columna 1 (derecha)

        # Agregar contenido a los marcos
        label_1 = CTkLabel(
            frame_1,
            text="Iniciar sesión",
            font=("./assets/fonts/DIN Black.ttf", 25),
        )
        label_1.place(x=80, y=100)

        username = CTkEntry(
            frame_1,
            font=("./assets/fonts/DIN.ttf", 18),
            placeholder_text="Usuario",
            width=300,
            height=40
        )
        username.place(x=80, y=200)


login = Login()
login.showLogin()
login.app.mainloop()
