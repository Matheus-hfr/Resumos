#POO HERANÇA

class Animal:  # Classe base (superclasse)
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

class Cachorro(Animal):  # Classe derivada (subclasse) que herda de Animal
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")  # Metodo utlizado para trazer os atributos da classe base
        self.raca = raca

    def latir(self):       # Busca o elemento na propria classe
        return f"{self.nome} está latindo!"
    
class Gato(Animal):  # Outra classe derivada que herda de Animal
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")  # Metodo utlizado para trazer os atributos da classe base
        self.cor = cor

    def miar(self):       # Busca o elemento na propria classe
        return f"{self.nome} está miando!"

animal_generico = Animal("Bicho", "Desconhecida")
cachorro1 = Cachorro("Rex", "Labrador")
gato = Gato("Mimi", "Branco")

print(cachorro1.nome, cachorro1.especie, cachorro1.raca)  # Acessando atributos herdados e próprios