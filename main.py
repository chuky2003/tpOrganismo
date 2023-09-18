
logones = ["B959263", "C569853", "T698952", "Z698563"]
roles = ["SUPERIOR", "ADJUNTO", "TEMPORARIO", "TERCERIZADO"]
contraseñas = ["B959263", "C569853", "T698952", "Z698563"]

permisosRol = {
    "SUPERIOR": [1, 3, 4],
    "ADJUNTO": [1],
    "TEMPORARIO": [3, 1],
    "TERCERIZADO": [1, 5]
}

def loguearse():
    intentos = 3

    while intentos > 0:
        logon = input("Ingrese su logon: ")
        contraseña = input("Ingrese su contraseña: ")
        if logon in logones and contraseña in contraseñas:
            rol = roles[logones.index(logon)]
            return rol
        else:
            intentos -= 1
            print("Logon o contraseña incorrectos. Intentos restantes:", intentos)

    return None


def verificar_permisos(rol, tipo_de_acto):
    if rol in permisosRol and tipo_de_acto in permisosRol[rol]:
        return True
    else:
        return False

rol = loguearse()

if rol:
    print("Bienvenido, usted ha iniciado sesión como:", rol)
    tipo_de_acto = int(input("Ingrese el tipo de acto que desea realizar: "))

    if verificar_permisos(rol, tipo_de_acto):
        print("Usted tiene permiso para realizar este tipo de acto.")
    else:
        print("Usted no tiene permiso para realizar este tipo de acto.")
else:
    print("Ha excedido el número de intentos permitidos. Por favor, contacte al administrador.")