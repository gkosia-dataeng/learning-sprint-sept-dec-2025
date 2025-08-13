import unittest
from custom_program._SimpleProgram  import  calculate_sum



class TestSimpleProgram(unittest.TestCase):

    def setUp(self):
        # initialize fixtures
        self.input_list = [1,2,3]
    

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(*self.input_list), 6, "Should be 6")
        self.assertNotEqual(calculate_sum(*self.input_list), 8, "Sould not be 8")
    

'''
if __name__ == "__main__":
    unittest.main()
'''