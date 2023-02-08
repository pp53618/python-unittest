import unittest


class TestCase(unittest.TestCase):

    def test_case_1(self):
        self.assertIn('@', 'b.mackiewicz@wp.pl')

    def test_case_2(self):
        tech_stack = ['Java', 'sql', 'python', 'aws']
        self.assertIn('python', tech_stack)

    def test_case_3(self):
        tech_stack = ['Java', 'sql', 'python', 'aws']
        self.assertIn('c++', tech_stack)

    def test_case_4(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertIn('java', tech_stack)

    def test_case_5(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertNotIn('excel', tech_stack)