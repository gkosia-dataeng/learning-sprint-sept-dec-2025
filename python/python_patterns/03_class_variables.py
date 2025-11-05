'''
    Problem: i want to have a common variable across the instances so when i update the value all instances to see the same value
    Solution: implement class variable and provide a classmethod to update it
'''


class Drone():
    direction = 'down' # class variable

    def __init__(self, id):
        self.id = id

    @classmethod 
    def set_direction(cls, direction):
        cls.direction = direction

    def give_the_direction(self):
        print(f"I am the drone {self.id} and going {Drone.direction}")


a_drone = Drone(1)
b_drone = Drone(2)

a_drone.give_the_direction()
b_drone.give_the_direction()

Drone.set_direction("up")


a_drone.give_the_direction()
b_drone.give_the_direction()