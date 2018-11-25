from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    peachyPrinter.return_string = True
    data = ['item one', 'item two', 'item three']

    output = peachyPrinter.peachy_print(data, 'basic list')
    print(output)
