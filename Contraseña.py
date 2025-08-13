contraseña = "gomarojanosemoja"

while True:
    passwd = input("Ingrese la contraseña: ")

    if passwd == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña erronea, vuelva a intentarlo")