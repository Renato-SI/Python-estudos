#estudos09
n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
media=(n1+n2)/2
if media>7:
    print("Parabens vc foi aprovado!")
elif media<7:
    print("Vc esta reprovado!")
print(f"Sua média é igual a: {media} ")
