def remover_duplicados():
    lista = [1, 2, 5, 6, 6, 8, 9, 8, 6, 5, 3, 3]
    lista_unica = []  
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)  
    return lista_unica

print(remover_duplicados())
