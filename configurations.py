class Configurations:
    def __init__(self):
        # Configuraciones predeterminadas
        self.settings = {
            "volume": 50,  # Rango 0-100
            "resolution": "1920x1080",
            "fullscreen": True,
            "controls": {
                "move_up": "W",
                "move_down": "S",
                "move_left": "A",
                "move_right": "D",
                "action": "E"
            }
        }

    # Métodos para interactuar con las configuraciones
    def increase_volume(self, step=5):
        if self.settings["volume"] < 100:
            self.settings["volume"] = min(100, self.settings["volume"] + step)
            print(f"Volumen aumentado a {self.settings['volume']}")
        else:
            print("El volumen ya está en el máximo.")

    def decrease_volume(self, step=5):
        if self.settings["volume"] > 0:
            self.settings["volume"] = max(0, self.settings["volume"] - step)
            print(f"Volumen reducido a {self.settings['volume']}")
        else:
            print("El volumen ya está en el mínimo.")