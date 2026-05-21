print ("Seja muito bem vindo ao quiz do Thiago")
answer_user = input("Quer começar? (SIM/NÃO) ").upper()

if answer_user != "SIM":
     quit ()
score = 0

print("Começando... \n")
print("QUEM DESENVOLVEU O JOGO GRAND THEFT AUTO (GTA)? \n (A) ROCKSTAR GAMES \n (B) ACTIVISION \n (C) UBISOFT \n (D) EASIM \n")
answer_1 = input("Resposta: ").upper()   #O .upper() transforma qualquer letra em MAIÚSCULA.

if answer_1 == "A":
    print("CORRETO \n")
    score += 1

else :
    print("INCORRETO \n")

print("QUAL O NOME DO PROTAGONISTA DO JOGO GTA SAN ANDREAS? \n (A) PELÉ \n (B) CARL JOHNSON (CJ) \n (C) CHAVES \n (D) GOKU \n")
answer_2 = input("Resposta: ").upper()

if answer_2 == "B":
    print("CORRETO \n")
    score += 1

else :
    print("INCORRETO \n")

print("O QUE SIGNIFICA GTA? \n (A) GRANDE TRATOR AGRÍCOLA \n (B) GRAND THEFT AUTO \n (C) GOKU TREINANDO AGACHAMENTO \n (D) GALO TOP ATÔMICO \n")
answer_3 = input("Resposta: ").upper()

if answer_3 == "B":
    print("CORRETO \n ")
    score += 1

else :
    print("INCORRETO \n")

print ("QUAL DESSES PERSONAGENS É DO GTA SAN ANDREAS? \n (A) BIG SMOKE \n (B) NARUTO \n (C) HOMEM-ARANHA \n (D) RELÂMPAGO MARQUINHOS \n")
answer_4 = input("Resposta: ").upper()

if answer_4 == "A":
        print("CORRETO \n")
        score += 1

else:
        print("INCORRETO ")

print("O QUE ACONTECE QUANDO VOCÊ GANHA 5 ESTRELAS NO GTA? \n (A) A POLÍCIA TE PERSEGUE \n (B) VOCÊ GANHA PIX \n (C) O CJ VIRA PREFEITO \n (D) O JOGO DESINSTALA \n")
answer_5 = input("Resposta: ").upper()

if answer_5 == "A":
        print("CORRETO \n")
        score += 1

else:
        print("INCORRETO \n")

print(f"\n🎮 Quiz acabou... Pontuação: {score}/5\n")

if score == 5:
    print("Você é um verdadeiro mestre do GTA 😎")

elif score >= 3:
    print("Você conhece bastante sobre GTA 🔥")

else:
    print("Tá precisando jogar mais GTA 😂")

input("Pressione ENTER para sair...")