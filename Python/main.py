from car import Car
from account import Account

if __name__ == "__main__":
    print ("Hola mundo")
    
    car = Car("AMS234",Account("Andres Herrera", "7149506"))
    print(vars(car))
    print(vars(car.driver))
    
    
    '''car = Car()
    car.license = "AMS234"
    car.driver  = "Andrés Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "AGD123"
    car2.driver  = "Gloria Zapata"
    print(vars(car2))'''