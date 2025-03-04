from models.boa_constrictor import BoaConstrictor
from models.huron import Huron

class Guarderia:
    def __init__(self):
        """Inicializa la guardería con 2 Boas y 2 Hurones."""
        self.boas = [
            BoaConstrictor("Nagini", 10.0, 5, "Brasil", 2.0),
            BoaConstrictor("Kaa", 8.5, 4, "India", 1.8)
        ]
        self.hurones = [
            Huron("Fuzzy", 3.5, 2, "Argentina", 1.5),
            Huron("Shadow", 4.0, 3, "Chile", 1.3)
        ]

    def alimentar_boa(self, boa):
        """Intenta alimentar a una boa y maneja excepciones adecuadamente."""
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.comer_raton()
            return "Éxito"
        except ValueError:
            return "La boa está llena"
