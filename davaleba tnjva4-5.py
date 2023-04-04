# class Currency:
#     exchange_rates = {"GEL": 1, "USD": 2.7, "EUR": 3}
#
#     def __init__(self, value, unit="GEL"):
#         self._value = value
#         self._unit = unit
#
#     def value(self):
#         return self._value
#
#     def unit(self):
#         return self._unit
#
#     def __str__(self):
#         return f"{self._value:.2f} {self._unit}"
#
#     def __add__(self, other):
#         if type(other) is not Currency:
#             raise TypeError("unsupported operand type for  'Currency' and '{}'".format(type(other).__name__))
#
#         if self._unit == other._unit:
#             new_value = self._value + other._value
#             return Currency(new_value, self._unit)
#         else:
#             rate = self.exchange_rates[self._unit] / self.exchange_rates[other._unit]
#             new_value = self._value + other._value * rate
#             return Currency(new_value, self._unit)
#
#     def __mul__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError("The multiplication operation must be performed only with a whole or a decimal number")
#
#         new_value = self._value * other
#         return Currency(new_value, self._unit)
#homework3
class Plane:
    def Move(self):
        print("Plane can fly")

    def Speed(self):
        print("its speed is up to 900km/h")

class Bus:
    def Move(self):
        print("Bus can move on roads")
    def Speed(self):
        print("its speed is up to 180km/h")
plane = Plane()
bus = Bus()
plane.Move()  # ბეჭდავს "Plane can fly"
plane.Speed()  # ბეჭდავს "its speed is up to 900km/h"
bus.Move()  # ბეჭდავს "Bus can move on roads"
bus.Speed()  # ბეჭდავს "its speed is up to 180km/h"
def movement(obj):
    obj.Move()
    obj.Speed()
movement(plane)
movement(bus)

