from PIL import ImageGrab
import os
import pyautogui as pq
import keyboard

def Jump():
    #pq.screenshot('C:\\Users\\Professional\\PycharmProjects\\app1\\screen.png')
    #f = Image.open('C:\\Users\\Professional\\PycharmProjects\\app1\\screen.png')
    #g=f.load()
    x=pq.position().x
    y=pq.position().y
    z=pq.pixel(x, y)
    if z[0]<90 or pq.pixel(x-20, y)[0]<90 or pq.pixel(x-40, y)[0]<90 or pq.pixel(x-30, y-40)[0]<90:
        pq.keyDown('space')

            #pq.keyDown('space')
            #pq.moveTo(700,520)


def Jump1():
    f=ImageGrab.grab()
    x = pq.position().x
    y = pq.position().y
    z = pq.pixel(x, y)
    c=True
    print(f.getpixel((x, y)))
    for i in range(0,160,5):
        if f.getpixel((x - i, y))[0] < 90:
            if c:
                pq.keyDown('space')
                c=False
    for i in range(-30,120, 10):
        if f.getpixel((x - i, y-30))[0] < 90:
            pq.keyDown('space')
    #pq.keyUp('space')
    s+=0.01
    if s==1:
        pq.move(f,0)
        s=0

s=0
while(True):
    f = ImageGrab.grab()
    x = pq.position().x
    y = pq.position().y
    z = pq.pixel(x, y)
    c = True
    print(f.getpixel((x, y)))
    for i in range(0, 160, 5):
        if f.getpixel((x - i, y))[0] < 90:
            if c:
                pq.keyDown('space')
                c = False
    for i in range(-30, 120, 10):
        if f.getpixel((x - i, y - 30))[0] < 90:
            pq.keyDown('space')
    # pq.keyUp('space')
    s += 0.01
    if s == 1:
        pq.move(s, 0)
        s = 0

