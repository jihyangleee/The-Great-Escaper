import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np


def load_texture_with_alpha(image_path):
    """
    Load the image with an alpha channel for OpenGL rendering.
    """
    try:
        img = Image.open(image_path).convert("RGBA")  # RGBA 포맷으로 변환
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  # OpenGL 좌표계를 위해 이미지 뒤집기
        img_data = np.array(img, dtype=np.uint8)

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            img.width,
            img.height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            img_data,
        )

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return texture, img.width, img.height
    except Exception as e:
        print(f"텍스처 로드 실패: {e}")
        return None, 0, 0


def render_to_image(image_path, output_path, angle):
    """
    Render the image rotated around the Y-axis (3D effect) with a transparent background
    and save the result to a file. Maintains original image size.
    """
    # Load the image to get its size
    img = Image.open(image_path).convert("RGBA")
    img_width, img_height = img.size

    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW 초기화 실패")

    # Create an offscreen window matching the image size
    window = glfw.create_window(img_width, img_height, "Offscreen Rendering", None, None)
    if not window:
        glfw.terminate()
        raise Exception("창 생성 실패")

    glfw.make_context_current(window)

    # Enable OpenGL features
    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)  # Enable blending for transparency
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # Alpha blending
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    # Set up the perspective projection
    glViewport(0, 0, img_width, img_height)  # Match viewport to image size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, img_width / img_height, 0.1, 100.0)  # 3D perspective projection
    glMatrixMode(GL_MODELVIEW)

    # Set a transparent background
    glClearColor(0.0, 0.0, 0.0, 0.0)  # RGBA: 마지막 값 0.0은 투명도

    # Load the texture
    texture, _, _ = load_texture_with_alpha(image_path)
    if not texture:
        glfw.terminate()
        return

    # OpenGL rendering
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -3.0)  # Move the object back in the Z-axis

    # Apply rotations to make it appear front-facing
    glRotatef(angle, 0.0, 1.0, 0.0)  # Rotate the object around the Y-axis
    glRotatef(10, 1.0, 0.0, 0.0)  # Slight tilt around X-axis for better perspective

    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()

    # Read the pixels from the frame buffer
    pixels = glReadPixels(0, 0, img_width, img_height, GL_RGBA, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGBA", (img_width, img_height), pixels)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image vertically

    # Save the image
    image.save(output_path, "PNG")  # Save as PNG with transparency
    print(f"회전된 투명 이미지가 저장되었습니다: {output_path}")

    glfw.terminate()




# if __name__ == "__main__":
#     # Input and output paths
#     input_image = "RoomEscape//poster.png"  # 원본 이미지 경로
#     output_image = "RoomEscape//poster.png"  # 저장될 이미지 경로
#     rotation_angle = 30  # 왼쪽으로 회전할 각도 (음수로 전달)

#     # Render the image rotated and save it
#     render_to_image(input_image, output_image, rotation_angle)





if __name__ == "__main__":
    # Input and output paths
    input_image = "RoomEscape//문-왼쪽-열림.png"  # 원본 이미지 경로
    output_image = "RoomEscape//문-왼쪽-열림(1).png"  # 저장될 이미지 경로
    rotation_angle = 30# 오른쪽으로 회전할 각도

    # Render the image rotated and save it
    render_to_image(input_image, output_image, rotation_angle)