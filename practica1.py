import re

#-------------------------Para el menu principal-------------------------
def menu():
    print("---MENU---\n")
    print("1. Ingresar alfabeto\n")
    print("2. Leer 2 cadenas\n")
    print("3. Comprobar Prefijo, Sufijo o Subcadena\n")
    print("4. Generar lenguajes aleatorios\n")
    print("5. Generar diferencia de lenguajes\n")
    print("6. Obtener potencia de alfabeto\n")
    print("7. Incisos\n")
    opc = int(input("Ingrese una opcion valida: "))
    return opc

#-------------------------Para ingresar alfabeto-------------------------
def punto1(miniO):
    alfabeto = []
    carac = 0
    i=0
    #Para ingresar alfabeto caracter por caracter
    if miniO == 1:
        while (carac!='-1'):
            print("Introduza el caracter del alfabeto", i, "(-1 para terminar): ")
            carac = input()
            alfabeto.append(carac)
            i+=1
        alfabeto.pop()
    #Para ingresar alfabeto por rango
    if miniO == 2:
        rango1 = input("Ingresa el caracter del rango inicial: ")
        rango2 = input("Ingresa el caracter del rango final: ")
        for i in range(ord(rango1), ord(rango2)+1):
            alfabeto.append(chr(i))
    return alfabeto

#-------------------------Para validar que las cadenas ingresadas pertenezcan al alfabeto-------------------------
def punto2(cad1, cad2, alfabeto):
    #Aqui lo de chat gpt
    
    if any(cad1.startswith(caracter) for caracter in alfabeto):
        #Si esto es verdad, verificar la cadena 2, de ser falso, pedir cadenas nuevamente
        print("La cadena ingresada está conformada por caracteres de la lista.")
    else:
        print("La cadena ingresada NO está conformada por caracteres de la lista.")



    '''if all(caracter in alfabeto for caracter in cad1):
        #Si esto es verdad, verificar la cadena 2, de ser falso, pedir cadenas nuevamente
        print("La cadena ingresada está conformada por caracteres de la lista.")
    else:
        print("La cadena ingresada NO está conformada por caracteres de la lista.")'''

#-------------------------Para el switch de la opcion seleccionada del menu-------------------------
def hazMenu(o):
    AlfaSigma=[]
    if o == 1:
        print("1. Ingresar alfabeto caracter por caracter\n")
        print("2. Ingresar el alfabeto por rango\n")
        miniOpc = int(input("Ingresa una opcion: "))
        if miniOpc == 1 or miniOpc == 2:
            AlfaSigma=punto1(miniOpc)
        else:
            print("¡¡Ingrese una opcion valida!!")
            return 0
    elif o == 2:
        if len(AlfaSigma) == 0:
            print("Debe ingresar el alfabeto primero, gracias :)")
            return 0
        else:
            valida = False
            while(not valida):
                w1 = input("Ingrese la cadena numero 1: ")
                w2 = input("Ingrese la cadena numero 2: ")
                valida = punto2(w1, w2, AlfaSigma)
        
            
            
#-------------------------Main-------------------------
def main():
    opcMenu = menu()
    hazMenu(opcMenu)

if __name__ == "__main__":
    main()