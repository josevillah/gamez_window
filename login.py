import pygame
import pygame_gui

class Login:
    def __init__(self, main):
        self.main = main
        self.username = None
        self.password = None
        self.login_button = None

    def show_inputs(self):
        # Crear input para username
        self.username = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (570, 325),
                (220, 50),
            ),
            manager=self.main.MANAGER
        )

        # Crear input para password
        self.password = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (570, 385),
                (220, 50),
            ),
            manager=self.main.MANAGER
        )

         # Crear el botón de inicio de sesión
        self.login_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (570, 445),  # Cambia la posición Y para que esté después del password
                (220, 50),
            ),
            text='Iniciar sesión',  # Texto del botón
            manager=self.main.MANAGER
        )

    def draw_login_window(self):
        # Fondo semitransparente para la ventana emergente
        overlay = pygame.Surface((self.main.WIDTH, self.main.HEIGHT))
        overlay.set_alpha(180)  # Transparencia
        overlay.fill((0, 0, 0))  # Fondo negro semitransparente
        self.main.SCREEN.blit(overlay, (0, 0))

        # Caja de inicio de sesión
        login_box = pygame.Rect(483, 250, 400, 300)
        pygame.draw.rect(self.main.SCREEN, self.main.white, login_box)

        # Títulos y campos
        title_text = self.main.titleLogin.render("Iniciar sesión", True, self.main.BLACK)
        self.main.SCREEN.blit(title_text, (self.main.WIDTH // 2 - title_text.get_width() // 2, 280))

        # Dibujar la interfaz de usuario con los inputs
        self.main.MANAGER.draw_ui(self.main.SCREEN)

        pygame.display.flip()
