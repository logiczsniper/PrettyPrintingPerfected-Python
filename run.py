from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    data = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
            'donuts', 'milk (organic)', ['hello_four', ['hello_five']],
            'twinkies', 'yogurt']

    output = peachyPrinter.peachy_print(data, 'User Data')
