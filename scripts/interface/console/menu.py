import scripts.interface.console.screen as screen
import scripts.interface.console.options as Options

def start():
    
    screen.clearConsole()
    print("         ¡Bienvenidos al programa!\n")

    while True:
        print("1) Algoritmo Dijkstra")
        print("2) Algoritmo simplex (Método de la gran M)")
        print("x) Salir del programa.")

        options = input("¿Qué opción deseas?: ")

        if options == "x" or options == "X": break
        else:

            if options == "1":
                screen.clearConsole()
                Options.dijkstraOptions()

            elif options == "2":
                screen.clearConsole()
                Options.bigMOptions()

            else: 
                screen.clearConsole()
                print("Opción inválida.")

        input("Presiona cualquier tecla para continuar: ")
        screen.clearConsole()

    print("¡Adiós!")