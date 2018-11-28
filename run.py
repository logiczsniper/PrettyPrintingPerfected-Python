from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    peachyPrinter.return_string = True
    data = [('item one', ('in nested tuple', ('hello',), 'yeah'), 'item two',
             'item three'), 70, 90, 'String', True, None,
            {'set item one', 'set item two', ('tuple set one', 'tuple set two'), 'set item three'},
            {'dict list': ['in dict one', 'in dict two', 'in dict three'], 'mighty': 'SEVEN', 'username': 'USERNAME'}]

    output = peachyPrinter.peachy_print(data, 'all the data in the world')
    print(output)
