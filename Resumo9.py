#POO Básico

#Principaias conceitos:
#Classe: é um modelo para criar objetos (uma estrutura que define atributos e comportamentos comuns a todos os objetos de um determinado tipo).
#Objeto: é uma instância de uma classe, que possui atributos (características) e métodos (comportamentos).
#Atributos: são as características ou propriedades de um objeto.
#Métodos: são as funções ou comportamentos que um objeto pode realizar.
#Encapsulamento: é o princípio de ocultar os detalhes internos de um objeto e expor apenas o que é necessário.
#Herança: é o mecanismo pelo qual uma classe pode herdar atributos e métodos de outra classe.
#Polimorfismo: é a capacidade de diferentes classes responderem de maneira diferente ao mesmo método ou mensagem.

#Exemplo básico de POO em Python:
class Pessoa:
    def __init__(self, nome, idade): # self guarda os dados dentro do objeto   EX: p1.nome, p1.idade, 
        self.nome = nome  # Atributo
        self.idade = idade  # Atributo

    def apresentar(self):  # Método
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
pessoa1 = Pessoa("João", 25) # Criando um objeto da classe Pessoa
pessoa2 = Pessoa("Maria", 30) # Criando outro objeto da classe Pessoa
print(pessoa1.apresentar())  # Chamando o método apresentar do objeto pessoa1
print(pessoa2.apresentar())  # Chamando o método apresentar do objeto pessoa2