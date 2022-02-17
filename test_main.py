import unittest
import main
true_options = ['apple|apple', 'ap|apple', 'le|apple', 'a|apple', '.|apple', 'colou?r|color', 'colou?r|colour',
                'colou*r|color', 'colou*r|colour', 'colou*r|colouur', 'col.*r|color', 'col.*r|colour',
                'col.*r|colr', 'col.*r|collar', '\.$|end.', '3\+3|3+3=6', '\?|Is this working?']
false_options = ['apwle|apple', 'peach|apple', 'colou?r|colouur', 'col.*r$|colors', 'colou\?r|color', 'colou\?r|colour']


class TestRegex(unittest.TestCase):  # a test case for the calculator.py module


    def test_regexp(self):
        # tests for the add() function
        for opt in true_options:
            self.assertEqual(main.check_string(*opt.split('|')), True, f"{opt.split('|')}")
        for opt in false_options:
            self.assertEqual(main.check_string(*opt.split('|')), False, f"{opt.split('|')}")


if __name__ == "__main__":
    unittest.main()
