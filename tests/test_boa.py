import unittest
from models.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba: inicializa un objeto BoaConstrictor"""
        self.boa = BoaConstrictor(nombre="Nagini", peso=10.0, edad=5, pais_origen="Brasil", impuestos=2.0)

    def test_hacer_sonido(self):
        """Prueba que la boa haga el sonido correcto."""
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        """Prueba que el cálculo del flete sea correcto."""
        self.assertEqual(self.boa.calcular_flete(), 20.0)  # 10.0 * 2.0

    def test_comer_raton(self):
        """Prueba que la boa coma ratones con un límite impuesto."""
        limite_ratones = 10

        for _ in range(limite_ratones):
            self.boa.comer_raton()

        self.assertEqual(self.boa._ratones_comidos, limite_ratones)

        with self.assertRaises(ValueError) as context:
            self.boa.comer_raton()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

if __name__ == '__main__':
    unittest.main()