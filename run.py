from src.main import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    data = {'id': '8472883', 'name': 'UserName', 'password': 'Password'}

    output = peachyPrinter.peachy_print(data, 'user data')
