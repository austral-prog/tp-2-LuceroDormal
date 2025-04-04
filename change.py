def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")
    print("\nVuelto\n")
    print("Pesos:")
    vuelto= money-expense
    pesos= int(vuelto)
    print(f"{pesos}")
    print("Centavos:")
    centavos =int((vuelto - pesos) * 100)
    rint(f"{centavos}")
