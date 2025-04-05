from PIL import Image

def decrypt_message(file_path):
    image = Image.open(file_path)
    pixels = image.load()

    width, height = image.size

    message = ""
    for i in range(width):
        for j in range(height):
            if pixels[i, j] == (0, 0, 0):
                message += chr(j)
                break

    return message