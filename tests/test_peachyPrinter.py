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
        input_data = ['item one', ['in nested one', 'in nested two', ['all the way in', ['core list']]], 'item two',
                      'item three']
        output = self.printer.peachy_print(input_data, 'nested lists')
        self.assertEqual(
            '''Nested Lists
____________

1) Item one
2) In nested one
3) In nested two
4) All the way in
5) Core list
6) Item two
7) Item three''', output)

    def test_only_nested_dicts(self):
        input_data = {'first key': 'first value',
                      'Dictionary two': {'second key': 'second value', 'dictionary three': {'core key': 'core value'}}}
        output = self.printer.peachy_print(input_data, 'nested dictionaries')
        self.assertEqual(
            '''Dictionary Three
________________

Core key -> core value

Dictionary Two
______________

Second key -> second value

Nested Dictionaries
___________________

First key -> first value''', output)

    def test_only_nested_tuples(self):
        input_data = (
            'item one', 'in nested one', ('in nested two', ('hello',), 'hu'), 'all the way in', 'core list', 'item two',
            'item three')
        output = self.printer.peachy_print(input_data, 'nested tuples')
        self.assertEqual(
            '''Nested Tuples
_____________

1) Item one
2) In nested one
3) In nested two
4) Hello
5) Hu
6) All the way in
7) Core list
8) Item two
9) Item three''', output)

    def test_nested_all_data(self):
        input_data = [('item one', ('in nested tuple', ('hello',), 'yeah'), 'item two',
                       'item three'), 70, 90, 'String', True, None,
                      {'set item one', 'set item two', ('tuple set one', 'tuple set two'), 'set item three'},
                      {'dict list': ['in dict one', 'in dict two', 'in dict three'], 'mighty': 'SEVEN',
                       'username': 'USERNAME'}]
        output = self.printer.peachy_print(input_data, 'nested everything')
        self.assertIn(
            '''Dict List
_________

1) In dict one
2) In dict two
3) In dict three

Nested Everything
_________________

1) Item one
2) In nested tuple
3) Hello
4) Yeah
5) Item two
6) Item three
7) 70
8) 90
9) String
10) True
11) None

Mighty -> SEVEN
Username -> USERNAME

- Set ''', output)
