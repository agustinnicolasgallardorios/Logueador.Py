print("Bienvenido al logeador, ingrese el nombre de usuario y contraseña correspondiente.")

usuario = input("Ingrese nombre de usuario ")
password = input("ingrese contraseña correspondiente ")

nombre_usuario = "Lastito"
password_usuario = "trunca123"
cuenta = 0

while cuenta < 2:
    if usuario == nombre_usuario:
        print("datos correctos")
        break
    else:
        print("los datos son incorrectos, ingreselos de nuevo")
        usuario = input("ingrese nuevamente el nombre de usuario ")
        password = input("ingrese nuevamente el password ")
        cuenta += 1

if cuenta == 2:
    print("Hemos bloqueado su cuenta")
