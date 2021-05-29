# Vehicle class created
class Vehicle:
    def __init__(self, model, weight, speed):
        self.set_model(model) # model attribute
        self.set_weight(weight) # weight attribute
        self.set_speed(speed) # speed attribute

    # Setter methods for model, weight and speed
    # model, weight and speed attributes defined as private (starts with __)
    def set_model(self, model):
        self.__model = model
    
    def set_weight(self, weight):
        if weight <= 0: # Check if the weight is negative
            self.__weight = 1524
        else:
            self.__weight = weight
    
    def set_speed(self, speed):
        self.__speed = speed

    # Getter methods for model, weight and speed
    def get_model(self):
        return self.__model

    def get_weight(self):
        return self.__weight

    def get_speed(self):
        return self.__speed

    # hp method returns horsepower with 1 digit after decimal point
    def hp(self):
        return round(self.__weight*((self.__speed/234)**3),1)

    # str method includes details of model, weight and speed
    def str(self):
        return f"Model: {self.__model} Weight: {self.__weight} kg, Speed: {self.__speed}"

example = Vehicle("BMW M3", 2735, 90)

print(f"Power: {example.hp()} hp")
print(example.str())

# Subclass of Vehicle
class GasolinePowered(Vehicle):
    def __init__(self, model, weight, speed):
        super().__init__(model, weight, speed) # super() allows to refer base class

    def str(self):
        return f"Vehicle Type: Gasoline Powered, Model: {self.get_model()}, Weight: {self.get_weight()} kg, Speed: {self.get_speed()}, Power: {super().hp()} hp"

# Subclass of Vehicle
class ElectricPowered(Vehicle):
    def __init__(self, model, weight, speed):
        super().__init__(model, weight, speed)

    def watt(self):
        return round(super().hp()*745.699872/1000,1) # hp is obtained from base class

    def str(self):
        return f"Vehicle Type: Electric Powered, Model: {self.get_model()}, Weight: {self.get_weight()} kg, Speed: {self.get_speed()}, Power: {self.watt()} kW"


# create two objects of GasolinePowered and ElectricPowered subclass
gasoline_powered = GasolinePowered("BMW M3", 3000, 100)
electric_powered = ElectricPowered("BMW M3", 2500, 112)

print(gasoline_powered.str())
print(electric_powered.str())

