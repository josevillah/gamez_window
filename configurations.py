import pygame

class Configurations:
    def __init__(self):
        # Opciones de resoluciones disponibles
        self.resolutions = {
            "1920x1080": (1920, 1080),  # FHD
            "1280x720": (1280, 720),    # HD
            "1366x768": (1366, 768),    # HD
            "1024x768": (1024, 768),    # XGA
            "800x600": (800, 600),      # SVGA
        }
        # Color para el fondo negro opaco
        self.OPAQUE_BLACK = (0, 0, 0, 200)

        # Resolución actual
        self.currentResolution = self.resolutions["1366x768"]

