# coding: utf-8
 
# comment

# 10 элементов

import turtle  # для Linux   apt-get install tkinter
import random
import sys

x = random.randint(1, 100)      # случайное число

# print('x = ', x)

def gotoxy(x, y):
    ''' Перемещение курсора
    '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    
def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)
    
def draw_gibbet(step): 
    if step == 1:
        draw_line(-160, -100, -160, 80)    # вертикальный столб
    elif step == 2:
        draw_line(-160, 80, -40, 80)
    elif step == 3:    
        draw_line(-160, 40, -120, 80)
    elif step == 4:    
        draw_line(-100, 80, -100, 30)
    elif step == 5:    
        gotoxy(-100, -10)
        turtle.circle(20)    
    elif step == 6:
        draw_line(-100, -10, -100, -50) # туловище
    elif step == 7:    
        draw_line(-100, -20, -120, -30) # рука левая
    elif step == 8:    
        draw_line(-100, -20, -80, -30) # рука левая
    elif step == 9:
        draw_line(-100, -50, -120, -60) # нога левая
    elif step == 10:
        draw_line(-100, -50, -80, -60)  # нога правая    
    else:
        pass
        
    
turtle.speed(0)    
turtle.color("blue")
    
try_count = 0

answer = turtle.textinput("Играть?", "Y/N")
if answer == 'N':
    sys.exit(13)

while True:        
    gotoxy(-200, 250)    
    turtle.write("Я загадал число от 1 до 100.\n Попробуй угадать?", font=("Arial", 16, "normal"))
    
    number = turtle.numinput("Введите число", "Число")
    
    
    if number == x:
        gotoxy(150, 250)
        turtle.color("green")
        turtle.write("Вы угадали", font=("Arial", 16, "normal"))
        break
    elif number == -13:
        break
    else:
        gotoxy(-150, 100)
        turtle.write("Неверно", font=("Arial", 16, "normal"))
        gotoxy(200, 200 - try_count * 10)
        if number < x:
            turtle.write("Загаданное число больше")
        else:
            turtle.write("Загаданное число меньше")
            
        try_count = try_count + 1    
        draw_gibbet(try_count)    
        
        if try_count == 10:
            turtle.color("red")
            gotoxy(-150, 100)
            turtle.write("Вы проиграли!")
            break
            
# PATH

inp = input('Нажмите ENTER для выхода')