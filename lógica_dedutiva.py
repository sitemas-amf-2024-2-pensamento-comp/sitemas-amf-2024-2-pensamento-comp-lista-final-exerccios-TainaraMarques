#Lógica dedutiva
#Parte de uma regra geral para analisar um caso específico. A conclusão é inevitável se as premissas forem verdadeiras.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
     print(f"O número {numero} é par.")

else:
    print(f"O número {numero} não é par.")

#Lógica indutiva
#Parte de observações específicas para formular uma regra geral ou identificar padrões. A conclusão é provável, mas não garantida.

print("\n\nLógica Indutiva")

for i in range(1, 101):
    if i % 2 != 0:
        print()