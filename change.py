def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto\n")
    print("Pesos:")
    vuelto= money-expense
    pesos= int(vuelto)
    print(pesos)
    print("Centavos:")
    centavos =int((vuelto - pesos) * 100)
    print(centavos)
