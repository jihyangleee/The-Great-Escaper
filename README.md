# The Great Escaper
<img width="1006" alt="image" src="https://github.com/user-attachments/assets/839d33d1-f583-413f-96e2-c034ea3341d8">


**The Great Escaper** – 방탈출 게임
-	The great escaper는 총 3개로 구성되어 있는 방에 있는 단서를 찾아야 탈출할 수 있는 게임입니다.
-	방탈출을 해서 단서를 찾아야 하는 이유는 다음과 같습니다.
범죄가 일어난 탐정 사무실이 있습니다. 탐정사무실에서 마지막 방인 침실에서 살인사건이 일어났습니다.<br>피해자인 탐정은 죽기 직전까지도 범인으로부터 협박을 받고 있었습니다.<br>
두번째 방에서 용의자들의 실루엣을 두고 그 범죄자가 누군지 밝혀내려고 했던 것으로 보입니다. 마지막 방에서 지문이 나왔으니 실루엣과 지문을 통해 범인을 밝혀내야 합니다. 
## Table of contents	
1.	시작환경
2.	게임방법
3.	게임구현 방법
4.	Reference

## 시작 환경
Python 기반 방탈출 게임 라이브러리를 사용하려면 32비트 환경이 필요합니다. (python8-32bit 환경 권장) , https://github.com/bosornd/bangtal/releases 여기서 v0.4.0 bangtal library를 다운받으면 됩니다. Bangtal.dll은 window환경에 있으며 bangtal파일은 python8파일에 있습니다. 이렇게 준비가 끝나면 함수를 추가하거나 객체를 추가하여 방을 꾸미고 단서를 넣어 방탈출 게임을 만듭니다.

## 게임 방법
- Demo Video
  
[![The Great Escaper](https://img.youtube.com/vi/10o4dw1W-zs/0.jpg)](https://youtu.be/10o4dw1W-zs)

- 게임화면
 
![image](https://github.com/user-attachments/assets/d3652ede-512f-4624-aea7-161aa371313c)


게임이 시작되기 전 억울하게 죽은 탐정이 확보해야 할 것들을 말해주고 있습니다.
게임 방법을 선택하면 게임을 하는 간단한 방법 같은 것들이 나옵니다. (클릭, 드래그를 해야한다는 것, 단서를 찾아야 방탈출을 할 수 있다는 것.) 

![image](https://github.com/user-attachments/assets/d2668463-d9dc-44e5-9516-dc831cd4b882)

게임이 시작되었습니다. 먼저 컴퓨터 쪽으로 가서 힌트를 방을 탈출할 수 있는 힌트를 얻으면 됩니다.

<img width="940" alt="image" src="https://github.com/user-attachments/assets/48fda8da-859b-4b7a-8090-199acf8dcae8">

힌트로 문장을 적어주었는데 방에 있는 물건들을 잘 조합해보면 답을 찾을 수 있습니다. 

<img width="940" alt="image" src="https://github.com/user-attachments/assets/5bbc24d7-bd64-47bc-87c0-f11e3b7fe694">

(컴퓨터, 빛, 소파를 영어로 바꿔서 앞글자를 조합해보면 됩니다)

<img width="940" alt="image" src="https://github.com/user-attachments/assets/02abd6b8-68cd-4e90-8cb7-01e374afe5b9">

Computer, light, sofa 이렇게 영어로 바꾼 후 c,l,s를 화살표를 클릭하여 찾으면 문이 열립니다. 

<img width="940" alt="image" src="https://github.com/user-attachments/assets/7130cb5a-8cb1-4bac-965d-f5e5010ba0ab">

벽에 붙여 있는 실루엣을 보고 힌트에 맞는 실루엣을 선택하여 오른쪽으로 드래그하면 됩니다. 그러면 스위치가 있습니다. <br> 그것을 누르면 방의 불이 꺼지면서 ‘BANGTAL’이라는 글자가 나옵니다.

![image](https://github.com/user-attachments/assets/25c7a064-2337-4a07-942c-0ad988f831ff)

‘BANGTAL’이 나온 것을 알 수 있습니다.

![image](https://github.com/user-attachments/assets/c03606bf-a9c5-4b3f-9f15-8b00c379a358)

문을 열기 위해 클릭해보면 하나의 창이 뜹니다. 거기에 방금 전에 보았던 단어를 입력하면 문이 열립니다. 

![image](https://github.com/user-attachments/assets/65275f9e-4ae0-4e90-a5f8-b36e20590867)

![image](https://github.com/user-attachments/assets/77c49b07-924c-428d-8614-10540f36819a)

살인사건이 일어난 마지막 방입니다. Warning과 침대를 옆으로 옮기면 단서가 나옵니다.

![image](https://github.com/user-attachments/assets/b56f2fad-fbc2-41d2-bb48-c51fbfe3e22a)

침대를 옮기니 지문이 나왔습니다. 지문의 방향을 보면 1시방향으로 기울어져 있음을 알 수 있습니다. <br>1을 적으면 마지막 방을 탈출할 수 있는 힌트가 나올 것입니다.

![image](https://github.com/user-attachments/assets/7edca17a-0b82-4025-a9e9-5b82aeba64f5)

시계를 옆으로 밀면 방을 나갈 수 있는 열쇠가 주어집니다.

![image](https://github.com/user-attachments/assets/294af7fc-0226-453a-b10b-08444f370a69)

방탈출에 성공했습니다.

![image](https://github.com/user-attachments/assets/ad6c2b69-8866-438c-b70a-3fe0a12ad9a3)

찾은 물품을 기록하는 공간입니다. 5초후에 게임이 종료됩니다. 


## 게임 구현 방법
살인사건이 일어난 마지막 방을 구현한 방법에 대해 설명하겠습니다.
(bangtal library, open source를 이용함)<br>
마지막 방 구현
``` python
scene3 = Scene("룸3", "RoomEscape//배경4.png")


fingerprint = Object("RoomEscape//rotated_지문.png")
fingerprint.locate(scene3,300,30)
fingerprint.setScale(0.6)
fingerprint.show()



bed = Object("RoomEscape//bed.png")
bed.locate(scene3,350,55)
bed.setScale(0.5)
bed.show()

caution = Object("RoomEscape//caution.png")
caution.locate(scene3,400,55)
caution.setScale(0.09)
caution.show()


key = Object("RoomEscape//열쇠.png")
key.setScale(0.2)
key.locate(scene3, 60, 550)
key.show()

clock = Object("RoomEscape//clock.png")
clock.locate(scene3,10,500)
clock.setScale(0.4)
clock.show()
```
방을 구현할 때 필요한 물건들은 Obejct클래스를 이용해서 불러옵니다. 

``` python
caution.moved = False
def onMouseAction_caution(x, y, action):
    global caution
    if caution.moved == False:
        if action == MouseAction.DRAG_LEFT:
            caution.locate(scene3, 200, 55)
            caution.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            caution.locate(scene3, 600, 55)
            caution.moved = True
caution.onMouseAction = onMouseAction_caution
```
주의 표시를 drag를 통해 옆으로 이동시킬 수 있도록 합니다.

```python
bed.moved = False
def onMouseAction_bed(x, y, action):
    global bed
    if bed.moved == False:
        if action == MouseAction.DRAG_LEFT:
            bed.locate(scene3, 150, 55)
            bed.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            bed.locate(scene3, 550, 55)
            bed.moved = True
bed.onMouseAction = onMouseAction_bed
```
침대를 옆으로 이동시켜 지문이 보일 수 있도록 합니다.

```python
import threading
global fingerpint_used
  # 지문 클릭 여부
door3_used = False  # 문 클릭 여부

def onMouseAction_fingerprint(x, y, action):
    global fingerprint_used
    if fingerprint_used:
        showCustomMessage("범인의 지문을 획득했네! 이제 증거를 찾았으니 키를 찾아 방을 나가면 되겠네!\n지문이 가리키는 방향을 잘보고 시계의 시침이 가리켜야 하는 숫자를 적어줘\n그게 범죄가 일어난 시각이야",duration=7.0)
        return
    fingerprint_used = True  # 한 번 실행 후 True로 설정

    showCustomMessage("범인의 지문을 획득했네! 이제 증거를 찾았으니 키를 찾아 방을 나가면 되겠네!\n지문이 가리키는 방향을 잘보고 시계의 시침이 가리켜야 하는 숫자를 적어줘\n그게 범죄가 일어난 시각이야",duration=7.0)
    
    def show_tkinter_dialog():
        root = tk.Tk()
        root.withdraw()  # Tkinter 창 숨기기
        user_input = simpledialog.askstring("숫자 입력", "키를 얻기 위한 숫자를 입력하세요:")
        root.destroy()  # Tkinter 창 닫기
        if user_input == "1":  # 정답
            showCustomMessage("정답입니다! 시계를 옆으로 밀어 열쇠를 획득하세요!",duration=3.0)
            clock.onMouseAction = onMouseAction_clock
        elif user_input is None or user_input.strip() == "":  # 취소 또는 빈 입력
            showCustomMessage("입력을 취소했습니다. 다시 시도하세요.",duration=3.0)
        else:  # 오답
            showCustomMessage("오답입니다. 다시 시도하세요.",duration=3.0)
    
    threading.Thread(target=show_tkinter_dialog).start()
fingerprint.onMouseAction = onMouseAction_fingerprint
```
지문을 클릭하면 tkinter창이 열리도록 하여 힌트를 보고 답을 적을 수 있도록 합니다.

``` python
 #시계 움직임
clock.moved = False
def onMouseAction_clock(x, y, action):
    global clock
    if clock.moved == False:
        if action == MouseAction.DRAG_LEFT:
            clock.locate(scene3, -100, 500)
            clock.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            clock.locate(scene3, 100, 500)
            clock.moved = True


end_timer = Timer(5.0)  # 5초 타이머 생성

def onMouseAction_key(x, y, action):
    global key
    key.pick()
    showCustomMessage("축하합니다! 열쇠를 찾았습니다. 방탈출 성공!",duration=7.0)

    # 5초 후 게임 종료 설정
    def end_game():
        endGame()  # 게임 종료
    end_timer.onTimeout = end_game  # 타이머 종료 시 end_game 실행
    end_timer.start()  # 타이머 시작

key.onMouseAction = onMouseAction_key
```
시계를 drag 할 수 있도록 하여 키가 보일 수 있도록 합니다. 키를 획득하면 게임이 종료되도록 합니다.

(추가적으로 2d 방에 3d로 물건들이 방에 있는 것처럼 구현하기 위해 
OpenGL을 이용해 2d 그래픽을 효율적으로 렌더링 했습니다.) 

```python
from OpenGL.GL import *
from OpenGL.GLU import *
```



## Reference
https://github.com/bosornd/bangtal.python.git

https://github.com/bosornd/bangtal/releases




