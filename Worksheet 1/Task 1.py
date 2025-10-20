# Task 9.1
class Car:
    def __init__(self, make, model, top_speed, type, colour, engine_size):
        self.make = make
        self.model = model
        self.__top_speed = top_speed
        self.type = type
        self.colour = colour
        self.__engine_size = engine_size

    # Task 9.4
    def __validate_colour(self, colour):
        colours = ["Red","White", "Black", "Blue", "Green"]

        if colour in colours:
            return True
        else:
            return False

    def display_top_speed(self):
        print(f"Top Speed: {self.__top_speed}")

    def set_colour(self, new):
        if self.__validate_colour(new):
            self.colour = new

    def display_engine_size(self):
        print(f"Engine Size: {self.__engine_size}")

# Task 9.2
car1 = Car("Ford", "Escort", 80, "Estate", "Red", 1800)
car2 = Car("BMW", "330D", 110, "Salooon", "White", 2400)
car3 = Car("Mercedes", "SLS Black Series 500", 200, "Coupe", "Black", 5000)
car4 = Car("Lamborghini", "Murcialago", 141, "Coupe", "Red", 150000)

# Task 9.3
car2.set_colour("Red")
car2.display_engine_size()
car2.display_top_speed()