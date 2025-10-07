from PIL import Image

def resize_image(image_path, new_size):
    try:
        image = Image.open(image_path)
        resized_image = image.resize(new_size)
        return resized_image
    except Exception as e:
        print(f"Ошибка при изменении размера: {e}")
        return None

def rotate_image(image_path, angle):
    try:
        image = Image.open(image_path)
        rotated_image = image.rotate(angle)
        return rotated_image
    except Exception as e:
        print(f"Ошибка при повороте: {e}")
        return None