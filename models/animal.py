from models import ianimal 

class Animal(ianimal.IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0.0

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del animal."""
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        """Establece un nuevo nombre para el animal, validando que sea un string."""
        if isinstance(value, str) and value.strip():
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena de texto válida.")

    @property
    def peso(self) -> float:
        """Devuelve el peso del animal."""
        return self._peso

    @peso.setter
    def peso(self, value: float):
        """Establece un nuevo peso para el animal, validando que sea un número positivo."""
        if isinstance(value, (int, float)) and value > 0:
            self._peso = value
        else:
            raise ValueError("El peso debe ser un número positivo.")

    @property
    def edad(self) -> int:
        """Devuelve la edad del animal."""
        return self._edad

    @edad.setter
    def edad(self, value: int):
        """Establece una nueva edad para el animal, validando que sea un número entero positivo."""
        if isinstance(value, int) and value >= 0:
            self._edad = value
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def kilos_comidos(self) -> float:
        """Devuelve la cantidad de comida consumida por el animal."""
        return self._kilos_comidos

    def comer(self, kilos: float):
        """Incrementa la cantidad de comida consumida."""
        if kilos > 0:
            self._kilos_comidos += kilos
        else:
            raise ValueError("La cantidad de comida debe ser positiva.")

    def obtener_kilos_comidos(self) -> float:
        """Implementación del método obligatorio de la interfaz IAnimal."""
        return self._kilos_comidos

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
