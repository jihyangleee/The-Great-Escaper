from PIL import Image

# 이미지 열기
image = Image.open("RoomEscape//지문.png")

# 시계방향 30도 회전
rotated_image = image.rotate(-30, expand=True)

# 회전한 이미지를 새 파일로 저장
rotated_image.save("RoomEscape//rotated_지문.png")