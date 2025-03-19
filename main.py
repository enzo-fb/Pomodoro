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
        while True:
                pomodoro(25,False)
                ciclos += 1
                if ciclos == 4:
                    pomodoro(15, True)
                    decisao = input("Enter 1 to restart the cycle or 2 to go back to the main menu")
                    if decisao == 2:
                        break
                    print("Returning to focus...")
                    ciclos = 0
                else: 
                    pomodoro(5,True)
                    print("Returning to focus...")
                    time.sleep(3)
        pass
    elif (escolha == "2"):
        minutos_foco = int(input("Enter the focus time (in minutes):"))
        minutos_descanso_menor = int (input("Enter the shorter break time (in minutes):"))
        minutos_descanso_maior = int (input("Enter the longer break time (in minutes):"))
        qntd_ciclos = int (input("Number of cycles until the long break:"))
        ciclos = 0
        while True:
                pomodoro(minutos_foco,False)
                ciclos += 1
                if ciclos == qntd_ciclos:
                    pomodoro(minutos_descanso_maior, True)
                    decisao = input("Enter 1 to restart the cycle or 2 to go back to the main menu")
                    if decisao == 2:
                        break
                    print("Returning to focus...")
                    ciclos = 0
                else: 
                    pomodoro(minutos_descanso_menor,True)
                    print("Returning to focus...")
                    time.sleep(3)
        pass
    elif(escolha == "3"):
        exit()
        