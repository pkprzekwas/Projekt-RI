import pygame
from pygame import *
import time
import math

pygame.init()
pygame.joystick.init()

speed = 0
angle = 0

#wysylanie
def send(left,right):
    print('Left motor: ',left)
    print('Right motor: ',right)

#skalowanie predkosci + zabezpieczenie przed wyjsciem poza zakres -400:400
def scale(angle,speed):

    left = left_motor(angle,speed)
    right = right_motor(angle,speed)

    if left>1:
        left = 1
    elif left<-1:
        left = -1

    if right>1:
        right=1
    elif right<-1:
        right=-1

    left = left*400
    right = right*400

    return left,right


#predkosc niewyskalowana lewego kola
def left_motor(angle, speed):
    if angle==90:
        return speed
    elif angle==270:
        return -speed
    else:
        if angle>=0 and angle<90:
            return speed
        elif angle>90 and angle<180:
            return (3 - (angle/90)*2)*speed
        elif angle>=180 and angle<270:
            return -speed
        elif angle>270 and angle<=360:
            return (-7 + (angle/90)*2)*speed

#predkosc niewyskalowana prawego kola
def right_motor(angle, speed):
    if angle==90:
        return speed
    elif angle==270:
        return -speed
    else:
        if angle>=0 and angle<90:
            return (-1 + (angle/90)*2)*speed
        elif angle>90 and angle<180:
            return speed
        elif angle>=180 and angle<270:
            return (5 - (angle/90)*2)*speed
        elif angle>=270 and angle<360:
            return -speed

#obliczanie kata 0:360 w zaleznosci od polozenia joyisticka
def angle(axis_x,axis_y,speed):
    if axis_y>0 and axis_x>0:
        return (math.asin(axis_y/speed)*180/math.pi)
    elif axis_y>0 and axis_x<0:
        return (180 - math.asin(axis_y/speed)*180/math.pi)
    elif axis_y<0 and axis_x<0:
        return (180 + math.asin(abs(axis_y/speed))*180/math.pi)
    elif axis_y<0 and axis_x>0:
        return (360 - math.asin(abs(axis_y/speed))*180/math.pi)

if __name__ == "__main__":
    # Tells the number of joysticks/error detection
    joystick_count = pygame.joystick.get_count()
    print ("There is ", joystick_count, "joystick/s")
    if joystick_count == 0:
        print ("Error, I did not find any joysticks")
    else:
        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()
    while 1: #petla wykonuje sie caly czas - trzeba ew. ustalic warunek jej zakonczenia - wylaczenie robota/tryb automatyczny?
        for event in pygame.event.get():  # User did something
            axes = my_joystick.get_numaxes()
            axis_y = my_joystick.get_axis(3)*(-1)
            axis_x = my_joystick.get_axis(4)
            speed = math.sqrt(axis_y**2 + axis_x**2)    #promien r we wspolrzednych biegunowych
            #kat 0:360
            angle = angle(axis_x,axis_y,speed)
            send(scale(angle,speed))
  #  pygame.quit() #uzywane dopiero, gdy bedziemy wiedzieli kiedy zakonczyc petle - wylaczenie robota/tryb automatyczny?