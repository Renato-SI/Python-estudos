#Da para limitar tambem a quantidade de casas flutuantes mostradadas de um numero :
n1=int(input("Digite seu n1"))
n2=int(input("Digite seu n2"))
m=(n1*n2)
di=(n1/n2)
rest=(n1%n2)
divexata=(n1//n2)
e=(n1**n2)         # esse, :.2(ou qualquer numero que vc queira)f , ta limitando o numero que vai ser mostrado na divisao(OU EM QUALQUER VARIAVEL ESCOLHIDA) a no maximo 03 casas flutuamtes/ decimais.
print(f"A m vale {m}, div vale {di:.2f}, rest vale {rest}, a divexata vale {divexata} ! por fim a e vale {e}")