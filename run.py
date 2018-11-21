from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    groceries_list = ('apples', ('belvita bars', (234, 3453)), 'donuts', 'milk (organic)')

    output = peachyPrinter.peachy_print(groceries_list, 'User Data')
