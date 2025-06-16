from __future__ import annotations
import random 

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida_maxima = 100
        self.vida_atual = 100
        self.pontos_ataque = 120
        self.pontos_defesa = 100
        self.mao_de_cartas = []
        self.energia_maxima = 10
        self.energia = 10


    def atacar(self, inimigo: Personagem):
        if self.energia < 3:
            return f"{self.nome} não tem energia para atacar"
        
        self.energia -= 3 # Custo para atacar = 3

        eficiencia = random.randint(70, 110) / 100
        dano = (self.pontos_ataque - inimigo.pontos_defesa) * eficiencia
        dano = max(0, round(dano)) #round arredonda o dano

        inimigo.levar_dano(dano)

        return f"{self.nome} atacou {inimigo.nome} com eficiência {eficiencia*100}% e casou {dano} de dano."        


    def usar_carta(self, inimigo : Personagem = None):
        pass


    def comprar_carta(self, baralho):
        carta_comprada = random.sample(baralho, k = 1) # escolhe uma carta do baralho
        self.mao_de_cartas.extend(carta_comprada)
        return f"{self.nome} comprou a carta {carta_comprada.nome}."


    def levar_dano(self, dano):
        self.vida_atual -= dano
        return f"{self.nome} levou {dano} de dano e agora a vida é {self.vida_atual}"


    def curar_se(self, pontos_de_vida):
        self.vida_atual = min(self.vida_maxima, self.vida_atual + pontos_de_vida)
        return f"{self.nome} curou {pontos_de_vida} pontos de vida e agora a vida é {self.vida_atual}"


    def ver_cartas(self):
        return self.mao_de_cartas


