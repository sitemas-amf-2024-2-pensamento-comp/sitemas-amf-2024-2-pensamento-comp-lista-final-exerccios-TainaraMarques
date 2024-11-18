def media(n1,n2):
    media = (n1 + n2) / 2
    return media

def main():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    m = media(n1,n2)
    print (m)

main()