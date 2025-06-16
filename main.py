from personagem import Personagem

objeto_personagem1 = Personagem("Garantido")
objeto_personagem2 = Personagem("Caprichoso")

mensagem = objeto_personagem1.atacar(objeto_personagem2)
print(mensagem)
mensagem = objeto_personagem2.atacar(objeto_personagem1)
print(mensagem)
