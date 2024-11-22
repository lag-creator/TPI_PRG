import random

def opcion_a():
    lista_p = ["ESENCIA", "calcio", "casa", "auto", "avion", "tren", "sol", "lentes", "arbol", "planeta", "agua", "lluvia", "rojo", "azul", "amarillo", "verde", "programa"]
    palabra = lista_p[random.randint(0, (len(lista_p)) -1)]  # Palabra predeterminada
    letras_adivinadas = []  # Aca se guardan las letras adivinadas
    intentos = 3  # Número de intentos permitidos

    print()
    print("VAMOS A JUGAR")
    while intentos > 0:
        progreso = "".join(letra if letra in letras_adivinadas else "_" for letra in palabra)
        print("Palabra:", progreso)
        
        if progreso == palabra:
            print()
            print("perfecto. Has adivinado la palabra:", palabra)
            print()
            break
        letra = input("Adivina una letra: ").lower()
        if letra in letras_adivinadas:
            print("ya colocaste esa letra. Intenta otra vez.")
            continue
        letras_adivinadas.append(letra)
        if letra in palabra:
            print("excelente")
        else:
            intentos -= 1
            print(f"incorrecto. Te quedan {intentos} intentos.")

    if intentos == 0:
        print()
        print("mas suerte la proxima. La palabra era:", palabra)
        print()
    
def opcion_b():
    record = [0,0,0,0]
    estado = 1

    while estado == 1:

        incorrecta = 0
        correctas = 0
        error_elec = 1

        print(f"""            Bienvenido a Agilidad Numerica. 
                Selecione su dificultad. 
      Mientras más alto el valor, más dificil será.
        Records:
        D1: {record[0]}
        D2: {record[1]}
        D3: {record[2]}
        D4: {record[3]}""")

        while error_elec != 0:
            dificultad = input("Ingrese un valor entre 1 y 4: ")
        
            if dificultad == "exit":
                estado = 0
                incorrecta = 1
                error_elec = 0
            elif dificultad != "1" and dificultad != "2" and dificultad != "3" and dificultad != "4":
                error_elec = 1
                print("Error. Seleccione un valor valido.")
            else:
                error_elec = 0

        while incorrecta == 0:
            if dificultad == "1":
                num_min = 1
                num_max = 9
                cal_min = 0
                cal_max = 1
            elif dificultad == "2":
                num_min = 10
                num_max = 99
                cal_min = 0
                cal_max = 2
            elif dificultad == "3":
                num_min = 1
                num_max = 500
                cal_min = 0
                cal_max = 3
            elif dificultad == "4":
                num_min = 115
                num_max = 999
                cal_min = 2
                cal_max = 3
        
            cal = random.randint(cal_min,cal_max)

            lis_cal = ["+","-","x","/"]

            num1 = random.randint(num_min,num_max)
            num2 = random.randint(num_min,num_max)

            if cal == 0:
                solu = num1+num2
            elif cal == 1:
                solu = num1-num2
            elif cal == 2:
                solu = num1*num2
            elif cal == 3:
                num1 = random.randint(100,num_max)
                num2 = random.randint(5,99)
                solu = num1//num2
        
            print(f"""
        Resuelva el siguiente calculo: 
                            """)
            if cal == 3:
                print("""Esto es una division, ingrese el resultado sin considerar el resto. (Solo se permiten valores enteros)
                                """)
            print(f"""        {num1} {lis_cal[cal]} {num2}
                                """)
            respu = input("Respuesta: ")

            if respu == str(solu):

                print("Respuesta Correcta.")

                correctas = correctas + 1 
                if correctas > record[int(dificultad)]:

                    record[int(dificultad)-1] = correctas
            else:

                print(f"""Respuesta incorrecta. Fin del juego. Respondiste {correctas} veces seguidas de forma correcta. Dificultad {dificultad}. Reocord en esta dificultad {record[int(dificultad)-1]}.
                      """)

                incorrecta = 1

def opcion_c():
    print("piedra papel o tijera")
    opc = ["piedra","papel","tijera"]
    jugador = input("Elige: piedra, papel, tijera: ").lower()
    
    if jugador not in opc:
        print("Elija una opcion valida.")
        return opcion_c
    npc = random.choice(opc)
    print(f"La computadora eligio {npc}")

    if jugador == npc:
        print("Empate")
    elif (jugador == "piedra" and npc == "tijera") or \
        (jugador == "papel" and npc == "piedra") or \
        (jugador == "tijera" and npc == "papel" ):
        print("El jugador gana")
    else:
        print("El bot gana")
    opcion_c()

def opcion_d():
    print("adivinar numero")
    import random
    secreto = random.randint(1,20)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = int(input("Ingrese su intento (del 1 al 20): "))
        intento = int(intento)
        if intento < 1 or intento > 20:
            print("El numero debe estar entre 1 a 20")
            intentos += 1
        if intento < secreto:
            print("Su numero es muy bajo, intente de nuevo: ")
        elif intento > secreto:
            print("Su numero es muy alto, ingrese de nuevo: ")
        else:
            print(f"Ha acertado el numero {secreto}. ")
            adivinado = True
    adivinado = True

def opcion_f():        
    print("TA TE TI")
    respuesta="S"
    jugada = 0
    juego = False
    X=0
    Y=0
    resultado = ""
    matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
    # Dibuja Tablero
    def dibuja_matriz():
        print(" %c | %c | %c " % (matriz[0][0],matriz[0][1],matriz[0][2]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (matriz[1][0],matriz[1][1],matriz[1][2]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (matriz[2][0],matriz[2][1],matriz[2][2]))    
    # Valida el estado de la jugada en el tablero
    def valida(trn):
        global resultado
        # Horizontal y Vertical
        for i in range(0,3):
            if matriz[i][0] == matriz[i][1] == matriz[i][2] != " " or matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
                resultado="gana "+trn
                return True
        # Diagonal
        if matriz[0][0] == matriz[1][1] == matriz[2][2] != " " or matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
            resultado="gana "+trn
            return True
        # Todo lleno
        if " " not in matriz[0] and " " not in matriz[1] and " " not in matriz[2]:
            resultado="Empate"
            return True
        # Por Default
        return False
 
    def nuevo_juego():
        for i in range(0,3):
            matriz[i][0] = " " 
            matriz[i][1] = " " 
            matriz[i][2] = " "
 
    print("---------------------------------------")
    print("Tateti                                 ")
    print("---------------------------------------")
    while respuesta.upper()!="N":
        try:
            Turno="X"
            nuevo_juego()
            juego=False
            # Lazo del juego si gano o tablas
            if respuesta.upper()=="S":
                while juego==False:
                    dibuja_matriz()
                    print("Juega ",Turno," ",end="")
                    # exception del valor cuando es ENTER ''
                    try:
                       jugada=int(input("donde juega?(1-9):"))
                    except ValueError:
                        print("No es un numero")
                    except KeyboardInterrupt:
                        print("No es un numero")
                    else:
                        if jugada <=9 and jugada >=1:
                            jugada=jugada-1
                            Y = jugada/3
                            X = jugada%3
                        X = int(X)
                        Y = int(Y)
                        if matriz[Y][X] == " ":
                            matriz[Y][X] = Turno
                            juego=valida(Turno)
                            if Turno == "X":
                                Turno = "O"
                            else:
                                Turno = "X"
                        else:
                            print("Ocupada, intente otra jugada!")
                        # Cambio de turno
            if resultado != "" :
                print("***************************")
                print("Fin de la Jugada!!!!!!!!!!")
                print("***************************")
                print(resultado)
                print("***************************")
                dibuja_matriz()
            respuesta=input("Jugar Otra vez? (S/N)")
            resultado=""
        except KeyboardInterrupt:
            print ("Selecione una opcion correcta!!")
            respuesta=""
            resultado=""
    print("Fin. Gracias por Jugar.")

def mostrar_menu():
    print()
    print("/|-----------------------------------------------|\\")
    print("|| Bienvenido al Programa Interactivo de Play.in ||")
    print("\|-----------------------------------------------|/")
    print("1. AHORCADO")
    print("2. AGILIDAD NUMERICA")
    print("3. PIEDRA PAPEL TIJERA")
    print("4. ADIVINAR UN NUMERO")
    print("5. TA TE TI")
    print("6. CERRAR SISTEMA")

while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))    
    if opcion == 1:
        opcion_a()
    elif opcion == 2:
        opcion_b()
    elif opcion == 3:
        opcion_c()    
    elif opcion == 4:
        opcion_d()
    elif opcion == 5:
        opcion_f()    
    elif opcion == 6:
        print("CERRANDO SISTEMA")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
