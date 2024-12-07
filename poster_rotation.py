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
    Render the image rotated by the given angle with a transparent background
    and save the result to a file.
    """
    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW 초기화 실패")

    # Create an offscreen window
    window = glfw.create_window(800, 800, "Offscreen Rendering", None, None)
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

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Set a transparent background
    glClearColor(0.0, 0.0, 0.0, 0.0)  # RGBA: 마지막 값 0.0은 투명도

    # Load the texture
    texture, img_width, img_height = load_texture_with_alpha(image_path)
    if not texture:
        glfw.terminate()
        return

    # OpenGL rendering
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)  # Move the object back
    glRotatef(-angle, 0.0, 2.0, 0.0)  # Rotate the object around the Y-axis (negative for left)

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
    width, height = 800, 800
    pixels = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)  # Include alpha channel
    image = Image.frombytes("RGBA", (width, height), pixels)
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
    input_image = "RoomEscape//switch(1).png"  # 원본 이미지 경로
    output_image = "RoomEscape//switch(1).png"  # 저장될 이미지 경로
    rotation_angle = 0 # 오른쪽으로 회전할 각도

    # Render the image rotated and save it
    render_to_image(input_image, output_image, rotation_angle)
