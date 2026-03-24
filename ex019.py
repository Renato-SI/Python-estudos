#estudos19:
from math import hypot
cateto_oposto=float(input(" Digite o valor do cateto oposto: "))
cateto_adjacente=float(input(" Digite o valor do adjacente: "))
hip01= hypot(cateto_adjacente,cateto_oposto)
print(f"{hip01:.2f}")