import os

def get_user_input():
    image_path = input("Введите путь к изображению: ")
    width = int(input("Введите новую ширину: "))
    height = int(input("Введите новую высоту: "))
    angle = int(input("Введите угол поворота: "))
    return image_path, (width, height), angle
def save_and_show_result(image, original_path):
    if image:
        if not os.path.exists("Результаты"):
            os.makedirs("Результаты")
        file_name = os.path.basename(original_path)
        name, ext = os.path.splitext(file_name)
        output_path = os.path.join("Результаты", f"Преобразования_{name}{ext}")
        image.save(output_path)
        print(f"Изображение сохранено как: {output_path}")
        print(f"Размер: {image.size}")
        print(f"Формат: {image.format}") 
        return output_path
    else:
        print("Ошибка: не удалось обработать изображение")
        return None