from datetime import date


class Medicine:
    def __init__(self, name, price, quantity, is_prescription_needed, expiration_date):
        self._name = name
        self.price = price  # проходить через setter з валідацією
        self._quantity = quantity
        self._is_prescription_needed = is_prescription_needed
        self._expiration_date = expiration_date

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # bool є підкласом int, тому його перевіряємо окремо
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"Ціна має бути числом, отримано {type(value).__name__}"
            )
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @property
    def is_prescription_needed(self):
        return self._is_prescription_needed

    @property
    def expiration_date(self):
        return self._expiration_date

    def showMedicine(self):
        recipe = "так" if self._is_prescription_needed else "ні"
        print(f"Назва: {self._name} | Ціна: {self._price:.2f} | Кількість: {self._quantity} "
              f"| За рецептом: {recipe} | Придатні до: {self._expiration_date}")

    def isExpired(self):
        return self._expiration_date < date.today()


class Pharmacy:
    def __init__(self):
        self._medicines = []

    def find_medicine(self, name):
        result = None
        for medicine in self._medicines:
            if medicine.name == name:
                result = medicine
                break
        return result

    def add_medicine(self, medicine):
        if self.find_medicine(medicine.name) is not None:
            print(f"Ліки {medicine.name} вже є в аптеці")
        else:
            self._medicines.append(medicine)

    def remove_medicine(self, name):
        medicine = self.find_medicine(name)
        if medicine is None:
            print(f"Ліки {name} не знайдено")
        else:
            self._medicines.remove(medicine)

    def inventory(self):
        expired = [m for m in self._medicines if m.isExpired()]
        if not expired:
            print("Прострочених ліків немає")
        else:
            for medicine in expired:
                print(f"Видалено прострочені ліки: {medicine.name}")
                self._medicines.remove(medicine)

    def apply_discount(self):
        for medicine in self._medicines:
            medicine.price = round(medicine.price * 0.9, 2)

    def show_cheapest(self):
        if not self._medicines:
            print("В аптеці немає ліків")
        else:
            min_price = min(m.price for m in self._medicines)
            for medicine in self._medicines:
                if medicine.price == min_price:
                    medicine.showMedicine()

    def show_all(self):
        if not self._medicines:
            print("В аптеці немає ліків")
        else:
            for medicine in self._medicines:
                medicine.showMedicine()

    def __iter__(self):
        return iter(self._medicines)


def main():
    pharmacy = Pharmacy()

    print("\n''' Створення та додавання ліків '''")
    med1 = Medicine("Парацетамол", 45.50, 100, False, date(2027, 5, 1))
    med2 = Medicine("Амоксицилін", 120, 30, True, date(2027, 1, 15))
    med3 = Medicine("Аспірин", 60, 50, False, date(2024, 3, 10))
    med4 = Medicine("Цитрамон", 45.50, 70, False, date(2027, 9, 20))
    pharmacy.add_medicine(med1)
    pharmacy.add_medicine(med2)
    pharmacy.add_medicine(med3)
    pharmacy.add_medicine(med4)
    pharmacy.show_all()

    print("\n''' Спроба додати ліки з існуючою назвою '''")
    pharmacy.add_medicine(Medicine("Парацетамол", 10, 1, False, date(2027, 1, 1)))

    print("\n''' Переоблік (видалення прострочених) '''")
    pharmacy.inventory()
    pharmacy.show_all()

    print("\n''' Знижка 10% на всі ліки '''")
    pharmacy.apply_discount()
    pharmacy.show_all()

    print("\n''' Найдешевші ліки '''")
    pharmacy.show_cheapest()

    print("\n''' Видалення ліків з аптеки '''")
    pharmacy.remove_medicine("Амоксицилін")
    pharmacy.remove_medicine("Невідомі ліки")
    pharmacy.show_all()

    print("\n''' Додавання нових ліків '''")
    pharmacy.add_medicine(Medicine("Но-шпа", 95, 25, False, date(2028, 2, 1)))
    pharmacy.show_all()

    print("\n''' Кінець програми '''")


if __name__ == "__main__":
    main()