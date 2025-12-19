from image_utils.image_handler import ImageHandler
from image_utils.image_processor import ImageProcessor

def main():
    print("=== Обработка изображения ===")
    image_path = input("Введите путь к изображению (например: image.jpg): ").strip()

    try:
        handler = ImageHandler(image_path)
        print(f"Изображение '{image_path}' загружено.")

        handler.resize(300, 300)
        print("Изображение изменено до 300x300 пикселей.")

        original_image = handler.get_image() 
        processor = ImageProcessor(original_image)
        print("Изображение передано для обработки.")

        processor.apply_blur()
        print("Фильтр размытия применён.")

        processor.add_text("Вариант 1", position="bottom_right")
        print("Текст 'Вариант 1' добавлен в нижний правый угол.")

        handler.set_image(processor.image)

        output_path = "output.png"
        handler.save(output_path)
        print(f"Результат сохранён как '{output_path}'.")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()