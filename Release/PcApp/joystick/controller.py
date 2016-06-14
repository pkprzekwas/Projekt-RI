import time
import math
import cmath

speed = 0
angle = 0


# wysylanie
def send(left, right):
    print(left, right)
    pass


# skalowanie predkosci + zabezpieczenie przed wyjsciem poza zakres -400:400
def scale(angle, speed):
    left = left_motor(angle, speed)
    right = right_motor(angle, speed)

    if left > 1:
        left = 1
    elif left < -1:
        left = -1

    if right > 1:
        right = 1
    elif right < -1:
        right = -1

    left = left * 400
    right = right * 400
    if speed < 0.1:
        left = 0
        right = 0
    return left, right


# predkosc niewyskalowana lewego kola
def left_motor(angle, speed):
    if 0 <= angle < 90:
        return speed
    elif 90 <= angle < 180:
        return (3 - (angle / 90) * 2) * speed
    elif 180 <= angle < 270:
        return -speed
    elif 270 <= angle <= 360:
        return (-7 + (angle / 90) * 2) * speed


# predkosc niewyskalowana prawego kola
def right_motor(angle, speed):
    if 0 <= angle < 90:
        return (-1 + (angle / 90) * 2) * speed
    elif 90 <= angle < 180:
        return speed
    elif 180 <= angle < 270:
        return (5 - (angle / 90) * 2) * speed
    elif 270 <= angle <= 360:
        return -speed


# obliczanie kata 0:360 w zaleznosci od polozenia joyisticka
def angle(axis_x, axis_y, speed):
    return cmath.phase(complex(axis_y, axis_x)) * 180 / math.pi + 180
