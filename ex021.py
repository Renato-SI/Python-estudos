#estudos21:
import random
a1 = str(input(" Primeiro aluno: "))
a2 = str(input(" Segundo aluno: "))
a3 = str(input(" Terceiro aluno: "))
a4 = str(input(" Quarto aluno: "))
lista = [a1,a2,a3,a4]
print(f" O aluno escolhido foi o : {random.choice(lista)}")

#print(f" O aluno escolhido foi o : {random.choices(lista , k=2)}")
# colocar o "k" quando queremos escolher mais de 01 resultado, junto ao choice , podendo repetir a mesma pessoa!
#O choices é com reposição, ou seja , pode repetir o mesmo elemento!