class Potion:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def drink(self):
        return f"Ты выпил {self.name}! Сила: {self.power}"
hp = Potion("Зелька хила", 50)
print(hp.drink())
