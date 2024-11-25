import pygame
import pygame.freetype  # Usado para fuentes más avanzadas, como input

class MenuOne:
    def __init__(self, main):
        self.main = main
        self.options = ["Iniciar sesión"]
        self.selected_option = 0
        self.font = main.titleFont  # Usar la fuente de la clase principal

    # Metodo para mostrar el menu de inicio
    def show_menu(self):
        for i, option in enumerate(self.options):

            # Cambiar el color de la opción seleccionada
            color = self.main.hoverColor if i == self.selected_option else self.main.gray

            # Crear el texto
            text = self.font.render(option, True, color)

            # Configurar el rectángulo del texto
            text_rect = text.get_rect(center=(170,(self.main.HEIGHT) / 2))

            # Dibujar el rectangulo del texto en la pantalla
            self.main.screen.blit(text, text_rect)


    # def move_selection(self, direction):
    #     """Mueve la selección del menú."""
    #     self.selected_option = (self.selected_option + direction) % len(self.options)

    # def select_option(self):
    #     """Ejecuta la acción según la opción seleccionada."""
    #     if self.selected_option == 0:  # Jugar
    #         print("Iniciar el juego")
    #         return "start_game"
    #     elif self.selected_option == 1:  # Opciones
    #         print("Abrir opciones")
    #         return "options"
    #     elif self.selected_option == 2:  # Salir
    #         print("Salir del juego")
    #         return "exit"

    # def draw_login_window(self):
    #     """Dibuja la ventana emergente de inicio de sesión."""
    #     # Fondo semitransparente para la ventana emergente
    #     overlay = pygame.Surface((self.main.windowWidth, self.main.windowHeight))
    #     overlay.set_alpha(180)  # Transparencia
    #     overlay.fill((0, 0, 0))  # Fondo negro semitransparente
    #     self.main.screen.blit(overlay, (0, 0))

    #     # Caja de inicio de sesión
    #     login_box = pygame.Rect(483, 250, 400, 300)
    #     pygame.draw.rect(self.main.screen, self.main.white, login_box)

    #     pygame.display.flip()

