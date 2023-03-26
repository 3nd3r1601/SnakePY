import os,time,colorama,keyboard,random
highscore = ""
lastscore = ""
render = ""
renderX = 0
renderY = 0
pre = 0
pos = "25-10"
snake = ["22-10", "23-10", "24-10"]
alive = False
X = 25
Y = 10
dir = 2
food = "30-10"
valid = False
option = 1
score = 0
colors = [colorama.Fore.GREEN, colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
colorChoice = 1
color = colors[colorChoice]
colorSav = ""
vel = 1
velSav = 0
os.system("mode 50,22")
colorama.init(autoreset=True)
open("velocity.txt", "w").write(str(vel))
#Defino la función "render".
def render(pos, render, renderX, renderY, pre, snake, food, alive, score):
    print("                        ",score)
    renderX = 0
    renderY = 0
    for i in range(20):
        for a in range(50):
            render = str(renderX)+"-"+str(renderY)
            pre = renderX
            if render == pos:
                print(color+"▓",end="")
                renderX += 1
            elif render == food:
                print(colorama.Fore.RED+"O",end="")
                renderX += 1
            for i in range(len(snake)):
                if render == snake[i]:
                    print(color+"▓",end="")
                    renderX += 1
            if renderX == pre:
                print(colorama.Fore.YELLOW+"░",end="")
                renderX += 1
        print("")
        renderY += 1
        renderX = 0
#Opciones.
def options(option, color, colors, colorChoice, colorSav, vel, velSav):
    velSav = open("velocity.txt", "r")
    vel = int(velSav.read())
    colorSav = open("color.txt", "r")
    color = colorSav.read()
    while True:
        os.system("cls")
        print("")
        print("")
        print(colorama.Fore.GREEN+"                               ╭═════╮")
        print(colorama.Fore.GREEN+"           ╭═══┳═══┳═══┳═══╭═══╝ O  "+colorama.Fore.RED+"┓"+colorama.Fore.GREEN+"║")
        print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ╭═╗ O  "+colorama.Fore.RED+"┛"+colorama.Fore.GREEN+"║")
        print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╰═════╯")
        print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ "+colorama.Fore.RESET+"SnakePY")
        print(colorama.Fore.GREEN+"           ╰═╯═══┻═══┻═══┻═══╯")
        print("")
        print("")
        print("")
        if option == 1:
            print("          ■ COLOR: ",end="")
        else:
            print("            COLOR: ",end="")
        if color == colorama.Fore.GREEN:
            print(color+"GREEN")
            colorChoice = 0
        elif color == colorama.Fore.RED:
            print(color+"RED")
            colorChoice = 1
        elif color == colorama.Fore.BLUE:
            print(color+"BLUE")
            colorChoice = 2
        elif color == colorama.Fore.YELLOW:
            print(color+"YELLOW")
            colorChoice = 3
        elif color == colorama.Fore.MAGENTA:
            print(color+"MAGENTA")
            colorChoice = 4
        elif color == colorama.Fore.CYAN:
            print(color+"CYAN")
            colorChoice = 5
        print("")
        if option == 2:
            print("          ■ VELOCITY: ", vel)
        else:
            print("            VELOCITY: ", vel)
        print("")
        if option == 3:
            print("          ■ BACK")
        else:
            print("            BACK")
        print("")
        print("")
        print("")
        print("")
        if keyboard.is_pressed("up_arrow") or keyboard.is_pressed("w") and option != 1:
            option += -1
        elif keyboard.is_pressed("down_arrow") or keyboard.is_pressed("s") and option != 3:
            option += 1
        elif keyboard.is_pressed("right_arrow") or keyboard.is_pressed("d"):
            if option == 1 and colorChoice != 5:
                colorChoice += 1
                color = colors[colorChoice]
                colorSav = open("color.txt", "w")
                colorSav.write(color)
            elif option == 2 and vel != 5:
                vel += 1
                velSav = open("velocity.txt", "w")
                velSav.write(str(vel))
            elif option == 3:
                option = 1
                break
            else:
                pass
        elif keyboard.is_pressed("left_arrow") or keyboard.is_pressed("a"):
            if option == 1 and colorChoice != 0:
                colorChoice += -1
                color = colors[colorChoice]
                colorSav = open("color.txt", "w")
                colorSav.write(color)
            if option == 2 and vel != 1:
                vel += -1
                velSav = open("velocity.txt", "w")
                velSav.write(str(vel))
        time.sleep(.15)
#Bucle de la aplicación.
while True:
#Menú.
    os.system("cls")
    print("")
    print("")
    print(colorama.Fore.GREEN+"                               ╭═════╮")
    print(colorama.Fore.GREEN+"           ╭═══┳═══┳═══┳═══╭═══╝ O  "+colorama.Fore.RED+"┓"+colorama.Fore.GREEN+"║")
    print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ╭═╗ O  "+colorama.Fore.RED+"┛"+colorama.Fore.GREEN+"║")
    print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╰═════╯")
    print(colorama.Fore.GREEN+"           ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ "+colorama.Fore.RESET+"SnakePY")
    print(colorama.Fore.GREEN+"           ╰═╯═══┻═══┻═══┻═══╯")
    print("")
    print("")
    if option == 1:
        print("          ■ PLAY")
    else:
        print("            PLAY")
    lastscore = open("lastscore.txt", "r")
    print("                         Last Score:"+lastscore.read())
    if option == 2:
        print("          ■ OPTIONS")
    else:
        print("            OPTIONS")
    highscore = open("highscore.txt", "r")
    print("                         Highscore:"+colorama.Fore.YELLOW+highscore.read())
    if option == 3:
        print(colorama.Fore.RED+"          ■ EXIT")
    else:
        print("            EXIT")
    print("")
    print("")
    print("")
    print("")
    if keyboard.is_pressed("up_arrow") or keyboard.is_pressed("w") and option != 1:
        option += -1
    elif keyboard.is_pressed("down_arrow") or keyboard.is_pressed("s") and option != 3:
        option += 1
    elif keyboard.is_pressed("right_arrow") or keyboard.is_pressed("d"):
        if option == 1:
            alive = True
            snake = ["22-10", "23-10", "24-10"]
            X = 25
            Y = 10
            dir = 2
            food = "30-10"
            colorSav = open("color.txt", "r")
            color = colorSav.read()
        elif option == 2:
            option = 1
            vel = int(open("velocity.txt", "r").read())
            options(option=option,color=color,colors=colors,colorChoice=colorChoice,colorSav=colorSav,vel=vel,velSav=velSav)
        elif option == 3:
            os._exit()
    time.sleep(.15)
#Bucle del juego.
    while alive:
#Detecto las pulsaciones y dependiendo de la dirección muevo la cabeza.
        if keyboard.is_pressed("up_arrow") or keyboard.is_pressed("w") and dir != 3:
            dir = 1
        if keyboard.is_pressed("left_arrow") or keyboard.is_pressed("a") and dir != 2:
            dir = 4
        if keyboard.is_pressed("down_arrow") or keyboard.is_pressed("s") and dir != 1:
            dir = 3
        if keyboard.is_pressed("right_arrow") or keyboard.is_pressed("d") and dir != 4:
            dir = 2
        if dir == 1:
            Y += -1
        elif dir == 2:
            X += 1
        elif dir == 3:
            Y += 1
        elif dir == 4:
            X += -1
#Hago el movimiento del cuerpo de la serpiente y la aparición de comida si en ese momento la posición de la cabeza es igual a la de la comida.
        if pos != food:
            snake.remove(snake[0])
        else:
            score += 1*vel
            valid = False
            while not valid:
                food = str(random.randint(0,49))+"-"+str(random.randint(0,19))
                valid = True
                for i in range(len(snake)):
                    if food == snake[i]:
                        valid = False
        snake.append(pos)
        pos = str(X)+"-"+str(Y)
#Detecto si ha chocado.
        for i in range(len(snake)):
            if pos == snake[i]:
                alive = False
        if X<0 or X>49 or Y<0 or Y>19:
            alive = False
#Renderizo.
        os.system("cls")
        render(pos=pos,render=render,renderX=renderX,renderY=renderY,pre=pre,snake=snake,food=food,alive=alive,score=score)
#Regulo la velocidad.
        if dir == 2 or dir == 4:
            time.sleep(.05/vel)
        else:
            time.sleep(.1/vel)
#Animación de la muerte.
    if pos != "25-10":
        os.system("cls")
        pos = "98-98"
        render(pos=pos,render=render,renderX=renderX,renderY=renderY,pre=pre,snake=snake,food=food,alive=alive,score=score)
        for i in range(len(snake)):
            os.system("cls")
            snake.remove(snake[len(snake)-1])
            render(pos=pos,render=render,renderX=renderX,renderY=renderY,pre=pre,snake=snake,food=food,alive=alive,score=score)
            time.sleep(.2)
        time.sleep(1)
        new = str(score*vel)
        lastscore = open("lastscore.txt", "w")
        lastscore.write(new)
        lastscore = open("lastscore.txt", "r")
        highscore = open("highscore.txt", "r")
        if int(lastscore.read()) > int(highscore.read()):
            highscore = open("highscore.txt", "w")
            highscore.write(new)
        os.system("cls")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(colorama.Fore.RED+"      ░██████╗░░█████╗░███╗░░░███╗███████╗")
        print(colorama.Fore.RED+"      ██╔════╝░██╔══██╗████╗░████║██╔════╝")
        print(colorama.Fore.RED+"      ██║░░██╗░███████║██╔████╔██║█████╗░░")
        print(colorama.Fore.RED+"      ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░")
        print(colorama.Fore.RED+"      ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗")
        print(colorama.Fore.RED+"      ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
        print("")
        print(colorama.Fore.RED+"        ░█████╗░██╗░░░██╗███████╗██████╗░")
        print(colorama.Fore.RED+"        ██╔══██╗██║░░░██║██╔════╝██╔══██╗")
        print(colorama.Fore.RED+"        ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝")
        print(colorama.Fore.RED+"        ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗")
        print(colorama.Fore.RED+"        ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║")
        print(colorama.Fore.RED+"        ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
        time.sleep(3)
        pos = "25-10"
        score = 0
