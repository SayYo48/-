from PIL import Image

def resize_image(image, new_size):
    try:
        resized_image = image.resize(new_size)
        return resized_image
    except Exception as e:
        print(f"Ошибка при изменении размера: {e}")
        return None
def rotate_image(image, angle):
    try:
        rotated_image = image.rotate(angle)
        return rotated_image
    except Exception as e:
        print(f"Ошибка при повороте: {e}")
        return None
def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None