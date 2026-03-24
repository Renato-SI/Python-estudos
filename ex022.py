#estudos22:
import random
a1 = str(input(" Primeiro aluno: "))
a2 = str(input(" Segundo aluno: "))
a3 = str(input(" Terceiro aluno: "))
a4 = str(input(" Quarto aluno: "))
lista = [a1,a2,a3,a4]
print(f" O primeiro é {random.sample(lista,1)}")
print(f" O segundo é {random.sample(lista,1)}")
print(f" O terceiro é {random.sample(lista,1)}")
print(f" O quarto é {random.sample(lista,1)}")

#Tambem pode ser: print(f" A ordem é: {random.sample(lista,4)}")