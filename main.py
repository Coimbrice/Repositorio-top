import random
a = 0
random.seed(0)
preco = input('Preço do Jogo: ')
print("Aperte 'Enter' para jogar. Escreva 'grana' para ver o dinheiro que você astou jogando e quantas vezes você jogou: ")
while True:
    I = input()
    if I == ('grana'):
        c = float(preco)*a
        if c > 0.9:
            print("Parabéns! Você gastou um total de %d reais! E tentou %d vezes" %(c,a))
        else:
            print("Parabéns! Você gastou um total de %.2f centavos! E tentou %d vezes" % (c, a))
    else:
        n = random.randint(1,1000000)
        print(n)
        a += 1
        if n == 1:
            c = float(preco) * a
            if c > 0.9:
                print("Parabéns! Você gastou um total de %d reais! E tentou %d vezes e ganhou 300.000.000 de reais na loteria" % (c, a))
            else:
                print("Parabéns! Você gastou um total de %.2f centavos! E tentou %d vezes e ganhou 300.000.000 de reais na loteria" % (c, a))
            break