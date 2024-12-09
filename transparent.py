from PIL import Image
from bangtal import * 
def make_image_transparent(input_path, output_path, transparency=128):
    image = Image.open(input_path).convert("RGBA")
    datas = image.getdata()

    new_data = []
    for item in datas:
        # item[3] is the alpha channel
        if item[3] != 0:  # If pixel is not fully transparent
            new_data.append((item[0], item[1], item[2], transparency))
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(output_path)

# 투명도를 50%로 설정한 이미지 생성
make_image_transparent("RoomEscape//background.png", "RoomEscape//background(1).png", transparency=190)

# # Bangtal에서 투명 이미지 사용
# message_background = Object("RoomEscape//message_bg_transparent.png")
# message_background.locate(scene3, 200, 300)
# message_background.setScale(0.8)
# message_background.show()
