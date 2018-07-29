############################################
#                                          #
#  Programa sencillo de manejo de clases   #
#                                          #
############################################


class Person:
    def __init__(self, name, age, birthdate, cars=0):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.cars = cars
        self.total = 0

        ## Si es un coche, aumenta el numero de coches

        for i in cars:
            if isinstance(i, Car):
                self.total+=1

    def printinfo(self):
        print "=== Person ==="
        print "Name: ", self.name
        print "Age: ", self.age
        print "Birthdate: ", self.birthdate
        print "Total cars: ", self.total, "\n"

        ## Comprobacion que el parametro cars pasado sea una lista de Coches. Si es asi, lo imprime

        if isinstance(self.cars, list):
            for i in self.cars:
                if isinstance(i, Car):
                    i.printinfo()

    def __del__(self):
        print self.name, "ha sido liberado por el sistema y ha muerto..."

class Car:
    def __init__(self, model, door, consumption, color, age):
        self.model = model
        self.door = door
        self.consumption = consumption
        self.color = color
        self.age = age

    def printinfo(self):
        print "=== Car ==="
        print "Model: ", self.model
        print "Doors: ", self.door
        print "Average Consumption: ", self.consumption
        print "Color: ", self.color
        print "Age: ", self.age, "\n"


# No necesario destructor porque no hay que liberar recursos del sistema...

coche1 = Car("Citroen", 4, 7.3, "grey", 6)
coche2 = Car("Toyota", 2, 8.8, "blue", 5)
coche3 = Car("Corsa", 8, 5.33, "green", 10)
persona = Person("Kevin", 20, "15/10/1990", [coche1, coche2, coche3])

persona.printinfo()
