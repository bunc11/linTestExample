import unittest
import SpaceX

class TestRocketMethods(unittest.TestCase):

    def setUp(self):
        print("Setting up")
        self.rocket = SpaceX.Rocket()

    def tearDown(self):
        print("Tearing down")
        self.rocket = None

    def test_rocket_initial_values(self):
        self.assertAlmostEqual(self.rocket.speed, 0.0,)
        self.assertAlmostEqual(self.rocket.acceleration, 0,0)
        self.assertEqual(self.rocket.engine, False)


    def test_acceleration_throws_exception(self):


        print("Testing exception raising")
        self.rocket.speed = 101
        with self.assertRaises(SpaceX.RocketException) as ar:
            self.rocket.accelerate()




if __name__ == "__main__":
    unittest.main()