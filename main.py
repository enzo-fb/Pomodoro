import os
import time
from pynput import keyboard
running = True
# Função que será chamada sempre que uma tecla for pressionada
def on_press(key):   
    global running
    try:
        # Verifica se a tecla pressionada é 'Enter'
        if key == keyboard.Key.enter:
            print("Exiting...")
            running = False  # Sai do loop
            return False  # Interrompe o listener
    except AttributeError:
        print(f"Tecla especial pressionada: {key}")


# Inicia o listener para capturar os eventos de teclado

def segundos(x):
    print(x)
    time.sleep(1)
    if(x != 60):
        return segundos(x+1)
def pomodoro(tempo, descanso):
    min = 0
    seg = 0
    if descanso == True:
        while min != tempo:
            os.system('clear')
            print("-"*10+"Rest time".upper()+"-"*10)
            if seg<10:
                print(f"Time: {min}:0{seg}")
            else:
                print(f"Time: {min}:{seg}")
            time.sleep(1)
            seg +=1 
            if seg == 60:
                seg = 0
                min += 1
    else:
        while min != tempo:
            os.system('clear')
            print("-"*10+"Focus time".upper()+"-"*10)
            if seg<10:
                print(f"Time: {min}:0{seg}")
            else:
                print(f"Time: {min}:{seg}")
            time.sleep(1)
            seg +=1 
            if seg == 60:
                seg = 0
                min += 1

while True:
    print("-"*10+"Welcome Pomodoro Time"+"-"*10)   
    print("1 - Traditional Pomodoro\n2 - Edit times\n3 - Exit")
    escolha = input()     
    if(escolha == "1"):
        ciclos = 0
        with keyboard.Listener(on_press=on_press) as listener:
            while running:
                pomodoro(1,False)
                if not running:
                    break
                ciclos += 1
                if ciclos == 4:
                    pomodoro(15, True)
                    print("Returning to focus...")
                    ciclos = 0
                else: 
                    pomodoro(1,True)
                    print("Returning to focus...")
                    time.sleep(3)
                if not running:
                    break
            listener.join()

    elif (escolha == "2"):
        minutos_foco = input("Enter the focus time (in minutes):")
        minutos_descanso_menor = input("Enter the shorter break time (in minutes):")
        minutos_descanso_maior = input("Enter the longer break time (in minutes):")
        qntd_ciclos = input("Number of cycles until the long break:")
        pass
    elif(escolha == "3"):
        exit()
        