# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol_amount = 0
        self.__odometer = 0

    def fill_up(self):
        if self.__petrol_amount <= 60:
            self.__petrol_amount += (60 - self.__petrol_amount)
    
    def drive(self, km: int):
        if km <= self.__petrol_amount:
            self.__odometer += km
            self.__petrol_amount -= km
        else:
            self.__odometer += self.__petrol_amount
            self.__petrol_amount = 0


    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol reading {self.__petrol_amount} litres" 

