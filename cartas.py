from enum import Enum
from personagem import Personagem
from random import randint

class Carta:
    def __init__(self, nome, energia_gasta: int, descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao

    def usar(self):
        return "Carta inválida."

class TipoCarta (Enum):
    VIDA_MAXIMA = 1
    DEFESA = 2
    ATAQUE = 3
    ENERGIA_MAXIMA = 4

# CartaAumento herda da classe "Carta"
class CartaAumento(Carta):
    def __init__(self, nome, energia_gasta:int, descricao, tipo: TipoCarta, pontos_aumentados:int):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
    
    def usar(self, beneficiado:Personagem):
        match self.tipo:
            case TipoCarta.VIDA_MAXIMA:
                beneficiado.vida_maxima += self.pontos_aumentados

            case TipoCarta.DEFESA:
                beneficiado.pontos_defesa += self.pontos_aumentados

            case TipoCarta.ATAQUE:
                beneficiado.pontos_ataque += self.pontos_aumentados
            
            case TipoCarta.ENERGIA_MAXIMA:
                beneficiado.energia_maxima += self.pontos_aumentados

            case _: # Default (se não cair em nenhum dos acima)
                return f"Tipo de carta inválida"

class CartaRoubo (Carta):
    def __init__(self, nome, energia_gasta: int, descricao):
        super().__init__(nome, energia_gasta, descricao)
    
    def usar (self, ladrao: Personagem, vitima: Personagem):
        n_aleatorio = randint(0, len(vitima.mao_de_cartas)-1)
        carta_roubada = vitima.mao_de_cartas.pop(n_aleatorio)
        ladrao.mao_de_cartas.append(carta_roubada)
        return f"{ladrao.nome} roubou a carta {carta_roubada.nome} de {vitima.nome}"