import pygame

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
        self.titleLogin = pygame.font.Font("./assets/fonts/DIN bold.ttf", 35)
        self.inputFont = pygame.font.Font("./assets/fonts/DIN.ttf", 36)

        # Colors
        self.white = (255, 255, 255)
        self.gray = (156, 156, 156)
        self.BLACK = (0, 0, 0)
        self.hoverColor = (200, 200, 200)

        # Clock
        self.CLOCK = pygame.time.Clock()

    def runGame(self):
        imageBg = pygame.image.load("./assets/images/bg.png")
        windowBg = pygame.transform.scale(imageBg, (self.WIDTH, self.HEIGHT))

        # Música de fondo
        pygame.mixer.music.load("./assets/sounds/musicLobby.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        # Botón de inicio de sesión
        button_login = pygame.Surface((200, 50), pygame.SRCALPHA)
        button_login.fill((0, 0, 0, 0))
        
        # Posición del botón
        button_rect = button_login.get_rect(center=(150, self.HEIGHT/2))
        
        # Texto del botón
        button_text = self.titleLogin.render("Iniciar sesión", True, self.white)
        text_rect = button_text.get_rect(center=button_login.get_rect().center)

        # Ciclo de juego
        while self.run:
            # Dibujar el fondo
            self.SCREEN.blit(windowBg, (0, 0))

            # Dibujar botón transparente
            self.SCREEN.blit(button_login, button_rect.topleft)
            self.SCREEN.blit(button_text, (button_rect.x + (250 - text_rect.width) // 2, button_rect.y + (50 - text_rect.height) // 2))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                # Verificar si se hace clic en el botón
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        self.login()

                # Verificar si se presiono el boton ENTER
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.login()


            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    Main().runGame()
    pygame.quit()
    # Main().login()