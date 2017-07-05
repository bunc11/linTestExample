class RocketException(Exception):
    pass


class Rocket:
    def __init__(self):
        self.speed = 0.0
        self.engine = False
        self.acceleration = 0.0

    def turnOn(self) -> None:
        self.engine = True

    def accelerate(self) -> None:
        if self.speed > 100:
            raise RocketException

        self.speed += .1




