import unittest

from deadzoned_joystick import is_in_deadzone as is_in_deadzone
 
class DeadZonedTest(unittest.TestCase):
    def test_deadzoned_center_p2(self):
        self.assertEqual(is_in_deadzone(.2, (0,0)), True)
    def test_deadzoned_2(self):
        self.assertEqual(is_in_deadzone(.2, (.2,.2)), False)
    def test_deadzoned_3(self):
        self.assertEqual(is_in_deadzone(1, (0.5,0.03)), True)
    def test_deadzoned_3(self):
        self.assertEqual(is_in_deadzone(1, (0.5,0.03)), True)

if __name__ == '__main__':
    unittest.main()
