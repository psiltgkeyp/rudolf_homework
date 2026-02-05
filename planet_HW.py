class Planet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def diameter(self):
        return 2 * self.radius
earth = Planet("Земля", 6371)
print(earth.diameter())
