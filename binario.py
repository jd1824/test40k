def convertir(string: str):
    salida = ""
    for i in string:
        salida += str(format(ord(i), "08b"))
        salida += " "
    print(salida)



def convertir2(cadena: str):
    salida = ""
    for i in cadena.split():
        salida += chr(int(i, 2))
    print(salida)

convertir(" ")