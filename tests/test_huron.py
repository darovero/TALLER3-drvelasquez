import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        """Inicializa un objeto Huron antes de cada prueba."""
        self.huron = Huron(nombre="Fuzzy", peso=3.5, edad=2, pais_origen="Argentina", impuestos=1.5)

    def test_hacer_sonido(self):
        """Prueba que el hurón haga el sonido correcto."""
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        """Prueba que el cálculo del flete sea correcto."""
        self.assertEqual(self.huron.calcular_flete(), 5.25)  # 3.5 * 1.5

if __name__ == '__main__':
    unittest.main()