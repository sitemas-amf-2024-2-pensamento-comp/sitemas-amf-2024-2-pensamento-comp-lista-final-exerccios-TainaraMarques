#while:
#O laço while é utilizado quando queremos repetir um bloco de código enquanto uma condição for verdadeira. A condição é verificada antes de cada iteração, e o laço continua até que essa condição se torne falsa. Ele é útil quando não sabemos o número exato de iterações, mas sabemos qual é a condição para a execução continuar.
vetor = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(vetor):
    print(f"O quadrado de {vetor[i]} é {vetor[i] ** 2}")
    i += 1



#for:
#O laço for é mais adequado quando sabemos o número de iterações ou estamos percorrendo uma sequência de elementos (como uma lista, tupla, ou intervalo). Ele itera diretamente sobre a sequência, e a variável do laço assume um valor diferente a cada iteração.

vetor = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(vetor)):
    quadrado = vetor[i] ** 2
    print(f" o quadrado de {vetor[i]} é {quadrado}")