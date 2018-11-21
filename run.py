from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    data = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
            {'id': '8472883', 'name': 'UserName', 'password': 'Password'}, 'milk (organic)',
            ['hello_four', ['hello_five']],
            'twinkies', 'yogurt', {'id': '456', 'name': ['item one', 'item two', 'item three'], 'password': 'yo'}]

    output = peachyPrinter.peachy_print(data, 'User Data')
