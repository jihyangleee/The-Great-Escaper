import sys
from bangtal import *
import tkinter as tk
# import threading  # OpenGL 실행을 위한 스레드 사용
# from opengl_scene import opengl_display  # OpenGL 관련 기능 가져오기

def start_escape_game():
    scene1 = Scene("룸1", "RoomEscape//배경-1.png")

    # 탁자 생성
    table = Object("RoomEscape//table(2).png")  # 탁자 이미지 필요
    table.locate(scene1, -20, 50)  # 탁자를 검정 벽 쪽으로 이동
    table.setScale(0.4)  # 크기 조정
    table.show()

    #컴퓨터 생성
    computer = Object("RoomEscape//computer(5).png")  # 노트북 이미지 필요
    computer.locate(scene1, 70, 370)  # 노트북을 탁자 위로 위치 조정
    computer.setScale(0.07)  # 크기 조정
    computer.show()

    light = Object("RoomEscape//light(2).png")  # 조명 이미지 경로
    light.locate(scene1, 300, 60)  # 천장 위치에 조명 배치
    light.setScale(0.7)  # 조명의 크기를 조정
    light.show()

    sofa = Object("RoomEscape//sofa.png")
    sofa.locate(scene1,1010,60)
    sofa.setScale(0.5)
    sofa.show()

    door1 = Object("RoomEscape//문-오른쪽-닫힘.png")
    door1.locate(scene1, 800, 270)
    door1.show()

    # 비밀번호 생성 
    keypad = Object("RoomEscape//키패드.png")
    keypad.locate(scene1, 700, 420)
    keypad.show()





    # flowerpot = Object("RoomEscape//화분.png")
    # flowerpot.locate(scene1, 550, 150)
    # flowerpot.show()

    #--------------------------------------------------------------scene2------------------------------------------------

    scene2 = Scene("룸2", "RoomEscape//배경-2.png")

    door2 = Object("RoomEscape//문-왼쪽-열림.png")
    door2.locate(scene2, 320, 270)
    door2.show()



    book1= Object("RoomEscape//books.png")
    book1.locate(scene2,40,160)
    book1.setScale(0.25)
    book1.show()


    book2= Object("RoomEscape//books(2).png")
    book2.locate(scene2,110,160)
    book2.setScale(0.25)
    book2.show()

    alpha = Object("RoomEscape//alpha.png")
    alpha.locate(scene2,900,150)
    alpha.setScale(0.6)
    alpha.show()

    #화분추가
    #이게 더 낫지??
    #약간 여러권 있는게 낫겠다. 저런 책 쌓인것이 여러개면 더 좋지 않겠나??

    # 포스터 1
    poster = Object("RoomEscape//범죄자1.png")
    poster.locate(scene2, 650, 300)  # 왼쪽 위
    poster.setScale(0.5)
    poster.show()

    # 포스터 2
    poster2 = Object("RoomEscape//범죄자2.jpg")
    poster2.locate(scene2, 735, 265)  # 오른쪽 위
    poster2.setScale(0.3)
    poster2.show()

    # 포스터 3
    poster3 = Object("RoomEscape//범죄자3.png")
    poster3.locate(scene2, 600, 260)  # 왼쪽 아래
    poster3.setScale(0.3)
    poster3.show()

    # 포스터 4
    poster4 = Object("RoomEscape//범죄자4.png")
    poster4.locate(scene2, 600, 390)  # 오른쪽 아래
    poster4.setScale(0.3)
    poster4.show()

    switch = Object("RoomEscape//switch(1).png")
    switch.locate(scene2, 770, 430)
    switch.setScale(0.1)
    switch.show()


    book = Object("RoomEscape//openbook.png")
    book.locate(scene2,200,100)
    book.setScale(0.1)
    book.show()


    password = Object("RoomEscape//암호.png")
    password.locate(scene2, 400, 100)

    board = Object("RoomEscape//board.png")
    board.setText("한글 ABCD\n1234")
    board.locate(scene2, 900, 600)
    board.show()

    door3 = Object("RoomEscape//문-오른쪽-닫힘.png")
    door3.locate(scene2, 910, 270)
    door3.show()




    #--------------------------------------------scene3-----------------------------------------

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













    # -------------------------------------------------------동작정의-----------------------------------------------
    # Door1 동작 정의
    door1.closed = True
    door1.unlocked = False
    def onMouseAction_door1(x, y, action):
        if not door1.unlocked:
            showMessage("문이 잠겨있다.")
        elif door1.closed:
            door1.setImage("C://오소소플젝//RoomEscape//문-오른쪽-열림.png")
            door1.closed = False
        else:
            scene2.enter()
            showMessage("떨어져 있는 책이 있네 그 속에 힌트가 있을거야\n책을 들여다볼까?")
    door1.onMouseAction = onMouseAction_door1

    # Keypad 동작 정의
    def onKeypad_door1():
        showMessage("철커덕")
        door1.unlocked = True
    door1.onKeypad = onKeypad_door1

    def onMouseAction_keypad(x, y, action):
        showKeypad("CLS", door1)
    keypad.onMouseAction = onMouseAction_keypad








    # flowerpot.moved = False
    # def onMouseAction_flowerpot(x, y, action):
    #     global flowerpot
    #     if flowerpot.moved == False:
    #         if action == MouseAction.DRAG_LEFT:
    #             flowerpot.locate(scene1, 450, 150)
    #             flowerpot.moved = True
    #         elif action == MouseAction.DRAG_RIGHT:
    #             flowerpot.locate(scene1, 650, 150)
    #             flowerpot.moved = True
    # flowerpot.onMouseAction = onMouseAction_flowerpot

    def onMouseAction_door2(x, y, action):
        global scene1
        scene1.enter()
    door2.onMouseAction = onMouseAction_door2


    door3.closed = True
    door3.unlocked = False
    import tkinter as tk
    from tkinter import simpledialog




    switch.lighted = True  # 스위치의 초기 상태
    switch.enabled = False  # 초기 상태는 비활성화

    def onMouseAction_switch(x, y, action):
        global switch, password, scene2
        if not switch.enabled:
            pass
        else:
            
            switch.lighted = not switch.lighted  # 스위치 상태를 토글
            if switch.lighted:
                scene2.setLight(1.0)  # 방을 밝게
                password.hide()  # 암호 숨김
            else:
                scene2.setLight(0.2)  # 방을 어둡게
                password.show()  # 암호 표시
    switch.onMouseAction = onMouseAction_switch




    poster.moved = False
    def onMouseAction_poster(x, y, action):
        global poster, switch
        if not poster.moved:
            if action == MouseAction.DRAG_LEFT:
                poster.locate(scene2, 550, 300)
                poster.moved = True
                switch.enabled = True  # 포스터가 옮겨지면 스위치 활성화
                showMessage("포스터를 옮겼습니다. 이제 스위치를 사용할 수 있습니다.")
            elif action == MouseAction.DRAG_RIGHT:
                poster.locate(scene2, 750, 300)
                poster.moved = True
                switch.enabled = True  # 포스터가 옮겨지면 스위치 활성화
                showMessage("포스터를 옮겼습니다. 이제 스위치를 사용할 수 있습니다.")
    poster.onMouseAction = onMouseAction_poster





    # caution움직임
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

    #메시지 표시
    message_background = Object("RoomEscape//background(1).png")
    message_background.locate(scene3, -10, -48) 
    message_background.hide()  # 처음에는 숨김


    message_text = Object("")
    message_text.locate(scene3,-300, -440)
    message_text.setScale(1.5)
    message_text.hide()
    def showCustomMessage(text, duration= 3.0):
        message_background.show()
        message_text.setText(text)
        message_text.show()

        timer = Timer(duration)
        def hideCustomMessage():
            message_background.hide()
            message_text.hide()
        timer.onTimeout = hideCustomMessage
        timer.start()

    #침대 움직임
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


    import threading

    fingerprint_used = False  # 지문 클릭 여부
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
















    import tkinter as tk
    from tkinter import simpledialog

    door3.closed = True
    door3.unlocked = False

    # Tkinter 창 관리 플래그
    is_tk_window_open = False  # 창이 열려 있는지 여부 추적

    def onMouseAction_door3(x, y, action):
        global door3, is_tk_window_open

        # 이미 열려 있는 상태에서는 재실행 방지
        if is_tk_window_open:
            return

        if door3.unlocked:
            if door3.closed:
                door3.setImage("RoomEscape//문-오른쪽-열림.png")  # 문 열림 이미지로 변경
                door3.closed = False
                showMessage("문이 열렸습니다. 다음 방으로 이동합니다.")
            else:
                scene3.enter()  # 이미 열린 상태라면 바로 이동
                showCustomMessage(
                    "살인사건이 일어난 현장이야. 침대에서 살인을 당했으니 침대에 단서가 있을거야\n Warning을 옆으로 제거한 뒤 침대도 옆으로 밀어볼래?",
                    duration=7.0,
                )
        else:
            # Tkinter 창이 이미 열려 있는 상태가 아니면 실행
            is_tk_window_open = True  # 창이 열렸음을 표시

            try:
                # 비밀번호 입력창 생성
                root = tk.Tk()
                root.withdraw()  # Tkinter 기본 창 숨기기

                user_input = simpledialog.askstring(
                    "비밀번호 입력", "문을 열기 위한 비밀번호를 입력하세요:"
                )
                root.destroy()  # Tkinter 창 닫기

                # 비밀번호 확인
                if user_input == "BANGTAL":  # 정답
                    showMessage("철커덕! 문이 열렸습니다.")
                    door3.unlocked = True
                elif user_input is None or user_input.strip() == "":  # 입력 취소 또는 빈 입력 처리
                    showMessage("입력을 취소했습니다. 다시 시도하세요.")
                else:  # 오답
                    showMessage("비밀번호가 틀렸습니다. 다시 시도하세요.")

            except Exception as e:
                print(f"오류 발생: {e}")  # 디버깅용 로그

            finally:
                is_tk_window_open = False  # 창이 닫혔음을 표시

    door3.onMouseAction = onMouseAction_door3



    def onMouseAction_book(x,y,action):
        showMessage("힌트 : 벽에 걸려있는 용의자들의 실루엣이 보일거야 저 사람들 중에 범인이 있어\n 범인은 평소에 추리소설을 좋아해 그래서 탐정들의 모습을 따라하는 것을 좋아한다네\n범인일 것 같은 범죄자의 얼굴을 클릭해서 옆으로 옮겨줘 그리고 무슨 문자가 나올거야 그걸 잘 기억해둬")
    book.onMouseAction = onMouseAction_book

    def onMouseAction_computer(x, y, action):
        showMessage("힌트 : '난 요즘 컴퓨터로 계속 작업하는데\n빛이 너무 강해서 그런가 눈이 너무 아파서\n소파에서 가끔씩 쉬면서 해'\n조명쪽으로 가서 빛 조절좀 해줄래?")
    computer.onMouseAction = onMouseAction_computer


    def onMouseAction_light(x,y,action):
        showMessage("방금 힌트를 봤을거야\n 거기에 나온 문장들을 잘보면 지금 이 방에 있는 물건들이 문장 속에 있을거야\n 문 옆에 있는 스위치를 눌러 그 단어들을 잘 조합해줘")
    light.onMouseAction = onMouseAction_light


    



    showMessage("먼저 탁자위에 있는 컴퓨터로 가봐!\n열쇠를 얻기 위한 힌트가 주어질거야")
    startGame(scene1)  # 방탈출 게임 시작
    


from tkinter import messagebox
# tkinter 로그인 창 생성
import ctypes
from PIL import Image, ImageTk  # 이미지 처리를 위한 라이브러리

def start_escape_game_with_closing(main_menu):
    """메인 메뉴 창을 닫고 게임을 시작합니다."""
    main_menu.destroy()  # 메인 메뉴 창 닫기
    start_escape_game()
# 게임 방법을 보여주는 함수
def show_game_instructions():
    messagebox.showinfo("게임 방법", "1. 아이템을 클릭하거나 드래그하세요.\n2. 단서를 모아 문제를 해결하세요.\n3. 모든 방을 탈출하면 승리합니다!")

# 로그인 성공 후 메인 메뉴 창 생성
def create_main_menu():
    main_menu = tk.Tk()
    main_menu.title("The Great Escaper")
    main_menu.geometry("1280x761")

    # 배경 이미지 삽입
    image_path = "RoomEscape//표지.webp"  # 사용자가 업로드한 이미지 경로
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(main_menu, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 탐정이 말하는 문구 추가
    detective_text = (
        "어느 오후 나는 얼굴도 모르는 사람한테 총에 맞아 죽고 말았어.\n"
        "범죄자의 실루엣과 지문을 찾아서 증거를 확보해줘."
    )
    text_label = tk.Label(
        main_menu,
        text=detective_text,
        font=("Arial", 16),
        bg="black",  # 배경색은 검정
        fg="white",  # 글자색은 흰색
        wraplength=1000,  # 텍스트 줄바꿈
        justify="center",  # 텍스트 중앙 정렬
    )
    text_label.place(x=240, y=50)  # 텍스트 위치



    # 버튼 배치
    start_button = tk.Button(
        main_menu,
        text="게임 시작",
        font=("Arial", 20),
        bg="black",
        fg="white",
        command=lambda: start_escape_game_with_closing(main_menu)  # 창 닫고 게임 시작
    )
    start_button.place(x=540, y=500, width=200, height=50)

    instructions_button = tk.Button(
        main_menu,
        text="게임 방법",
        font=("Arial", 20),
        bg="black",
        fg="white",
        command=show_game_instructions
    )
    instructions_button.place(x=540, y=580, width=200, height=50)

    main_menu.mainloop()


















# DPI 스케일링 비활성화 (Windows 환경)
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def create_login_window():
    def on_login():
        user_id = id_entry.get()
        user_pw = pw_entry.get()

        if user_id == "admin" and user_pw == "1234":
            messagebox.showinfo("로그인 성공", "게임을 시작합니다!")
            root.destroy()  # 로그인 창 닫기
            create_main_menu()  # 메인 메뉴 창 생성
        else:
            messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 틀렸습니다.")

    root = tk.Tk()
    root.title("The Great Escaper - 로그인")

    # 창 크기 설정
    root.geometry("1280x761")
    root.configure(bg="#2E2E2E")  # 밝은 회색

    title_label = tk.Label(root, text="The Great Escaper", font=("Arial", 36, "bold"), bg="black", fg="white")
    title_label.place(x=1280 // 2 - 300, y=50)

    tk.Label(root, text="아이디:", font=("Arial", 18), bg="black", fg="white").place(x=350, y=250)
    id_entry = tk.Entry(root, font=("Arial", 18))
    id_entry.place(x=550, y=250, width=300)

    tk.Label(root, text="비밀번호:", font=("Arial", 18), bg="black", fg="white").place(x=350, y=320)
    pw_entry = tk.Entry(root, show="*", font=("Arial", 18))
    pw_entry.place(x=550, y=320, width=300)

    login_button = tk.Button(root, text="로그인", command=on_login, font=("Arial", 18), bg="white", fg="#2E2E2E")
    login_button.place(x=590, y=400, width=100, height=50)

    root.mainloop()

create_login_window()