idade = 25
sexo = "feminino"

if idade < 18:
    if sexo == "masculino":
        print("Menor de idade do sexo masculino.")
    else:
        print("Menor de idade do sexo feminino.")
elif idade >= 18 and idade < 60:
    if sexo == "masculino":
        print("Adulto do sexo masculino.")
    else:
        print("Adulta do sexo feminino.")
else:
    if sexo == "masculino":
        print("Idoso do sexo masculino.")
    else:
        print("Idosa do sexo feminino.")