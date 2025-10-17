class Car:
    def __init__(self, make, model, top_speed, type, colour, engine_size):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.type = type
        self.colour = colour
        self.engine_size = engine_size

    def display_top_speed(self):
        print(f"Top Speed: {self.top_speed}")

    def set_colour(self, new):
        self.colour = new

    def display_engine_size(self):
        print(f"Engine Size: {self.engine_size}")

car1 = Car("Ford", "Escort", 80, "Estate", "Red", 1800)
car2 = Car("BMW", "330D", 110, "Salooon", "White", 2400)
car3 = Car("Mercedes", "SLS Black Series 500", 200, "Coupe", "Black", 5000)
car4 = Car("Lamborghini", "Murcialago", 141, "Coupe", "Red", 150000)