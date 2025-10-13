from image_processor import load_image, resize_image, rotate_image
from user_interface import get_user_input, save_and_show_result

def main():
    print("Программа для обработки изображений")
    image_path, new_size, angle = get_user_input()
    original_image = load_image(image_path)
    if not original_image:
        return
    print(f"Изображение загружено. Размер: {original_image.size}")
    resized_image = resize_image(original_image, new_size)
    if not resized_image:
        return
    print(f"Размер изменен на: {new_size}")
    final_image = rotate_image(resized_image, angle)
    if not final_image:
        return
    print(f"Изображение повернуто на {angle} градусов")
    save_and_show_result(final_image, image_path)
    print("Обработка завершена!")

if __name__ == "__main__":
    main()