print ("Seja muito bem vindo ao quiz do Thiago")
answer_user = input(" Quer começar? (SIM/NÃO) ")

if answer_user != "SIM":
     quit ()
score = 0

print("Começando... \n")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) ROCKSTAR GAMES \n (B) ACTIVISION \n (C) UBISOFT \n (D) EASIM \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("CORRETO ")
    score += 1

else :
    print("INCORRETO ")

print("QUAL O NOME DO PROTAGONISTA DO JOGO GTA SAN ANDREAS? \n (A) PELÉ \n (B) CARL JONHSON (CJ) \n (C) CHAVES \n (D) GOKU \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("CORRETO ")
    score += 1

else :
    print("INCORRETO ")

print("O QUE SIGNIFICA GTA? \n (A) GRANDE TRATOR AGRÍCOLA \n (B) GRAND THEFT AUTO \n (C) GOKU TREINANDO AGACHAMENTO \n (D) GALO TOP ATÔMICO \n")
answer_3 = input("Resposta: ")

if answer_3 == "B":
    print("CORRETO ")
    score += 1

else :
    print("INCORRETO ")

print ("QUAL DESSES PERSONAGENS É DO GTA SAN ANDREAS? \n (A) BIG SMOKE \n (B) NARUTO \n (C) HOMEM-ARANHA \n (D) RELÂMPAGO MARQUINHOS \n")
answer_4 = input("Resposta: ")

if answer_4 == "A":
        print("CORRETO ")
        score += 1

else:
        print("INCORRETO ")

print("O QUE ACONTECE QUANDO VOCÊ GANHA 5 ESTRELAS NO GTA? \n (A) A POLÍCIA TE PERSEGUE \n (B) VOCÊ GANHA PIX \n (C) O CJ VIRA PREFEITO \n (D) O JOGO DESINSTALA \n")
answer_5 = input("Resposta: ")

if answer_5 == "A":
        print("CORRETO ")
        score += 1

else:
        print("INCORRETO ")

print(f"Quiz acabou... Pontuação: {score}/5")