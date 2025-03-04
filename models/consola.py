from boa_constrictor import BoaConstrictor
from huron import Huron

def main():
    print("\n PRUEBA DE ANIMALES EXÓTICOS ")

    boa = BoaConstrictor(nombre="Nagini", peso=12.5, edad=5, pais_origen="Brasil", impuestos=2.5)
    print(f"\nBoa Constrictor creada: {boa.nombre}")
    print(f"Peso: {boa.peso} kg")
    print(f"Origen: {boa.pais_origen}")
    print(f"Costo de importación: ${boa.calcular_flete()}")
    print(f"Sonido: {boa.hacer_sonido()}")

    print("\nAlimentando a la Boa con 3 ratones")
    boa.comer_raton()
    boa.comer_raton()
    boa.comer_raton()
    print(f"Ratones comidos: {boa.ratones_comidos}")

    huron = Huron(nombre="Fuzzy", peso=4.2, edad=2, pais_origen="Argentina", impuestos=1.8)
    print(f"\nHurón creado: {huron.nombre}")
    print(f"Peso: {huron.peso} kg")
    print(f"Origen: {huron.pais_origen}")
    print(f"Costo de importación: ${huron.calcular_flete()}")
    print(f"Sonido: {huron.hacer_sonido()}")

if __name__ == "__main__":
    main()
