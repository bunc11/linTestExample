import App
import unittest

class TestCarMethods(unittest.TestCase):

    def test_default_speed(self):
        c = App.Car()
        self.assertEqual(c.speed, 0, "Initial speed tested")

    def test_acceleration(self):
        c = App.Car()
        c.accelerate()
        self.assertEqual(c.speed, 1, "Acceleration tested")

    def test_josNekaj(self):
        pass


