# room2.py
from bangtal import *
from shared import scene1, scene2, showMessage

# 두 번째 방의 객체 정의
door2 = Object("C://오소소플젝//RoomEscape//문-왼쪽-열림.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("C://오소소플젝//RoomEscape//문-오른쪽-닫힘.png")
door3.locate(scene2, 910, 270)
door3.show()

keypad = Object("C://오소소플젝//RoomEscape//키패드.png")
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object("C:/오소소플젝/RoomEscape/스위치.png")
switch.locate(scene2, 880, 440)
switch.show()

# Door2 동작 정의
def onMouseAction_door2(x, y, action):
    scene1.enter()
door2.onMouseAction = onMouseAction_door2

# Door3 동작 정의
door3.closed = True
door3.unlocked = False
def onMouseAction_door3(x, y, action):
    if not door3.unlocked:
        showMessage("문이 잠겨있다.")
    elif door3.closed:
        door3.setImage("C://오소소플젝//RoomEscape//문-오른쪽-열림.png")
        door3.closed = False
    else:
        endGame()
door3.onMouseAction = onMouseAction_door3

# Keypad 동작 정의
def onKeypad_door3():
    showMessage("철커덕")
    door3.unlocked = True
door3.onKeypad = onKeypad_door3

def onMouseAction_keypad(x, y, action):
    showKeypad("BANGTAL", door3)
keypad.onMouseAction = onMouseAction_keypad
