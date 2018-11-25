from unittest import TestCase
from src.main import PeachyPrinter


class TestPeachyPrinter(TestCase):

    def setUp(self):
        self.printer = PeachyPrinter()
        self.printer.return_string = True

    def test_basic_data(self):
        output = self.printer.peachy_print(1989, 'You Should Not Do This')
        self.assertEqual('1989', output)

        output = self.printer.peachy_print('Prettify Me', 'You Should Not Do This')
        self.assertEqual('Prettify Me', output)

        output = self.printer.peachy_print(True, 'You Should Not Do This')
        self.assertEqual('True', output)

    def test_basic_list(self):
        input_data = ['item one', 'item two', 'item three']
        output = self.printer.peachy_print(input_data, 'basic list')
        self.assertEqual(
            '''Basic List
__________

1) Item one
2) Item two
3) Item three''', output)

    def test_basic_dict(self):
        input_data = {'key one': 'value one', 'key two': 'value two', 'key three': 'value three'}
        output = self.printer.peachy_print(input_data, 'basic dictionary')
        self.assertEqual(
            '''Basic Dictionary
________________

Key one -> value one
Key two -> value two
Key three -> value three''', output)

    def test_basic_set(self):
        input_data = {'item one', 'item two', 'item three'}
        output = self.printer.peachy_print(input_data, 'basic set')
        self.assertIn(
            '''Basic Set
_________

- Item''', output)

    def test_basic_tuple(self):
        input_data = ('item one', 'item two', 'item three')
        output = self.printer.peachy_print(input_data, 'basic tuple')
        self.assertEqual(
            '''Basic Tuple
___________

1) Item one
2) Item two
3) Item three''', output)

    def test_only_nested_lists(self):
        self.fail()

    def test_only_nested_dicts(self):
        self.fail()

    def test_only_nested_sets(self):
        self.fail()

    def test_only_nested_tuples(self):
        self.fail()

    def test_nested_all_data(self):
        self.fail()
