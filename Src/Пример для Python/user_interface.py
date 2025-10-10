def get_user_input():
    image_path = input("Введите путь к изображению: ")
    width = int(input("Введите новую ширину: "))
    height = int(input("Введите новую высоту: "))
    angle = int(input("Введите угол поворота: "))
    return image_path, (width, height), angle
def save_and_show_result(image, output_path):
    if image:
        image.save(output_path)
        print(f"Изображение сохранено как: {output_path}")
    else:
        print("Ошибка обработки изображения")