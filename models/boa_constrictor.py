from models.animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    LIMITE_RATONES = 20

    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_raton(self):
        """Incrementa los ratones comidos con un límite de 10. Si se alcanza, lanza ValueError."""
        if self._ratones_comidos >= self.LIMITE_RATONES:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += 1
