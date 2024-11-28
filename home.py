import pygame
import sys

class Home:
    def __init__(self):
        super().__init__()
        pygame.init()
        # Variables de screen
        self.screenWidth = 1366
        self.screenHeight = 720
        self.gameName = 'Proyecto Z'
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.data = None
        pygame.display.set_caption(self.gameName)

        # Variables de colores
        self.backgroundColor = '#1f2329'
        self.blackColor = '#000000'
        self.whiteColor = '#ffffff'
        self.blueColor = "#1565c0"
        self.hoverColor = "#1565c0"  # Color para hover

        # Variables de fuentes
        self.fontTitle = pygame.font.Font('./assets/fonts/DIN Bold.ttf', 50)
        self.fontMenuOptions = pygame.font.Font('./assets/fonts/DIN Medium.ttf', 24)
        self.fontMenuSelected = pygame.font.Font('./assets/fonts/DIN Medium.ttf', 24)
        self.fontMessage = pygame.font.Font('./assets/fonts/DIN Medium.ttf', 24)

        # Variables de titulo
        self.textTitle = ''
        self.textTitleRect = ''

        # Variables de opciones de menu
        self.menuOptions = ["Crear sala", "Unirse a sala", "Opciones", "Salir"]
        self.menuOptionRects = []
        self.selectedOption = 0  # Indica qué opción está seleccionada
        self.keyPressed = False  # Variable para evitar repeticiones automáticas
        self.legendText = ''  # Variable para la leyenda debajo del menú

        # Cargar y redimensionar la imagen de fondo solo una vez
        self.background_image = pygame.image.load("./assets/images/lobby/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.screenWidth, self.screenHeight))

    def showMenu(self):
        # Crear el texto del título
        self.textTitle = self.fontTitle.render(self.gameName, True, self.whiteColor)
        self.textTitleRect = self.textTitle.get_rect(center=(170, 80))  # Centrar el texto en la parte superior

        # Crear rectángulos para cada opción del menú
        self.menuOptionRects = []  # Reiniciar la lista de rectángulos
        for i, option in enumerate(self.menuOptions):
            text = self.fontMenuOptions.render(option, True, self.whiteColor)
            text_rect = text.get_rect(left=50, top=self.screenHeight / 2 + i * 50)
            self.menuOptionRects.append((text, text_rect))

    def optionSelected(self):
        # Función que se llama cuando una opción es seleccionada
        selected_option = self.menuOptions[self.selectedOption]

        if selected_option == "Crear sala":
            print(self.data)
        elif selected_option == "Unirse a sala":
            print("Unirse a sala")
        elif selected_option == "Opciones":
            print("Opciones")
        elif selected_option == "Salir":
            print("Salir")
            self.running = False

    def updateLegend(self):
        # Actualizar el texto de la leyenda según la opción seleccionada
        selected_option = self.menuOptions[self.selectedOption]

        if selected_option == "Crear sala":
            self.legendText = "Comienza una nueva aventura."
        elif selected_option == "Unirse a sala":
            self.legendText = "Unete a una sala existente."
        elif selected_option == "Opciones":
            self.legendText = "Configura las opciones del juego."
        elif selected_option == "Salir":
            self.legendText = "Sal del juego."

    def runHome(self, data):
        self.data = data
        self.showMenu()

        while self.running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i, (text, rect) in enumerate(self.menuOptionRects):
                        if rect.collidepoint(mouse_x, mouse_y):  # Si el clic está sobre la opción
                            self.selectedOption = i
                            self.optionSelected()  # Llamar a la función cuando se selecciona una opción
                            break
                elif event.type == pygame.KEYDOWN:  # Detectar teclas presionadas
                    if event.key == pygame.K_RETURN:  # Si se presiona la tecla Enter
                        self.optionSelected()  # Llamar a la función cuando se presiona Enter

            # Obtener la posición del mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Actualizar la leyenda
            self.updateLegend()

            # Dibujar la imagen de fondo solo una vez (sin redimensionar cada vez)
            self.screen.blit(self.background_image, (0, 0))

            # Dibujar el título
            self.screen.blit(self.textTitle, self.textTitleRect)

            # Dibujar las opciones de menú con efecto hover
            for i, (text, rect) in enumerate(self.menuOptionRects):
                # Comprobar si el mouse está sobre la opción
                if rect.collidepoint(mouse_x, mouse_y):
                    text = self.fontMenuOptions.render(self.menuOptions[i], True, self.hoverColor)
                else:
                    # Cambiar color si la opción está seleccionada por teclado
                    if i == self.selectedOption:
                        text = self.fontMenuSelected.render(self.menuOptions[i], True, self.hoverColor)
                    else:
                        text = self.fontMenuOptions.render(self.menuOptions[i], True, self.whiteColor)
                self.screen.blit(text, rect)

            # Mostrar la leyenda debajo del menú
            legend_text_surface = self.fontMessage.render(self.legendText, True, self.whiteColor)
            legend_rect = legend_text_surface.get_rect(left=50, top= self.screenHeight - 50)  # Centrado en la parte inferior
            self.screen.blit(legend_text_surface, legend_rect)

            # Movimiento con las teclas
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and not self.keyPressed:  # Mover hacia abajo
                self.selectedOption = (self.selectedOption + 1) % len(self.menuOptions)
                self.keyPressed = True  # Marcar que la tecla ha sido presionada

            elif keys[pygame.K_UP] and not self.keyPressed:  # Mover hacia arriba
                self.selectedOption = (self.selectedOption - 1) % len(self.menuOptions)
                self.keyPressed = True  # Marcar que la tecla ha sido presionada

            # Si la tecla es liberada, permitir la siguiente pulsación
            if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                self.keyPressed = False

            # Actualizar la pantalla
            pygame.display.flip()

            # Limitar los FPS a 60 para mejorar el rendimiento
            self.clock.tick(60)

        pygame.quit()


home = Home()
home.runHome({'_id': '67401d7668743d231fa3b869', 'email': 'villa.herrera.1994@gmail.com', 'username': 'josevillah', 'role': 1})