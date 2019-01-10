import unittest

from deadzoned_joystick import is_in_deadzone as is_in_deadzone
 
class DeadZonedTest(unittest.TestCase):
    def test_deadzoned_center_p2(self):
        self.assertEqual(is_in_deadzone(.2, (0,0)), True)


if __name__ == '__main__':
    unittest.main()
