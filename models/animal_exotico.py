from models.animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    @property
    def pais_origen(self) -> str:
        """Devuelve el país de origen del animal exótico."""
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value: str):
        """Establece el país de origen del animal, validando que sea un string válido."""
        if isinstance(value, str) and value.strip():
            self._pais_origen = value
        else:
            raise ValueError("El país de origen debe ser una cadena de texto válida.")

    @property
    def impuestos(self) -> float:
        """Devuelve el impuesto de importación del animal."""
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value: float):
        """Establece los impuestos del animal, validando que sean positivos."""
        if isinstance(value, (int, float)) and value >= 0:
            self._impuestos = value
        else:
            raise ValueError("El impuesto debe ser un número positivo.")

    def calcular_flete(self) -> float:
        return round(self.peso * self._impuestos, 2)
