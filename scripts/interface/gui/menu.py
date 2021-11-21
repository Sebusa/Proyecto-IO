import tkinter as tk

#ventana
screen = tk.Tk()
screen.geometry("700x500")

def start():

    welcomeText = "¡Bienvenido!"
    welcomeLabel = tk.Label(screen, text = welcomeText, justify = tk.CENTER, fg = "black",
                            bg = "white", font = "Roboto 15").pack(fill = tk.X)

    creditsText = "Elaborado por Grupo C"
    creditsLabel = tk.Label(screen, text = creditsText, fg = "black", bg = "white",
                            font = "Roboto 8 italic").pack(fill = tk.X, side = tk.BOTTOM)


    #labelHola = tk.Label(screen, text = text, bg = "blue")
    #labelHola.pack(side = tk.LEFT)
    #labelHola.pack(fill = tk.Y, expand = 1)
    #labelHola.pack()

    screen.mainloop()

start()