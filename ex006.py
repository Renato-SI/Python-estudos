#estudos06:
#Quebra e continuidaed de linhas:
#Para quebrarmos o print usamos o"\n" = ao contrabarra+n, ja para impedir que o print quebre ao meio, usamos end="  " no inicio do print antes do f(format)
#ex do \n(quebra de linha)
name01=input("digite seu nome")
idade_name1=input("digite sua idade")
print(f" Seu nome é {name01} \n voce tem {idade_name1} anos \n Nasceu no ano de {2026-(int(idade_name1))}")
#exemplo do end
name0=input("digite seu nome")
idade_name0=input("digite sua idade")
print(end=" >>> " f" Seu nome é {name0} , vc tem {idade_name0} anos e seu nascimento foi em  {2026-(int(idade_name0))} !")
#Nesse caso , eu peguei uma variavel do type str e usei ela em uma conta que eu precisei como int.