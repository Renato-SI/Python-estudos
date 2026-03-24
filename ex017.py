#estudo17
km = float(input(" Quantos Km vc perecorreu? "))
dias = int(input(" por quantos dias vc alugou o carro? " ))
valor = (dias * 60) + (km * 0.15)
print(f" O valor a ser pago pelo aluguel de {dias} dias e Por ter rodado {km} KM \n é de {valor:.2f}R$ ! ")