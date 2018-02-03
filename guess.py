import numpy as np

n = int(input('Escolha a quantidade de dígitos:    '))
tent = 0
lista = []

for i in range(n):
    lista.append(str(np.random.randint(0,9)))
    numero = "".join(lista)

while (tent != numero and tent != 'sair'):
    tent = str(input("Tente adivinhar o número:   "))
    while len(tent) != len(numero):
        print("Mané, a quantidade de dígitos deve ser {}!".format(len(numero)))
        tent = str(input("Tente adivinhar o número:    "))

    pos_cor = pos_err = 0

    for i in range(len(numero)):
        if tent[i] == numero[i]:
            pos_cor += 1

    temp = numero  
    for t in tent:
        if t in temp:
            pos_err +=1
            temp = temp.replace(t, "", 1)
            
    print("Número de dígitos na posição correta: ", pos_cor)
    print("Número de dígitos na posição incorreta: {}\n".format(pos_err - pos_cor))
    
print("Jogo terminado com SUCESSO!")
