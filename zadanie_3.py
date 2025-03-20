class BaseConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_kelvin(self):
        """Конвертация из градусов Цельсия в Кельвины."""
        kelvin = self.celsius + 273.15
        return round(kelvin, 2)

    def to_fahrenheit(self):
        """Конвертация из градусов Цельсия в Фаренгейты."""
        fahrenheit = (self.celsius * 1.80) + 32
        return round(fahrenheit, 2)

    def convert(self, unit):
        """Основной метод для преобразования температуры."""
        if unit.lower() == 'kelvin':
            return self.to_kelvin()
        elif unit.lower() == 'fahrenheit':
            return self.to_fahrenheit()
        else:
            return f"Неизвестная единица измерения: {unit}"

def main():
    celsius = float(input("Введите градусы Цельсия: "))
    converter = BaseConverter(celsius)
    choice = input("Выберите единицу измерения (Kelvin/Fahrenheit): ")
    result = converter.convert(choice)
    print(f"{celsius}°C равно {result}{choice}.")

if __name__ == "__main__":
    main()