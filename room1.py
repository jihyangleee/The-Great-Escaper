# room1.py
from bangtal import *
from shared import scene1, scene2, showMessage

# 첫 번째 방의 객체 정의
door1 = Object("C://오소소플젝//RoomEscape//문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()

key = Object("C://오소소플젝//RoomEscape//열쇠.png")
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object("C://오소소플젝//RoomEscape//화분.png")
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

# 탁자 생성
table = Object("RoomEscape//table(2).png")  # 탁자 이미지 필요
table.locate(scene1, -20, 70)  # 탁자를 검정 벽 쪽으로 이동
table.setScale(0.4)  # 크기 조정
table.show()

# 노트북 생성
laptop = Object("RoomEscape//computer(5).png")  # 노트북 이미지 필요
laptop.locate(scene1, 70, 370)  # 노트북을 탁자 위로 위치 조정
laptop.setScale(0.07)  # 크기 조정
laptop.show()






# Door1 동작 정의
door1.closed = True
def onMouseAction_door1(x, y, action):
    if door1.closed:
        if key.inHand():
            door1.setImage("C://오소소플젝//RoomEscape//문-오른쪽-열림.png")
            door1.closed = False
        else:
            showMessage("열쇠가 필요해~~~")
    else:
        scene2.enter()
door1.onMouseAction = onMouseAction_door1

# Key 동작 정의
def onMouseAction_key(x, y, action):
    key.pick()
key.onMouseAction = onMouseAction_key

# Flowerpot 동작 정의
flowerpot.moved = False
def onMouseAction_flowerpot(x, y, action):
    if not flowerpot.moved:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
        flowerpot.moved = True
flowerpot.onMouseAction = onMouseAction_flowerpot
