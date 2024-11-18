def calcular_renda_liquida(renda, despesas):
    return renda - despesas

def verificar_elegibilidade(pontuacao_credito, parcela, renda_liquida):
    limite_parcela = renda_liquida * 0.30
    
    if pontuacao_credito >= 600 and parcela <= limite_parcela:
        return True, limite_parcela
    else:
        return False, limite_parcela

def main():
    renda = float(input("Digite a renda mensal do cliente (em reais): "))
    pontuacao_credito = int(input("Digite a pontuação de crédito do cliente (0 a 1000): "))
    despesas = float(input("Digite as despesas mensais do cliente (em reais): "))
    parcela = float(input("Digite o valor da parcela mensal do empréstimo (em reais): "))
    
    renda_liquida = calcular_renda_liquida(renda, despesas)
    print(f"\nRenda líquida: R${renda_liquida}")
    
    elegivel, limite_parcela = verificar_elegibilidade(pontuacao_credito, parcela, renda_liquida)
    
    if elegivel:
        print("O cliente é elegível para o empréstimo.")
    else:
        print("O cliente NÃO é elegível para o empréstimo.")
    
    if parcela > limite_parcela:
        print(f"A parcela mensal de R${parcela:.2f} ultrapassa 30% da renda líquida de R${renda_liquida}. O cliente pode ter dificuldades financeiras.")
    else:
        print(f"A parcela mensal de R${parcela} está dentro de 30% da renda líquida. O cliente pode pagar com mais facilidade.")

main()
