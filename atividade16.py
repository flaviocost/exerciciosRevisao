# Escreva um algoritmo para ler a hora de
# início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em
# horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo
# pode iniciar em um dia e terminar no dia
# seguinte

horaInicio = int(input('Informe a hora de início da partida: '))
horaFim = int(input('Informe a hora do fim da partida: '))

if horaInicio <= horaFim:
    tempo = horaFim - horaInicio
else:
    tempo = 24 - horaInicio + horaFim
print(f'O jogo durou {tempo} horas!')