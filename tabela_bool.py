valores = [True, False]

print(f"{'A':^5} {'B':^5} {'C':^5} {'A || (B && C)':^20} {'!A && B && C':^20} {'!(A && B && !C)':^20}")

for A in valores:
    for B in valores:
        for C in valores:
            expr1 = A or (B and C)
            expr2 = (not A) and B and C
            expr3 = not (A and B and not C)
            
            print(f"{A:^5} {B:^5} {C:^5} {str(expr1):^20} {str(expr2):^20} {str(expr3):^20}")
