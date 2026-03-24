#Anotações aula 08 em diante:
#Modularização = podemos trazer uma importação de fora para dentro do python , exemplo 
#import bebida(vai importar todas as  bebidas que estiverem na biblioteca exportada)
#caso eu queira importar apenas algumas ou uma unica bebida devo dar um from no inicio 
#from doce import pudim ( ou algo assim), entao basicamente a modularização é vc armazenar coisas em um modulo
#para usar posteriormente.
#Resumindo: o comando Import+nome do moculo vai importar tudo daquele modulo (Vai importar todas as funcionalidades / generalista)
      #ja o comando from + import + algo especifico do modulo. ( apenas oq eu escolher / especifico )
#from math import sqrt

#num01 = int(input("digite um n"))
#raiz = sqrt(num01)
#print(f"A raiz de {num01} vale {raiz}")
#isso é um otimo exemplo da exportação de uma funcionalidade especifica , nesse caso da biblioteca math!
# se eu tivesse colocado import math , eu teria importrado tudo da biblioteca math , gastando muita memoria!


#import random # Nesse caso estou importando toda  a bibli de random
#num = random.random()# esse comando vai gerar um numero random entre 0-1
#num02 = random.randint(100,1000) #Ja nesse ele ta pegando um numero inteiro aleatorio do intervalo d a,b q eu selecionei
#print(num02)
