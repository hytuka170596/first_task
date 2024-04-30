class Property:
    """Базовый класс Property
     Args:
         worth (int) - стоймость продукта
         """
    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def __str__(self):
        return f'{self.__class__.__name__}\tСтоймость: {str(self.get_worth())}'

    def set_worth(self, new_worth):
        """Сеттер для проверки стоймости на правильный тип данных """
        try:
            if isinstance(new_worth, (int, float)):
                self.__worth = new_worth
                return self.__worth
            else:
                raise TypeError('Ошибка, значение ожидало тип - int или float')
        except TypeError as exc:
            print(type(exc), exc)

    def get_worth(self):
        """Геттер не знаю зачем я тут сделал """
        return self.__worth

    def calculation_of_taxes(self):
        ...


class Apartment(Property):
    """Дочерний класс Apartment от (Property) """
    def calculation_of_taxes(self):
        """Метод для расчёта налога на квартиру! """
        return self.get_worth() * 0.001


class Car(Property):
    """Дочерний класс Car от (Property) """
    def calculation_of_taxes(self):
        """Метод расчёта налога на машину """
        return self.get_worth() * 0.005


class CountryHouse(Property):
    """Дочерний класс CountryHouse от (Property) """
    def calculation_of_taxes(self):
        """Метод для расчёта налога на дачу"""
        return self.get_worth() * 0.002


def check_coast(balance, coast, cls):
    """Функция проверяет, хватит ли средств для покупки товара.
     И возвращает налог, и остаток средств или сколько не хватает для покупки
     Args:
         balance - (int) Баланс кошелька
         coast - (int) Стоймость продукта
         cls - (class) объект в котором идут расчёты
         """
    result = balance - (coast + cls.calculation_of_taxes())
    if str(result).endswith('.0'):
        result = int(result)
    if result >= 0:
        return '\nНалог: {} руб. \nДенег достаточно, можете приобрести! Тогда у вас останется: {} руб.'.format(
            round(cls.calculation_of_taxes(), 2), round(result, 2))
    else:
        return '\nНалог: {} руб. \nК сожалению недостаточно средств. Вам нехватает - {} руб.'.format(
            round(cls.calculation_of_taxes(), 2), abs(result))


def main():
    """Код запускающий программу! """
    try:
        total_many = int(input('Укажите сколько всего средств на балансе: '))
        cost_property = int(input('Укажите стоймость имущества, которое желаете приобрести: '))
        product = input('И наконец, что именно хотите купить? ').lower()
        if product in ['квартира', 'квартиру', 'дом']:
            apartment = Apartment(worth=cost_property)
            print(check_coast(total_many, cost_property, apartment))

        elif product in ['машина', 'машину', 'автомобиль', 'тачку', 'тачка']:
            car = Car(worth=cost_property)
            print(check_coast(total_many, cost_property, car))

        elif product in ['дача', 'дачу', 'загородный дом']:
            country_house = CountryHouse(worth=cost_property)
            print(check_coast(total_many, cost_property, country_house))

        else:
            raise ValueError('Таких услуг мы не предоставляем, но вы можете обратиться к нашим партнерам!')
    except ValueError as exc:
        print(exc)


if '__main__' == __name__:
    main()


print(Property.__doc__)