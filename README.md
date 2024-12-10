# The Great Escaper

**The Great Escaper** – 방탈출 게임
-	The great escaper는 총 3개로 구성되어 있는 방에 있는 단서를 찾아야 탈출할 수 있는 게임이다.
-	방탈출을 해서 단서를 찾아야 하는 이유는 다음과 같다.
범죄가 일어난 탐정 사무실이 있다. 탐정사무실에서 마지막 방인 침실에서 살인사건이 일어났다. 피해자인 탐정은 죽기 직전까지도 범인으로부터 협박을 받고 있었다.
두번째 방에서 용의자들의 실루엣을 두고 그 범죄자가 누군지 밝혀내려고 했던 것으로 보인다. 마지막 방에서 지문이 나왔으니 실루엣과 지문을 통해 범인을 밝혀내야 한다. 
## Table of contents	
1.	시작환경
2.	게임방법
3.	게임구현 방법
4.	Reference
5.	License
## 시작 환경
Python 기반 방탈출 게임 라이브러리를 사용하려면 32비트 환경이 필요하다. (python8-32bit 환경 권장) , https://github.com/bosornd/bangtal/releases 여기서 v0.4.0 bangtal library를 다운받으면 된다. Bangtal.dll은 window환경에 있으며 bangtal파일은 python8파일에 있다. 이렇게 준비가 끝나면 함수를 추가하거나 객체를 추가하여 방을 꾸미고 단서를 넣어 방탈출 게임을 만든다.

## 게임 방법


[![The Great Escaper](https://img.youtube.com/vi/10o4dw1W-zs/0.jpg)](https://youtu.be/10o4dw1W-zs)


 
![image](https://github.com/user-attachments/assets/d3652ede-512f-4624-aea7-161aa371313c)
게임이 시작되기 전 억울하게 죽은 탐정이 확보해야 할 것들을 말해주고 있다.
게임 방법을 선택하면 게임을 하는 간단한 방법 같은 것들이 나온다. (클릭, 드래그를 해야한다는 것, 단서를 찾아야 방탈출을 할 수 있다는 것.) 

![image](https://github.com/user-attachments/assets/d2668463-d9dc-44e5-9516-dc831cd4b882)
게임이 시작되었다. 먼저 컴퓨터 쪽으로 가서 힌트를 방을 탈출할 수 있는 힌트를 얻으면 된다.

![image](https://github.com/user-attachments/assets/9f42c17d-8b79-4588-9184-0bd07c849cda)
힌트로 문장을 적어주었는데 방에 있는 물건들을 잘 조합해보면 답을 찾을 수 있다. 

![image](https://github.com/user-attachments/assets/5bbc24d7-bd64-47bc-87c0-f11e3b7fe694)
 (컴퓨터, 빛, 소파를 영어로 바꿔서 앞글자를 조합해보면 된다)

![image](https://github.com/user-attachments/assets/02abd6b8-68cd-4e90-8cb7-01e374afe5b9)
Computer, light, sofa 이렇게 영어로 바꾼 후 c,l,s를 화살표를 클릭하여 찾으면 문이 열린다. 

![image](https://github.com/user-attachments/assets/7130cb5a-8cb1-4bac-965d-f5e5010ba0ab)
벽에 붙여 있는 실루엣을 보고 힌트에 맞는 실루엣을 선택하여 오른쪽으로 드래그하면 된다. 그러면 스위치가 있다. 그것을 누르면 방의 불이 꺼지면서 ‘BANGTAL’이라는 글자가 나온다.

![image](https://github.com/user-attachments/assets/25c7a064-2337-4a07-942c-0ad988f831ff)
‘BANGTAL’이 나온 것을 알 수 있다.

![image](https://github.com/user-attachments/assets/c03606bf-a9c5-4b3f-9f15-8b00c379a358)
문을 열기 위해 클릭해보면 하나의 창이 뜬다. 거기에 방금 전에 보았던 단어를 입력하면 문이 열린다. 

![image](https://github.com/user-attachments/assets/65275f9e-4ae0-4e90-a5f8-b36e20590867)

![image](https://github.com/user-attachments/assets/77c49b07-924c-428d-8614-10540f36819a)
살인사건이 일어난 마지막 방이다. Warning과 침대를 옆으로 옮기면 단서가 나온다.

![image](https://github.com/user-attachments/assets/b56f2fad-fbc2-41d2-bb48-c51fbfe3e22a)
침대를 옮기니 지문이 나왔다. 지문의 방향을 보면 1시방향으로 기울어져 있음을 알 수 있다. 1을 적으면 마지막 방을 탈출할 수 있는 힌트가 나올 것이다.

![image](https://github.com/user-attachments/assets/7edca17a-0b82-4025-a9e9-5b82aeba64f5)
시계를 옆으로 밀면 방을 나갈 수 있는 열쇠가 주어진다.

![image](https://github.com/user-attachments/assets/294af7fc-0226-453a-b10b-08444f370a69)
방탈출에 성공했다.

![image](https://github.com/user-attachments/assets/ad6c2b69-8866-438c-b70a-3fe0a12ad9a3)
찾은 물품을 기록하는 공간이다. 5초후에 게임이 종료된다. 






 

 

