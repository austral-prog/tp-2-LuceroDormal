def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")


    print("Vuelto")


    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")
