from random import randint

sorteio = {}

participantes = {
    1:  ["Leonardo Leao", "leonardoleao486@gmail.com"],
    2:  ["Leonardo Claudio", "leonardo-claudio@outlook.com"],
    3:  ["Bruna Fabio", "bruninha.fabio@hotmail.com"],
    4:  ["Gabrielle Lelis", "ggabi.lelis@gmail.com"],
    5:  ["Luana Melo", "luana.melo1900@gmail.com"],
    6:  ["Daniela Muraro", "dani.muraro1@gmail.com"],
    7:  ["Luciana Oliveira", "luciaolivier24@gmail.com"],
    8:  ["Karina Porfirio", "karinaporfirio98@gmail.com"],
    9:  ["Any Caroline", "anycarolinexx@gmail.com"],
    10: ["Julia Poker", "juliaapoker@gmail.com"],
    11: ["Isabella Araujo", "i237019@dac.unicamp.br"]
}

for i in range(1, len(participantes)+1):
    sorteado = randint(1, len(participantes))
    while (sorteado in sorteio.values()) or (i == sorteado):
        sorteado = randint(1, len(participantes))
    sorteio[i] = sorteado
    
if len(sorteio) == len(participantes):
    for i in sorteio.keys():
        print(participantes[sorteio[i]][0], participantes[i][1])
