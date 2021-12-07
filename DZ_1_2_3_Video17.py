# ДЗ 1 Видео 17. Описать иерархию классов. 
class Car():
    def __init__(self):
        pass
class Car:           # создаем класс Car 
    def __init__(self, name, make, model):  # создание объект класса 
        self.name = name                   # для это создаем метод класса 
        self.make = make                 # def __init__(self):
        self.model = model              # класс должен уметь имя (или модель,
car_a = Car("Toyota", 2015, "Corrola")  # или когда сделано) и какая езда будет 
print("Быстрая езда")
print(car_a.name) 

class Car():
    def __init__(self, name, make, model):
        self.name = name            # показал нам имя автомобиля Shevrolet
        self.make = make            # и Медленная езда
        self.model = model
car_b = Car("Shevrolet", 2013, "Spark")      
print("Медленная езда")
print(car_b.name)

# ДЗ 2 написать тест к приложению
import unittest

class TestCar(unittest.TestCase): # Тест для класса Car
    def test_get_full_name(self): # Проверяет правильность получения полного имени
        car_b = Car('Shevrolet", 2013, "Spark')
        self.assertEqual(car_b.get_full_name(), 'Автомобиль Shevrolet 2013 Spark')

if __name__ == '__main__':
    unittest.main()

import unittest

class TestCar(unittest.TestCase): # Тест для класса Car
    def test_get_full_name(self): # Проверяет правильность получения полного имени
        car_b = Car('Shevrolet", 2013, "Spark')
        self.assertNotEqual(car_b.get_full_name(), 'Автомобиль Shevrolet 2013 Spark')

if __name__ == '__main__':
    unittest.main()

# ДЗ 3 описать исключения.

# Выход ДЗ 1-2:
# TypeError: __init__() missing 2 required positional arguments: 'make' and 'model'

----------------------------------------------------------------------
#Ran 1 test in 0.001s

# FAILED (errors=1)
# Обработаем исключение TypeError:


try:
   class Car():
    def __init__(self, name, make, model):
        self.name = name            # показал нам имя автомобиля Shevrolet
        self.make = make            # и Медленная езда
        self.model = model
car_b = Car("Shevrolet", 2013, "Spark")      
print("Медленная езда")
print(car_b.name) 
except Exception:
    print(__init__() missing 2 required positional arguments: 'make' and 'model')
    
    
    
class Car_bFastDrivingException(Exception):
    pass
 
class CarStoppedException(Exception):
    pass
 