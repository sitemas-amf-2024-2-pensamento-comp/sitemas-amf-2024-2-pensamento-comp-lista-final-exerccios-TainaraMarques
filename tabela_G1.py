valores = [True, False]

print(f"{'Avaliação G1':^25} {'chovendo':^20} {'fazendo sol':^20} {'chovendo or fazendo sol':^15} {'Avaliacao G1 -> (chovendo or fazendo sol)':^25}")

for p in valores:
    for q in valores:
        for r in valores:
            p_or_q = q or r  #
            p_implies_qr = not p or p_or_q  # P3 -> (P1 or P2)
            
            # Exibindo os resultados
            print(f"{str(p):^25} {str(q):^20} {str(r):^20} {str(p_or_q):^15} {str(p_implies_qr):^25}")
