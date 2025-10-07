import os
from PIL import Image

def main():
    image_path = input("Введите путь к изображению: ")
    width = int(input("Введите новую ширину: "))
    height = int(input("Введите новую высоту: "))
    angle = int(input("Введите угол поворота: "))
    try:
        image = Image.open(image_path)
        print("Изображение загружено")
        new_size = (width, height)
        resized_image = image.resize(new_size)
        print("Размер изменен")
        final_image = resized_image.rotate(angle)
        print("Изображение повернуто")
        file_name = os.path.basename(image_path)
        output_path = os.path.join("Результаты", "Преобразованный_" + file_name)
        final_image.save(output_path)
        print(f"Изображение сохранено как: {output_path}")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()