class Giraffe():
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.height = 79
    def eat(self):
        food = input("how much do you want to feed your animal?")
        self.energy += int(food)
        print(f"you fed {self.name} {food} pieces of food there energy is currently {self.energy}")


Jeff = Giraffe("Jeff", 10)
Jeff.eat()