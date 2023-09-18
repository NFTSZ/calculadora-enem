from time import sleep

# Apresentação inicial
print('     --------------------------')
print('     BEM VINDO A CALCULADORA ENEM')
print('obs: use ponto(.) ao invés de vírgula(,) nas notas')
print('     --------------------------\n')

sleep(1)

# Solicitação das notas de cada disciplina
ling = float(input('Digite sua nota em: Linguagens, Codigos e suas Tecnologias>  '))
hum = float(input('Digite sua nota em: Ciências Humanas e suas Tecnologias> '))
natu = float(input('Digite sua nota em: Ciências da Natureza e suas Tecnologias> '))
mat = float(input('Digite sua nota em: Matemática e suas Tecnologias> '))
red = float(input('Digite sua nota em: Redação> '))

# Cálculo da média
media = (ling + hum + natu + mat + red) / 5

# Exibição da média no ENEM
print('Sua média no ENEM é: {:.2f}'.format(media))
