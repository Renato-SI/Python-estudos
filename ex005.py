#ESTUDOS05 , Podemos alinhar ou definir quantos espaços  a variavel {qualquercoisa}, vai ocupar no print
#ex:
nome=input("digite seu nome")
print (f"prazer em te conhecer {nome:20} !")

#nesse  caso o ":20" quer dizer que a variavel "nome vai ocupar 20 espaces no total , como ja tem 04 spaces no caso de jose , ele joga maisa 16 espaces antes de rodar a outra parte da string/ print.
nome=input("digite seu nome")
print(f"prazer em te conhecer {nome:20} !")

#Se quisermos centralizar a variavel para a esquerda usamos ":<" e para direita ":>", podemos centralizar para algum lado mesmo usando o lance dos espacamentos!
nome=input("digite seu nome")
print(f"prazer em te conhecer {nome:>10} !")

nome=input("digite seu nome")
print(f"prazer em te conhecer {nome:<10} !")

#se quisermos centralizar o item no meio usamos "^", quando colocamos ":=" ele vai ocupar os espaces com =.... , ja se usarmos ":^20" ele vai centralizar a varivel e ainda vai ocupar todos os espaces vazios... .
nome=input("digite seu nome")
print(f"prazer em te conhecer {nome:=^20} !")
