class Mascota:
    def _init_(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
    
    def saludar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class Perro(Mascota):
    def _init_(self, nombre, peso, altura, es_lazarillo=False):
        super()._init_(nombre, peso, altura)
        self.es_lazarillo = es_lazarillo

    def saludar(self):
        print(f"{self.nombre} ladra: ¡Guau guau!")

class Gato(Mascota):
    def _init_(self, nombre, peso, altura, es_sociable=True):
        super()._init_(nombre, peso, altura)
        self.es_sociable = es_sociable

    def saludar(self):
        print(f"{self.nombre} maulla: ¡Miau!")

class Pez(Mascota):
    def _init_(self, nombre, peso, altura, es_agua_dulce=True):
        super()._init_(nombre, peso, altura)
        self.es_agua_dulce = es_agua_dulce

    def saludar(self):
        print(f"{self.nombre} gira en el agua en forma de saludo.")

#SUBCLASES 
class Adoptante:
    def _init_(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def adoptar(self, mascota):
        self.mascotas.append(mascota)

    def mascotas_saludar(self):
        for mascota in self.mascotas:
            mascota.saludar()

class Refugio:
    def _init_(self):
        self.mascotas = []

    def recibir_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        for mascota in self.mascotas:
            print(f"{mascota.nombre} ({type(mascota)._name_})")
#ejemplo de uso 
refugio = Refugio()

# Creamos mascotas
firulais = Perro("Firulais", 20, 50, es_lazarillo=True)
michi = Gato("Michi", 5, 25, es_sociable=False)
nemo = Pez("Nemo", 1, 10, es_agua_dulce=True)

# Las llevamos al refugio
refugio.recibir_mascota(firulais)
refugio.recibir_mascota(michi)
refugio.recibir_mascota(nemo)

# Un adoptante llega
ana = Adoptante("Ana")

# Ana adopta a Michi y Nemo
ana.adoptar(michi)
ana.adoptar(nemo)

# Las mascotas de Ana saludan
ana.mascotas_saludar()


