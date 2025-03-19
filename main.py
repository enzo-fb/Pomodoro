import os
import time
# Função que será chamada sempre que uma tecla for pressionada
focus = "-"*10+"Focus time".upper()+"-"*10
restTime = "-"*10+"Rest time".upper()+"-"*10
def pomodoro(tempo, descanso):
    min = tempo
    seg = 59
    if descanso == True:
            while min >= 0:
                os.system('clear')
                print(restTime + "\n")
                if seg<10:
                    print(f"Time: {min}:0{seg}".center(len(restTime)))
                else:
                    print(f"Time: {min}:{seg}".center(len(restTime)))
                time.sleep(1)
                seg -=1 
                if seg == 0:
                    seg = 59
                    min -= 1         
    else:
            while min >= 0 : 
                os.system('clear')
                print(focus+ "\n")
                if seg<10:
                    print(f"Time: {min}:0{seg}".center(len(focus)))
                else:
                    print(f"Time: {min}:{seg}".center(len(focus)))
                time.sleep(1)
                seg -=1 
                if seg == 0:
                    seg = 59
                    min -= 1

            

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
                    decisao = int (input("Enter 1 to restart the cycle or 2 to go back to the main menu:\n"))
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
        minutos_descanso_menor = int (input("Enter the shorter break time (in minutes):\n"))
        minutos_descanso_maior = int (input("Enter the longer break time (in minutes):\n"))
        qntd_ciclos = int (input("Number of cycles until the long break:\n"))
        ciclos = 0
        while True:
                pomodoro(minutos_foco,False)
                ciclos += 1
                if ciclos == qntd_ciclos:
                    pomodoro(minutos_descanso_maior, True)
                    decisao = int (input("Enter 1 to restart the cycle or 2 to go back to the main menu:\n"))
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
        print("Exiting...")
        exit()
        