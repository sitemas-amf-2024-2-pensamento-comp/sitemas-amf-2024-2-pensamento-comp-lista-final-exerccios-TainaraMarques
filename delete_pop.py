# Del -> Instrução que é usada para remover um item ou uma fatia de elementos de uma lista ou outro tipo de estrutura de dados, Não retorna o item removido, Pode ser usada para remover um item com base no índice ou para excluir a variável inteira, Pode ser usada em listas, dicionários e outros tipos de dados, incluindo a remoção de variáveis inteiras.

dicionario = {
    'abacaxi': 2,
    'banana': 6,
    'maça': 8
              }

del dicionario['abacaxi']
print(dicionario)

dicionario = {    
    'abacaxi': 2,
    'banana': 6,
    'maça': 8
              }

dicionario.pop('maça')
print(dicionario)