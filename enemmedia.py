from time import sleep

#ignorem, so p ficar bonitinho KKKKK
print('     --------------------------')
print('     BEM VINDO A CALCULADORA ENEM')
print('obs: use ponto(.) ao invés de virgula(,) nas notas')
print('     --------------------------\n')

sleep(1)

#queria ter feito algo mais curto mas o básico funciona
ling = float(input('Digite sua nota em: Linguagens, Codigos e suas Tecnologias>  '))
hum = float(input('Digite sua nota em: Ciencias Humanas e suas Tecnologias> '))
natu = float(input('Digite sua nota em: Ciencias da Natureza e suas Tecnologias> '))
mat = float(input('Digite sua nota em: Matematica e suas Tecnologias> '))
red = float(input('Digite sua nota em: Redacao> '))
media = (ling + hum + natu + mat + red) / 5

print('Sua media no ENEM é: {:.2f}'.format(media))