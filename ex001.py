dic01=int(input("Digite o PRIMEIRO número"))
dic03=input("Qual o operação vc quer fazer(soma,multiplicação,subtração,divisão)")
dic02=int(input("Digite o SEGUNDO número"))
if dic03=="soma": 
    print (dic01+dic02)
elif dic03== "multiplicação":
    print (dic01*dic02)
elif dic03== "subtração":
    print (dic01-dic02)
elif dic03== "divisão":
    print (dic01/dic02)
elif dic03!=("soma,multiplicação,subtração,divisão"):
    print("Tu é demente porra")