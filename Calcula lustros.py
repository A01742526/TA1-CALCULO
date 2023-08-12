def main():
    #escribe tu código abajo de esta línea
    pass
#pedir información
nacimiento= int(input("Introduzca el año de su nacimiento:"))
actual= int(input("Introduzca el año actual:"))
#cálculo
lustros= float(actual-nacimiento)/5
#mostrar resultados
print("Los lustros que has vivido son:",lustros)

if __name__ == '__main__':
    main()
