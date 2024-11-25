import pygame
import pygame_gui

from login import Login

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.WIDTH = 1366
        self.HEIGHT = 768
        self.run = True
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.icon = pygame.image.load("./assets/images/logo.png")

        # Fonts
        self.titleFont = pygame.font.Font("./assets/fonts/DIN.ttf", 35)
        self.titleLogin = pygame.font.Font("./assets/fonts/DIN Medium.ttf", 35)
        self.inputFont = pygame.font.Font("./assets/fonts/DIN.ttf", 36)

        # Colors
        self.white = (255, 255, 255)
        self.gray = (156, 156, 156)
        self.BLACK = (0, 0, 0)
        self.hoverColor = (200, 200, 200)

        # Clock
        self.CLOCK = pygame.time.Clock()
        self.MANAGER = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))

        self.login = Login(self)
        self.show_login_window = False  # Flag para mostrar la ventana de inicio de sesión

    def runGame(self):
        imageBg = pygame.image.load("./assets/images/bgOne.jpg")
        windowBg = pygame.transform.scale(imageBg, (self.WIDTH, self.HEIGHT))

        # Música de fondo
        pygame.mixer.music.load("./assets/sounds/musicLobby.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        # Ciclo de juego
        while self.run:
            UI_REFRESH_RATE = self.CLOCK.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.show_login_window = True  # Mostrar la ventana de login cuando se presiona Enter
                        self.login.show_inputs()

                self.MANAGER.process_events(event)

            self.MANAGER.update(UI_REFRESH_RATE)

            # Dibujar el fondo
            self.SCREEN.blit(windowBg, (0, 0))

            # Si la ventana de login está activa, dibuja la ventana
            if self.show_login_window:
                self.login.draw_login_window()

            # Dibujar la interfaz de usuario
            self.MANAGER.draw_ui(self.SCREEN)

            pygame.display.update()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Main().runGame()