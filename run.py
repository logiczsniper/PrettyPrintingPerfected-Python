from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    data = {5: [3, 4, 5, 6, 7], 'hi': [34, 345, 4], '4': '4', 'tuple': ('in tuple one', 'in tuple two'),
            'my set': {'one', 'two', 'three', 'one', 5}}

    output = peachyPrinter.peachy_print(data, 'User Data')
